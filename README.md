# AI Test Project

This is a test repository for validating the AI-driven development automation system.

## Purpose

This repository simulates a real AI development project and is used to test:

- Automated environment provisioning via K8s
- CircleCI integration and validation workflows
- Dynamic configuration based on environment variables
- Push-based validation and feedback loops
- Jira ticket integration

## Project Structure

```
ai-test-project/
├── src/                    # Source code
├── tests/                  # Test files
├── config/                 # Configuration files
├── .circleci/             # CircleCI configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Development Workflow

1. AI agent requests development environment for specific Jira ticket
2. Automation system provisions K8s pod with proper configuration
3. AI agent develops and commits code
4. CircleCI validates code on push
5. Feedback is provided to AI agent via webhook
6. Valid code is ready for merge

## Environment Variables

- `ENV`: Target environment (DEV, INTEGRATION, STAGING, PROD)
- `JIRA_TICKET`: Associated Jira ticket ID
- `AI_AGENT_ID`: Identifier for the AI agent

## Getting Started

This repository is designed to work with the AI development automation system.
Do not manually clone or work with this repository directly.

Instead, use the automation system:

```bash
# On the orchestration server (198.91.25.229)
./boot-dev-container.sh --ticket PROJ-123 --env DEV
```

## Automation System Repository

The automation system itself is maintained at:
https://github.com/W3EvolutionsLLC/ai-dev-automation
