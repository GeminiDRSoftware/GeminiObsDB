from sqlalchemy import Column
from sqlalchemy import Integer, Text, Boolean, DateTime, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from sqlalchemy.ext.associationproxy import association_proxy

from io import StringIO

from . import Base

# ------------------------------------------------------------------------------
class Publication(Base):
    """
    This is the ORM class for storing publication details fetched from the
    librarian's database.

    """
    __tablename__ = 'publication'

    id = Column(Integer, primary_key=True)
    bibcode = Column(String(20), index=True)
    author = Column(Text)
    title = Column(Text)
    year = Column(Integer)
    journal = Column(Text)
    telescope = Column(String(5))
    instrument = Column(String(50))
    country = Column(String(20))
    wavelength = Column(String(20))
    mode = Column(String(20))
    gstaff = Column(Boolean)
    gsa = Column(Boolean)
    golden = Column(Boolean)
    too = Column(String(10))
    partner = Column(String(35))
    last_refreshed = Column(DateTime, server_default=func.now(), onupdate=func.now())
    programs = association_proxy('publication_programs', 'program')

    def __init__(self, bibcode):
        self.bibcode = bibcode

    def ads_tagged(self):
        retval = StringIO.StringIO()

        retval.write("%%R %s\n" % (self.bibcode))
        retval.write("%%A %s\n" % (self.author))        
        retval.write("%%J %s\n" % (self.journal))
        retval.write("%%D %s\n" % (self.year))
        retval.write("%%T %s\n" % (self.title))

        out = retval.output()
        retval.close()

        return out
