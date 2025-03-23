from fastapi import APIRouter

router = APIRouter()


@router.get("/events/{event_id}")
def get_event_by_id(event_id: int):
    return event_id


@router.get("/events/")
def get_events_by_date(date_from: str, date_to: str, page: int, items_count: int):
    return [date_from, date_to, page, items_count]
