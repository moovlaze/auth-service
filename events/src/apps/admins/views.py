from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.schemas import SEventsCreate, SEventsUpdate, SMessage
from src.core.helpers import get_db_session
from . import controllers


router = APIRouter(tags=["Admins API"])


@router.post("/events/")
def create_event(
    body: SEventsCreate,
    session: Session = Depends(get_db_session),
) -> SMessage:
    return controllers.create_event(data=body, session=session)


@router.put("/events/{event_id}")
def update_event(
    event_id: int,
    body: SEventsUpdate,
    session: Session = Depends(get_db_session),
) -> SMessage:
    return controllers.update_event(id=event_id, data=body, session=session)


@router.delete("/events/{event_id}")
def delete_event(
    event_id: int,
    session: Session = Depends(get_db_session),
) -> SMessage:
    return controllers.delete_event(id=event_id, session=session)
