from datetime import datetime

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from . import controllers
from src.core.schemas import SEventsID, SMessage
from src.core.helpers import get_db_session

router = APIRouter()


@router.get("/events/{event_id}")
def get_event_by_id(
    event_id: int,
    session: Session = Depends(get_db_session),
) -> SEventsID | SMessage:
    return controllers.get_event_by_id(id=event_id, session=session)


@router.get("/events/")
def get_events_by_date(
    date_from: datetime,
    date_to: datetime,
    page: int = Query(..., gt=0),
    items_count: int = Query(..., gt=0),
    session: Session = Depends(get_db_session),
) -> list[SEventsID]:
    return controllers.get_events_by_date(
        date_from=date_from,
        date_to=date_to,
        page=page,
        items_count=items_count,
        session=session,
    )
