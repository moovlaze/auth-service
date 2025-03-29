from sqlalchemy import Column, Integer, String, DateTime, Index

from .base import Base


class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    description = Column(String)
    event_date = Column(DateTime)
    available_tickets = Column(Integer)
    ticket_price = Column(Integer)

    __table_args__ = (Index("idx_events_event-date", "event_date"),)
