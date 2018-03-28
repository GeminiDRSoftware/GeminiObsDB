#
#                                                                    FitsStorage
#
#                                                             Gemini Observatory
#                                               fits_store.orm.obslog_comment.py
# ------------------------------------------------------------------------------
__version__      = '0.99 beta'
# ------------------------------------------------------------------------------
from sqlalchemy import Column
from sqlalchemy import Integer, Text, Boolean

from . import Base

# ------------------------------------------------------------------------------
class ObslogComment(Base):
    """
    This is the ORM class for storing observation log comments retrieved from the
    ODB. Note, these are not related (in the FitsStorage world) to the obslog files
    we also store.

    """
    __tablename__ = 'obslog_comment'

    id = Column(Integer, primary_key=True)
    program_id = Column(Text, index=True)
    data_label = Column(Text, index=True)
    comment = Column(Text)

    def __init__(self, program_id, data_label, comment):
        self.program_id = program_id
        self.data_label = data_label
        self.comment = comment

