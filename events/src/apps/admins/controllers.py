from sqlalchemy import select
from sqlalchemy.orm import Session

# from src.core.helpers import Session
from src.core.orm_models import Events
from src.core.repository import IEventRepository, get_event_repository


def create_event(
    data: Events, session: Session, repo: IEventRepository = get_event_repository()
) -> dict[str, str]:
    new_event = Events(**data.model_dump())

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
    id: int,
    data: Events,
    session: Session,
    repo: IEventRepository = get_event_repository(),
) -> dict[str, str]:
    stmt = select(Events).where(Events.id == id)
    event: Events = session.execute(stmt).scalars().first()

    if not event:
        return {"status": "flase", "message": "record not found"}

    for key, val in data.model_dump().items():
        setattr(event, key, val)

    session.commit()

    repo.send(
        "Update",
        f"Update event {event.id}:\n"
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
    id: int, session: Session, repo: IEventRepository = get_event_repository()
) -> dict[str, str]:
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
