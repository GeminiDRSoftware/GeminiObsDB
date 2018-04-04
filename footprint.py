from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text

from . import Base

class Footprint(Base):
    """
    This is the ORM object for the Footprint table. Each row is a footprint
    derived from a WCS. There can be several footprints (typically one per science
    extension) per header object.

    """
    __tablename__ = 'footprint'

    id = Column(Integer, primary_key=True)
    header_id = Column(Integer, ForeignKey('header.id'), nullable=False, index=True)
    extension = Column(Text)
    # An area column of type polygon gets added using raw sql in CreateTables.py

    def __init__(self, header):
        self.header_id = header.id

    def populate(self, extension):
        self.extension = extension


