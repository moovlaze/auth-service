from datetime import datetime

from pydantic import BaseModel


class SEventsBase(BaseModel):
    name: str
    description: str
    event_date: datetime
    available_tickets: int
    ticket_price: int


class SEventsID(SEventsBase):
    id: int


class SEventsCreate(SEventsBase):
    pass


class SEventsUpdate(SEventsBase):
    name: str
    description: str
    event_date: datetime
    available_tickets: int
    ticket_price: int


class SMessage(BaseModel):
    status: str = "status"
    message: str = "message"
