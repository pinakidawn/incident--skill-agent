from typing import List
from pydantic import BaseModel, Field

class Incident(BaseModel):
    title: str
    short_description: str
    description: str

class RCAResult(BaseModel):
    root_cause: str
    analysis: str
    evidence: List[str]
    historical_correlation: List[str]
    uncertainties: List[str]
    confidence: float = Field(ge=0, le=100)
    confidence_colour: str

class ResolutionStep(BaseModel):
    step: int
    action: str
    reason: str
    source: str

class ResolutionResult(BaseModel):
    resolution_summary: str
    steps: List[ResolutionStep]
    validation_steps: List[str]
    rollback: List[str]
    historical_solutions_used: List[str]
    uncertainties: List[str]
    confidence: float = Field(ge=0, le=100)
    confidence_colour: str

class IncidentResult(BaseModel):
    incident: Incident
    rca: RCAResult
    resolution: ResolutionResult
