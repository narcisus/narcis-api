from . import Base
from .named_model import NamedModel

class Browser(Base, NamedModel):
    __tablename__ = 'browser'
