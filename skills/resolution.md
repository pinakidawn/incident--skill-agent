---
name: resolution
description: Generate safe and actionable incident resolution steps using the completed RCA and similar historical solutions from Confluence.
version: 1.0.0
metadata:
  author: incident-platform
  lifecycle: active
compatibility:
  runtime: python3
allowed-tools:
  - confluence_search
license: internal
---

# Skill Intent / Purpose

The Resolution skill generates a practical resolution procedure only after RCA
has completed. It must use the RCA and validated historical solutions.

# Inputs Required

1. Original incident metadata
2. Completed RCA
3. RCA evidence
4. Similar historical incidents
5. Historical resolution/SOP information

# Process Steps / Workflows

1. Read the incident metadata and completed RCA.
2. Search Confluence for the same/similar root cause, application/component,
   errors and successful historical resolutions.
3. Rank historical solutions by relevance.
4. Generate actionable resolution steps based primarily on validated historical
   solutions.
5. If reliable historical evidence is unavailable, mark an action as
   "recommended" rather than "historical".
6. Include validation after remediation.
7. Include rollback considerations where relevant.
8. Never claim that remediation has been executed.
9. Assign a resolution-only confidence score from 0 to 100.
10. Confidence colour is GREEN when >85, AMBER when 70-85, RED when <70.

# Output Specification

Return JSON:
{
  "resolution_summary": "string",
  "steps": [
    {
      "step": 1,
      "action": "string",
      "reason": "string",
      "source": "historical|recommended"
    }
  ],
  "validation_steps": ["string"],
  "rollback": ["string"],
  "historical_solutions_used": ["string"],
  "uncertainties": ["string"],
  "confidence": 0,
  "confidence_colour": "GREEN|AMBER|RED"
}

Do not calculate or report an overall confidence.

# Tools to be used

- `confluence_search`: historical incidents and validated solutions.

The skill must not directly execute production remediation.
