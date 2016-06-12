from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import Base
from .named_model import NamedModel

class Platform(Base, NamedModel):
    device_id = Column(Integer, ForeignKey('device.id'))
    operating_system_id = Column(Integer, ForeignKey('operating_system.id'))
    browser_id = Column(Integer, ForeignKey('browser.id'))
    project_id = Column(Integer, ForeignKey('project.id'))

    device = relationship('Device')
    operating_system = relationship('OperatingSystem')
    browser = relationship('Browser')
    project = relationship('Project', back_populates='platforms')

    __tablename__ = 'platform'
