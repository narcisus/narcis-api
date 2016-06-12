from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from . import Base
from .named_model import NamedModel

class Page(Base, NamedModel):
    path = Column(String)
    project_id = Column(Integer, ForeignKey('project.id'))

    project = relationship('Project', back_populates='pages')

    __tablename__ = 'page'
    __table_args__ = (
        UniqueConstraint('name_slug', 'project_id'),
    )
