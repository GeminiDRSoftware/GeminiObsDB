from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text
from sqlalchemy.orm import relation

from . import Base
from .header import Header

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
    read_mode = Column(Text, index=True)
    coadds = Column(Integer, index=True)
    focal_plane_mask = Column(Text)

    def __init__(self, header, ad):
        self.header = header

        # Populate from an astrodata object
        self.populate(ad)

    def populate(self, ad):
        self.disperser = ad.disperser().for_db()
        self.filter_name = ad.filter_name().for_db()
        self.read_mode = ad.read_mode().for_db()
        self.coadds = ad.coadds().for_db()
        self.focal_plane_mask = ad.focal_plane_mask().for_db()
