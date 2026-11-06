from ticket_triage.graph import build_graph
from ticket_triage.tickets import load_tickets


def test_loads_24_tickets():
    tickets = load_tickets()
    assert len(tickets) == 24
    assert {t.expected_route for t in tickets} == {"billing", "orders"}


def test_escalations_have_no_tool_calls():
    for t in load_tickets():
        if t.should_escalate:
            assert t.expected_tool_calls == ()


def test_graph_runs():
    out = build_graph().invoke({"subject": "x", "message_body": "y"})
    assert "route" in out
