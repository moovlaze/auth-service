from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    description = Column(String)
    event_date = Column(DateTime)
    available_tickets = Column(Integer)
    ticket_price = Column(Integer)
