---
name: github-context
description: Retrieve relevant GitHub repository, issue, pull request or commit information when an incident contains a GitHub reference.
version: 1.0.0
metadata:
  author: incident-platform
  lifecycle: active
compatibility:
  runtime: python3
allowed-tools:
  - github_search
license: internal
---

# Skill Intent / Purpose

The GitHub Context skill enriches an investigation with information from GitHub.
It should be activated only when the incident contains a GitHub reference.

# Inputs Required

1. Incident metadata
2. GitHub URL, repository name, issue, pull request or commit reference

# Process Steps / Workflows

1. Detect GitHub references.
2. Extract repository, issue, pull request or commit identifiers.
3. Query `github_search`.
4. Retrieve only information relevant to the incident.
5. Correlate relevant changes with the incident.
6. Return factual GitHub evidence and clearly label inference.

# Output Specification

Return JSON:
{
  "repository": "string",
  "references": ["string"],
  "evidence": ["string"],
  "relevant_changes": ["string"]
}

# Tools to be used

- `github_search`: GitHub repositories, issues, pull requests and commits.
