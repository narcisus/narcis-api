from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from . import Base
from .named_model import NamedModel

class Branch(Base, NamedModel):
    project_id = Column(Integer, ForeignKey('project.id'))

    project = relationship('Project', back_populates='branches')
    builds = relationship('Build', back_populates='branch')

    __tablename__ = 'branch'
    __table_args__ = (
        UniqueConstraint('name_slug', 'project_id'),
    )
