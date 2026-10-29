import json
from .confidence import confidence_colour

class SkillAgent:
    def __init__(self, llm, tool_registry):
        self.llm = llm
        self.tools = tool_registry

    def run(self, skill, context):
        allowed = skill.metadata.get("allowed-tools", [])
        available = [
            t for t in self.tools.descriptions()
            if t["name"] in allowed
        ]

        system_prompt = f'''
You are executing the skill named "{skill.name}".

SKILL INSTRUCTIONS
==================
{skill.instructions}

AVAILABLE TOOLS
===============
{json.dumps(available, indent=2)}

EXECUTION RULES
===============
1. Follow the skill instructions exactly.
2. Use only tools declared in the skill.
3. Never invent tool results.
4. Separate evidence from inference.
5. Return valid JSON only.
6. Do not return Markdown fences.
'''

        # The loaded .md skill reaches the LLM through system_prompt.
        result = self.llm.generate_json(system_prompt, context)

        if "confidence" in result:
            result["confidence_colour"] = confidence_colour(
                float(result["confidence"])
            )

        return result
