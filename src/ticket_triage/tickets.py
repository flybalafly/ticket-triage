import csv
from dataclasses import dataclass
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parents[2] / "data" / "tickets.csv"


@dataclass(frozen=True)
class Ticket:
    ticket_id: str
    subject: str
    message_body: str
    merchant_country: str
    expected_route: str
    expected_tool_calls: tuple[str, ...]
    expected_fix: str
    is_two_problem: bool
    should_escalate: bool


def load_tickets(path: Path = DEFAULT_PATH) -> list[Ticket]:
    with open(path, newline="", encoding="utf-8") as f:
        return [
            Ticket(
                ticket_id=r["ticket_id"],
                subject=r["subject"],
                message_body=r["message_body"],
                merchant_country=r["merchant_country"],
                expected_route=r["expected_route"],
                expected_tool_calls=tuple(t for t in r["expected_tool_calls"].split(";") if t),
                expected_fix=r["expected_fix"],
                is_two_problem=r["is_two_problem"] == "true",
                should_escalate=r["should_escalate"] == "true",
            )
            for r in csv.DictReader(f)
        ]
