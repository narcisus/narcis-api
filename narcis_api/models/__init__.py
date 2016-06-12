from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .project import Project
from .user import User
from .operating_system import OperatingSystem
from .browser import Browser
from .device import Device
from .platform import Platform
from .page import Page
from .branch import Branch
from .build import Build
from .screenshot import Screenshot
