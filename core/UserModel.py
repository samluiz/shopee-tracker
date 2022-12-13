from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///core/db/shopeetracker.db", echo=True)
Base = declarative_base()
Base.metadata.bind = engine
Session = scoped_session(sessionmaker(bind=engine, autoflush=True))
session = Session()

class User(Base):
  __tablename__ = "user"
  
  id = Column(Integer, primary_key=True, autoincrement="auto")  
  telegram_id = Column(Integer)
  first_name = Column(Text)
  last_name = Column(Text)
  username = Column(Text)
  
  def __repr__(self):
    return f"ID: {self.telegram_id}\nName: {self.first_name} {self.last_name}\nUsername: {self.username}"
    
  def get_user(id):
    return session.get(User, id)
  
  def get_user_by_username(username):
    return select(User).filter_by(username=username)
  
  def create_user(self, telegram_id, first_name, last_name, username):
    new_user=User(telegram_id=telegram_id, first_name=first_name, last_name=last_name, username=username)
    session.add(new_user)
    session.commit()
    
  def update_user(**kwargs):
    session.merge(kwargs)
    
  def delete_user(id):
    session.delete(id)
    
def init_db():
  Base.metadata.create_all(engine)
    
if __name__ == "__main__":
  init_db()