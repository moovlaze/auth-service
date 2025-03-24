from fastapi import APIRouter

router = APIRouter(tags="Admins API")


@router.post("/events/")
def create_event():
    pass


@router.put("/events/{event_id}")
def update_event():
    pass


@router.delete("/events/{event_id}")
def delete_event():
    pass
