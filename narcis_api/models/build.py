from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from . import Base
from .named_model import NamedModel

class Build(Base, NamedModel):
    branch_id = Column(Integer, ForeignKey('branch.id'))

    branch = relationship('Branch', back_populates='builds')
    screenshots = relationship('Screenshot', back_populates='build')

    __tablename__ = 'build'
    __table_args__ = (
        UniqueConstraint('name_slug', 'branch_id'),
    )
