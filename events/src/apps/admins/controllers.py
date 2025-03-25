from sqlalchemy import select

from src.core.helpers import Session
from src.core.orm_models import Events


def create_event(data: Events) -> dict[str, str]:
    with Session() as session:
        new_event = Events(
            name=data.name,
            description=data.description,
            event_date=data.event_date,
            available_tickets=data.available_tickets,
            ticket_price=data.ticket_price,
        )

        session.add(new_event)
        session.commit()

        return {"status": "OK", "message": f"create new event, name event: {data.name}"}


def update_event(id: int, data: Events) -> dict[str, str]:
    with Session() as session:
        stmt = select(Events).where(Events.id == id)
        event: Events = session.execute(stmt).scalars().first()

        if event:
            event.name = data.name
            event.description = data.description
            event.event_date = data.event_date
            event.available_tickets = data.available_tickets
            event.ticket_price = data.ticket_price

        session.commit()

        return {
            "status": "ok",
            "message": f"The record: {data.name} is successfully updated",
        }


def delete_event(id: int) -> dict[str, str]:
    with Session() as session:
        stmt = select(Events).where(Events.id == id)
        event: Events = session.execute(stmt).scalars().first()

        if event:
            event.soft_delete()

        session.commit()

        return {
            "status": "ok",
            "message": "The record deleted",
        }
