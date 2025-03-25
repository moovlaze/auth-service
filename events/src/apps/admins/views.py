from fastapi import APIRouter

from src.core.schemas import SEventsCreate, SEventsUpdate, SMessage
from . import controllers


router = APIRouter(tags=["Admins API"])


@router.post("/events/")
def create_event(body: SEventsCreate) -> SMessage:
    return controllers.create_event(data=body)


@router.put("/events/{event_id}")
def update_event(event_id: int, body: SEventsUpdate) -> SMessage:
    return controllers.update_event(id=event_id, data=body)


@router.delete("/events/{event_id}")
def delete_event(event_id: int) -> SMessage:
    return controllers.delete_event(id=event_id)
