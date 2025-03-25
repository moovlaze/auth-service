from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

# from src.core.helpers import Session
from src.core.orm_models import Events


def get_event_by_id(
    id: int,
    session: Session,
) -> Events | dict[str, str]:
    # with Session() as session:
    stmt = select(Events).where(Events.id == id)
    event = session.execute(stmt).scalars().first()
    if event.delete_at:
        return {"status": "delete", "message": "this event delete"}
    return event


def get_events_by_date(
    date_from: datetime,
    date_to: datetime,
    page: int,
    items_count: int,
    session: Session,
) -> list[Events]:
    # with Session() as session:
    stmt = select(Events).where(
        Events.event_date >= date_from,
        Events.event_date <= date_to,
        Events.available_tickets > 0,
        Events.delete_at.is_(None),
    )
    stmt = stmt.offset((page - 1) * items_count).limit(items_count)
    events = session.execute(stmt).scalars().all()
    return events
