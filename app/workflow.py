from .models import Incident, RCAResult, ResolutionResult, IncidentResult

class IncidentWorkflow:
    def __init__(self, skill_loader, agent):
        self.skills = skill_loader.load_all()
        self.agent = agent

    def execute(self, incident: Incident):
        # ============================================================
        # STEP 1: RCA
        # ============================================================
        rca_skill = self.skills["rca"]

        rca = self.agent.run(
            rca_skill,
            {"incident": incident.model_dump()}
        )
        rca_result = RCAResult(**rca)

        # ============================================================
        # STEP 2: RESOLUTION
        # Resolution starts only after RCA is completed/validated.
        # ============================================================
        resolution_skill = self.skills["resolution"]

        resolution = self.agent.run(
            resolution_skill,
            {
                "incident": incident.model_dump(),
                "rca": rca_result.model_dump()
            }
        )
        resolution_result = ResolutionResult(**resolution)

        return IncidentResult(
            incident=incident,
            rca=rca_result,
            resolution=resolution_result
        )
