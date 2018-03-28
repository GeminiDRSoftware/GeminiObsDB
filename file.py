#
#                                                                    FitsStorage
#
#                                                             Gemini Observatory
#                                                         fits_store.orm.file.py
# ------------------------------------------------------------------------------
__version__      = '0.99 beta'
# ------------------------------------------------------------------------------
from sqlalchemy import Column
from sqlalchemy import Integer, Text
from sqlalchemy.orm import relationship

from . import Base

# ------------------------------------------------------------------------------
class File(Base):
    """
    This is the ORM class for the file table. This is highest level most abstract
    concept of a 'File'. It's essentially just a unique label that other things
    - actual DiskFiles for example can reference. The 'name' column here may not
    be the actual filename - the definitive filename is in the diskfile table,
    when we have a compressed (bzip2) file, we trim off the .bz2 here.

    """
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True, index=True)

    diskfiles = relationship('DiskFile', lazy='dynamic')

    def __init__(self, filename):
        self.name = File.trim_name(filename)

    def __repr__(self):
        return "<File('%s', '%s')>" % (self.id, self.name)

    @staticmethod
    def trim_name(filename):
        """
        Trim any trailing .bz2 off the filename
        """

        if filename.endswith(".bz2"):
            return filename[:-4]

        return filename
