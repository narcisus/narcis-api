from sqlalchemy import Column, Boolean, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from . import Base
from .named_model import NamedModel

class Project(Base, NamedModel):
    private = Column(Boolean)
    url = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='projects')
    platforms = relationship('Platform', back_populates='project')
    pages = relationship('Page', back_populates='project')
    branches = relationship('Branch', back_populates='project')

    __tablename__ = 'project'
    __table_args__ = (
        UniqueConstraint('name_slug', 'user_id'),
    )
