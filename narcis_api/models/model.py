from sqlalchemy import Column, Integer, Boolean
from slugify import slugify

class Model(object):
    id = Column(Integer, primary_key=True)
    deleted = Column(Boolean)
