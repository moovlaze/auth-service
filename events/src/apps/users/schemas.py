from datetime import datetime

from pydantic import BaseModel


class SEvents(BaseModel):
    id: int
    name: str
    description: str
    event_date: datetime
    available_tickets: int
    ticket_price: int
