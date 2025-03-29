from datetime import datetime

from pydantic import BaseModel, Field


class SEventsBase(BaseModel):
    name: str
    description: str
    event_date: datetime
    available_tickets: int = Field(..., gt=-1)
    ticket_price: int = Field(..., gt=0)


class SEventsID(SEventsBase):
    id: int


class SEventsCreate(SEventsBase):
    pass


class SEventsUpdate(SEventsBase):
    pass


class SMessage(BaseModel):
    status: str = "status"
    message: str = "message"
