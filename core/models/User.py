from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

Base = declarative_base()

class User(Base):
  __tablename__ = "user"
  
  id = Column(Integer, primary_key=True)
  first_name = Column(String(60))
  last_name = Column(String(60))
  username = Column(String(30))
  shopee_email = Column(String(60))
  accepted_term = Column(Boolean())