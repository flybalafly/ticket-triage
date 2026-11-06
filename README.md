# ticket-triage

A [LangGraph](https://langchain-ai.github.io/langgraph/) project for triaging Shopify merchant support tickets.

## Test set

`data/tickets.csv` holds 24 labelled tickets. Key columns:

| column | meaning |
| --- | --- |
| `expected_route` | `billing` or `orders` |
| `expected_tool_calls` | semicolon-separated tools an ideal run would call |
| `expected_fix` | the resolution a good agent should reach |
| `is_two_problem` | ticket contains two distinct problems |
| `should_escalate` | must be handed to a human advisor |

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Layout

- `src/ticket_triage/tickets.py` – CSV loader
- `src/ticket_triage/graph.py` – LangGraph workflow (placeholder router, to be replaced with an LLM classifier)
