from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base
from .model import Model

class User(Base, Model):
    username = Column(String)
    display_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    projects = relationship('Project', back_populates='user')

    __tablename__ = 'user'
