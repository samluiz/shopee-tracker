from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

class SqliteConfig:
    engine = create_engine("sqlite:///core/db/shopeetracker.db", echo=True, future=True)
    Base = declarative_base()
    Base.metadata.bind = engine

    @classmethod
    def get_session(cls):
        Session = scoped_session(sessionmaker(bind=cls.engine, autoflush=True))
        session = Session()
        return session

    @classmethod
    def get_base(cls):
        return cls.Base

    @classmethod
    def init_db(cls):
        cls.Base.metadata.create_all(cls.engine)