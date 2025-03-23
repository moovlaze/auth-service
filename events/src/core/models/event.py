from datetime import datetime


class Event:
    id: int
    name: str
    description: str
    event_date: datetime
    available_tickets: int
    ticket_price: int
