import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Lemma

from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def is_table_empty():
    with get_db() as db:
        return db.query(Lemma).first() is None