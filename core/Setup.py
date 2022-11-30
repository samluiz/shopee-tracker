from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

def start_database() -> scoped_session:
  engine = create_engine("sqlite:///shopeetracker.db", echo=True, future=True)
  BASE.metadata.bind = engine
  BASE.metadata.create_all(engine)
  return scoped_session(sessionmaker(bind=engine, autoflush=True))

BASE = declarative_base()
SESSION = start_database()