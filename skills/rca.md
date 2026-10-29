---
name: rca
description: Analyze an IT incident and determine its most probable root cause using incident metadata, live logs, and historical incident information from Confluence.
version: 1.0.0
metadata:
  author: incident-platform
  lifecycle: active
compatibility:
  runtime: python3
allowed-tools:
  - live_logs
  - confluence_search
license: internal
---

# Skill Intent / Purpose

The RCA skill analyzes an incident and identifies the most probable root cause
using available technical evidence. It must prefer factual evidence over assumptions.

# Inputs Required

1. Incident title
2. Incident short description
3. Incident description
4. Live application/system logs
5. Historical incidents retrieved from Confluence

# Process Steps / Workflows

1. Read the incident metadata.
2. Identify affected application/component, symptoms, errors, timestamps,
   identifiers, environment and impact.
3. Query `live_logs` using relevant identifiers and symptoms.
4. Search `confluence_search` for the same error, application, component and
   similar historical symptoms.
5. Correlate current logs with historical incidents.
6. Determine the most probable root cause.
7. Explicitly distinguish observed facts, historical evidence, inference and
   unresolved uncertainty.
8. Never invent evidence.
9. Assign an RCA-only confidence score from 0 to 100.
10. Confidence colour is GREEN when >85, AMBER when 70-85, RED when <70.

# Output Specification

Return JSON:
{
  "root_cause": "string",
  "analysis": "string",
  "evidence": ["string"],
  "historical_correlation": ["string"],
  "uncertainties": ["string"],
  "confidence": 0,
  "confidence_colour": "GREEN|AMBER|RED"
}

Do not calculate or report an overall confidence.

# Tools to be used

- `live_logs`: current application/system logs.
- `confluence_search`: historical incidents and RCA information.

The skill must not execute remediation.
