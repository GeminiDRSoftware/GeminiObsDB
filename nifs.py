from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text, Enum
from sqlalchemy.orm import relation

from . import Base
from .header import Header

NIFS_READ_MODE_ENUM = Enum('Faint Object', 'Medium Object', 'Bright Object', 'Invalid', name='nifs_read_mode')

class Nifs(Base):
    """
    This is the ORM object for the NIFS details
    """
    __tablename__ = 'nifs'

    id = Column(Integer, primary_key=True)
    header_id = Column(Integer, ForeignKey('header.id'), nullable=False, index=True)
    header = relation(Header, order_by=id)
    disperser = Column(Text, index=True)
    filter_name = Column(Text, index=True)
    read_mode = Column(NIFS_READ_MODE_ENUM, index=True)
    focal_plane_mask = Column(Text)

    def __init__(self, header, ad):
        self.header = header

        # Populate from an astrodata object
        self.populate(ad)

    def populate(self, ad):
        self.disperser = ad.disperser().for_db()
        self.filter_name = ad.filter_name().for_db()
        self.read_mode = ad.read_mode().for_db()
        self.focal_plane_mask = ad.focal_plane_mask().for_db()
