from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import Boolean
from Setup import BASE, SESSION

class User(BASE):
  __tablename__ = "user"
  
  id = Column(Integer, primary_key=True, autoincrement="auto")  
  telegram_id = Column(Integer)
  first_name = Column(Text)
  last_name = Column(Text)
  username = Column(Text)
  accepted_term = Column(Boolean)
  
  def __repr__(self):
    return f"Name: {self.first_name} {self.last_name}\nUsername: {self.username}"
  
  def get_user(id):
    return SESSION.get(User, id)
  
  def create_user(*user):
    SESSION.add(user)
    SESSION.commit(user)
    
  def update_user(**kwargs):
    SESSION.merge(kwargs)
    
  def delete_user(id):
    SESSION.delete(id)