import os
from dotenv import load_dotenv
from fastapi import FastAPI

from .models import Incident
from .skill_loader import SkillLoader
from .agent import SkillAgent
from .llm import LLMClient
from .workflow import IncidentWorkflow

from .tools.registry import ToolRegistry
from .tools.logs import LiveLogsTool
from .tools.confluence import ConfluenceSearchTool
from .tools.github import GitHubSearchTool

load_dotenv()

app = FastAPI(title="Skill-Based Incident Agent", version="1.0.0")

def build_application():
    registry = ToolRegistry()
    registry.register(LiveLogsTool())
    registry.register(ConfluenceSearchTool())
    registry.register(GitHubSearchTool())

    llm = LLMClient()
    loader = SkillLoader("skills")
    agent = SkillAgent(llm, registry)

    return IncidentWorkflow(loader, agent)

workflow = build_application()

@app.get("/health")
def health():
    return {"status": "UP", "skills": list(workflow.skills.keys())}

@app.get("/skills")
def skills():
    return {
        name: {
            "description": skill.description,
            "allowed_tools": skill.metadata.get("allowed-tools", [])
        }
        for name, skill in workflow.skills.items()
    }

@app.post("/incident/analyze")
def analyze_incident(incident: Incident):
    return workflow.execute(incident).model_dump()
