from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Lemma(Base):
    __tablename__ = 'lemma'

    id = Column(Integer, primary_key=True, autoincrement=True)
    lemma_id = Column(Integer)
    word = Column(String)
    lemma = Column(String)
    pos = Column(String)

    def __repr__(self):
        return f'Lemma: {self.lemma_id}, {self.word}, {self.pos}, {self.lemma}'
