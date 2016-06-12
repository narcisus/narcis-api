from sqlalchemy import Column, String
from slugify import slugify

from .model import Model

class NamedModel(Model):
    name = Column(String)
    name_slug = Column(String)
