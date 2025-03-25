from sqlalchemy import select

from src.core.helpers import Session
from src.core.orm_models import Events
from src.core.repository import IEventRepository, get_event_repository


def create_event(
    data: Events, repo: IEventRepository = get_event_repository()
) -> dict[str, str]:
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

        repo.send(
            "Create",
            f"New event {new_event.id}:\n"
            f"{new_event.name}\n"
            f"{new_event.description}\n"
            f"{new_event.event_date}\n"
            f"{new_event.available_tickets}\n"
            f"{new_event.ticket_price}",
        )

        return {
            "status": "OK",
            "message": f"create new event, name event: {new_event.name}",
        }


def update_event(
    id: int, data: Events, repo: IEventRepository = get_event_repository()
) -> dict[str, str]:
    with Session() as session:
        stmt = select(Events).where(Events.id == id)
        event: Events = session.execute(stmt).scalars().first()

        if not event:
            return {"status": "flase", "message": "record not found"}

        event.name = data.name
        event.description = data.description
        event.event_date = data.event_date
        event.available_tickets = data.available_tickets
        event.ticket_price = data.ticket_price

        session.commit()

        repo.send(
            "Create",
            f"update event {event.id}:\n"
            f"{event.name}\n"
            f"{event.description}\n"
            f"{event.event_date}\n"
            f"{event.available_tickets}\n"
            f"{event.ticket_price}",
        )

        return {
            "status": "ok",
            "message": f"The record: {event.name} is successfully updated",
        }


def delete_event(
    id: int, repo: IEventRepository = get_event_repository()
) -> dict[str, str]:
    with Session() as session:
        stmt = select(Events).where(Events.id == id)
        event: Events = session.execute(stmt).scalars().first()

        if not event:
            return {"status": "flase", "message": "record not found"}

        event.soft_delete()

        session.commit()

        repo.send(
            "Soft-delete",
            f"Soft-elete event {event.id}:\n",
        )

        return {
            "status": "ok",
            "message": "The record deleted",
        }
