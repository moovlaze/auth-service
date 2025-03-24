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
