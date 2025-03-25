from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.orm_models import Base

engine = create_engine("postgresql+psycopg://postgres:postgres@localhost:5432/postgres")

Session = sessionmaker(bind=engine)


def init_db():
    # Base.metadata.clear()
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
