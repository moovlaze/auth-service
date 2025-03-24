from datetime import datetime

from sqlalchemy import select

from src.core.helpers import Session
from src.core.orm_models import Events


def get_event_by_id(id: int) -> Events:
    with Session() as session:
        stmt = select(Events).where(Events.id == id)
        event = session.execute(stmt).scalars().first()
        return event


def get_events_by_date(
    date_from: datetime,
    date_to: datetime,
    page: int,
    items_count: int,
) -> list[Events]:
    with Session() as session:
        stmt = select(Events).where(
            Events.event_date >= date_from,
            Events.event_date <= date_to,
            Events.available_tickets >= 0,
        )
        stmt = stmt.offset((page - 1) * items_count).limit(items_count)
        events = session.execute(stmt).scalars().all()
        return events
