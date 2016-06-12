from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import Base
from .model import Model

class Screenshot(Base, Model):
    image = Column(String)
    page_id = Column(Integer, ForeignKey('page.id'))
    platform_id = Column(Integer, ForeignKey('platform.id'))
    build_id = Column(Integer, ForeignKey('build.id'))

    page = relationship('Page')
    platform = relationship('Platform')
    build = relationship('Build')

    __tablename__ = 'screenshot'
