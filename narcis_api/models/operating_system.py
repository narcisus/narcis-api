from . import Base
from .named_model import NamedModel

class OperatingSystem(Base, NamedModel):
    __tablename__ = 'operating_system'
