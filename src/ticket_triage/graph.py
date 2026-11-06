from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class TriageState(TypedDict, total=False):
    subject: str
    message_body: str
    route: str  # "billing" | "orders"


def classify(state: TriageState) -> TriageState:
    # Placeholder: swap for an LLM classifier.
    return {"route": "billing"}


def build_graph():
    g = StateGraph(TriageState)
    g.add_node("classify", classify)
    g.add_edge(START, "classify")
    g.add_edge("classify", END)
    return g.compile()
