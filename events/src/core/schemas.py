from datetime import datetime

from pydantic import BaseModel


class SEventsBase(BaseModel):
    id: int


class SEvents(SEventsBase):
    name: str
    description: str
    event_date: datetime
    available_tickets: int
    ticket_price: int


class SEventsUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    event_date: datetime | None = None
    available_tickets: int | None = None
    ticket_price: int | None = None
