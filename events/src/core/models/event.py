from time import time


class Event:
    id: int
    name: str
    description: str
    event_date: time
    available_tickets: int
    ticket_price: int
