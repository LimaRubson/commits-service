# backend/model/models.py
from sqlalchemy import create_engine, Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import config

Base = declarative_base()

class Commit(Base):
    __tablename__ = 'commits'
    id = Column(Integer, primary_key=True, autoincrement=True)
    commit_time = Column(TIMESTAMP, nullable=False)
    commit_id = Column(String, nullable=False)
    ticket_id = Column(Integer, nullable=False)
    commit_text = Column(String, nullable=False)
    prediction = Column(Float, nullable=False)
    label_status = Column(String, nullable=False)
    history_datetime = Column(TIMESTAMP, nullable=False)

# Criar o engine e a sessão
engine = create_engine(config.DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()