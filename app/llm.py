import json
import os
from openai import OpenAI

class LLMClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.model = os.getenv("LLM_MODEL", "gpt-5.6-luna")

    def generate_json(self, system_prompt: str, context: dict):
        # ============================================================
        # LLM CALL - this is the single LLM integration point.
        # ============================================================
        response = self.client.responses.create(
            model=self.model,
            instructions=system_prompt,
            input=json.dumps(context, indent=2, default=str)
        )
        # ============================================================
        # END LLM CALL
        # ============================================================
        text = response.output_text
        return json.loads(text)
