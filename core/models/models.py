from sqlalchemy.orm import relationship, relationship
from sqlalchemy import Column, Integer, Boolean, ForeignKey, Text, select, Enum, ForeignKey
from passlib.hash import bcrypt
from models.enums import Status, Platform
from config.database import SqliteConfig

config = SqliteConfig()
Base = config.get_base()
session = config.get_session()

class User(Base):
  __tablename__ = "user"
  
  id = Column(Integer, primary_key=True, autoincrement="auto")  
  telegram_id = Column(Integer)
  first_name = Column(Text)
  last_name = Column(Text)
  username = Column(Text)
  login = Column(Text)
  password = Column(Text)
  status = Column(Enum(Status))
  user_accepted = Column(Boolean)
  orders = relationship("Order", back_populates="user")
  
  def __repr__(self):
    return f"ID: {self.telegram_id}\nName: {self.first_name} {self.last_name}\nUsername: {self.username}"
    
  def get_user(id):
    return session.get(User, id)
  
  def get_user_by_username(username):
    return select(User).filter_by(username=username)
  
  def get_user_status_by_id(id):
    return select(User.status).filter_by(id=id)
  
  def get_user_accept_by_id(id):
    return select(User.user_accepted).filter_by(id=id)
  
  def create_user(self, telegram_id, first_name, last_name, username, login, password, status, user_accepted):
    new_user=User(telegram_id=telegram_id, first_name=first_name, last_name=last_name, username=username, login=login, password=bcrypt.hash(password), status=status, user_accepted=user_accepted)
    session.add(new_user)
    session.commit()
    
  def update_password(self, password):
    updated_user = User(password=bcrypt.hash(password))
    session.update(updated_user)
    session.commit()
    
  def update_status(self, status):
    updated_user = User(status=status)
    session.update(updated_user)
    session.commit()
    
  def delete_user(id):
    session.delete(id)
    session.commit()
  
class Order(Base):
  __tablename__ = "order"
  
  id = Column(Integer, primary_key=True, autoincrement="auto") 
  order_id = Column(Integer)
  user_id = Column(Integer, ForeignKey(User.id))
  platform = Column(Enum(Platform))
  user = relationship("User", back_populates="orders")