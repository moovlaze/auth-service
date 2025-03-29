from datetime import datetime

from fastapi import APIRouter, Query

from . import controllers
from .schemas import SEvents

router = APIRouter()


@router.get("/events/{event_id}")
def get_event_by_id(event_id: int) -> SEvents:
    return controllers.get_event_by_id(id=event_id)


@router.get("/events/")
def get_events_by_date(
    date_from: datetime,
    date_to: datetime,
    page: int = Query(..., gt=0),
    items_count: int = Query(..., gt=0),
) -> list[SEvents]:
    return controllers.get_events_by_date(
        date_from=date_from,
        date_to=date_to,
        page=page,
        items_count=items_count,
    )
