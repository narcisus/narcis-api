from . import Base
from .named_model import NamedModel

class Device(Base, NamedModel):
    __tablename__ = 'device'
