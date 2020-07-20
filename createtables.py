"""
This module provides various utility functions for create_tables.py
in the Fits Storage System.
"""
import sqlalchemy

from ..fits_storage_config import using_apache, using_sqlite
from . import pg_db
from .file import File
from .diskfile import DiskFile
from .diskfilereport import DiskFileReport
from .fulltextheader import FullTextHeader
from .header import Header
from .footprint import Footprint
from .gmos import Gmos
from .niri import Niri
from .gnirs import Gnirs
from .nifs import Nifs
from .f2 import F2
from .gpi import Gpi
from .gsaoi import Gsaoi
from .nici import Nici
from .michelle import Michelle
from .ingestqueue import IngestQueue
from .tapestuff import Tape, TapeWrite, TapeFile, TapeRead
from .notification import Notification
from .photstandard import PhotStandard
from .qastuff import QAreport, QAmetricIQ, QAmetricZP, QAmetricSB, QAmetricPE
from .exportqueue import ExportQueue
from .user import User
from .userprogram import UserProgram
from .usagelog import UsageLog
from .queue_error import QueueError
from .querylog import QueryLog
from .downloadlog import DownloadLog
from .filedownloadlog import FileDownloadLog
from .fileuploadlog import FileUploadLog
from .calcache import CalCache
from .calcachequeue import CalCacheQueue
from .preview import Preview
from .previewqueue import PreviewQueue
from .obslog import Obslog
from .miscfile import MiscFile
from .glacier import Glacier
from .obslog_comment import ObslogComment
from .program import Program
from .publication import Publication
from .programpublication import ProgramPublication
# from .bibliography import BibliographyReference, BibliographyAuthor, Bibliography
from .target import init_target_tables


def create_tables(session):
    """
    Creates the database tables and grants the apache user
    SELECT on the appropriate ones

    Parameters
    ----------
    session : sqlalchemy.orm.session.Session
        The SQL Alchemy session to create the tables in
    """
    # Create the tables
    File.metadata.create_all(bind=pg_db)
    DiskFile.metadata.create_all(bind=pg_db)
    DiskFileReport.metadata.create_all(bind=pg_db)
    FullTextHeader.metadata.create_all(bind=pg_db)
    Header.metadata.create_all(bind=pg_db)
    Footprint.metadata.create_all(bind=pg_db)
    Gmos.metadata.create_all(bind=pg_db)
    Niri.metadata.create_all(bind=pg_db)
    Nifs.metadata.create_all(bind=pg_db)
    Gnirs.metadata.create_all(bind=pg_db)
    F2.metadata.create_all(bind=pg_db)
    Gpi.metadata.create_all(bind=pg_db)
    Gsaoi.metadata.create_all(bind=pg_db)
    IngestQueue.metadata.create_all(bind=pg_db)
    Michelle.metadata.create_all(bind=pg_db)
    Nici.metadata.create_all(bind=pg_db)
    Tape.metadata.create_all(bind=pg_db)
    TapeWrite.metadata.create_all(bind=pg_db)
    TapeFile.metadata.create_all(bind=pg_db)
    TapeRead.metadata.create_all(bind=pg_db)
    Notification.metadata.create_all(bind=pg_db)
    PhotStandard.metadata.create_all(bind=pg_db)
    QAreport.metadata.create_all(bind=pg_db)
    QAmetricIQ.metadata.create_all(bind=pg_db)
    QAmetricZP.metadata.create_all(bind=pg_db)
    QAmetricSB.metadata.create_all(bind=pg_db)
    QAmetricPE.metadata.create_all(bind=pg_db)
    ExportQueue.metadata.create_all(bind=pg_db)
    User.metadata.create_all(bind=pg_db)
    UserProgram.metadata.create_all(bind=pg_db)
    UsageLog.metadata.create_all(bind=pg_db)
    QueryLog.metadata.create_all(bind=pg_db)
    DownloadLog.metadata.create_all(bind=pg_db)
    FileDownloadLog.metadata.create_all(bind=pg_db)
    FileUploadLog.metadata.create_all(bind=pg_db)
    CalCache.metadata.create_all(bind=pg_db)
    CalCacheQueue.metadata.create_all(bind=pg_db)
    Preview.metadata.create_all(bind=pg_db)
    PreviewQueue.metadata.create_all(bind=pg_db)
    Obslog.metadata.create_all(bind=pg_db)
    MiscFile.metadata.create_all(bind=pg_db)
    Glacier.metadata.create_all(bind=pg_db)
    QueueError.metadata.create_all(bind=pg_db)
    ObslogComment.metadata.create_all(bind=pg_db)
    Program.metadata.create_all(bind=pg_db)
    Publication.metadata.create_all(bind=pg_db)
    ProgramPublication.metadata.create_all(bind=pg_db)

    init_target_tables(session, pg_db)

    # Add the geometry types separately. this is postgres specific and referencing these column in local mode isn't going to work
    # Ignore any errors, commonly from column already exists...
    if not using_sqlite:
        try:
            pg_db.execute("ALTER TABLE footprint ADD COLUMN area polygon; COMMIT;")
            pg_db.execute("ALTER TABLE photstandard ADD COLUMN coords point; COMMIT;")
        except sqlalchemy.exc.ProgrammingError:
            pass

    if using_apache and not using_sqlite:
        # Now grant the apache user select on them for the www queries
        pg_db.execute("GRANT SELECT ON file, diskfile, diskfilereport, header, fulltextheader, gmos, niri, michelle, gnirs, gpi, nifs, f2, gsaoi, nici, tape, tape_id_seq, tapewrite, taperead, tapefile, notification, photstandard, photstandardobs, footprint, qareport, qametriciq, qametriczp, qametricsb, qametricpe, ingestqueue, exportqueue, archiveuser, userprogram, usagelog, querylog, downloadlog, filedownloadlog, fileuploadlog, calcache, preview, obslog, miscfile, ingestqueue, exportqueue, previewqueue, calcachequeue, queue_error, obslog_comment, program, publication, programpublication TO fitsdata;COMMIT;")
        pg_db.execute("GRANT INSERT,UPDATE ON tape, notification, qareport, qametriciq, qametriczp, qametricsb, qametricpe, archiveuser, userprogram, usagelog, querylog, downloadlog, filedownloadlog, fileuploadlog, miscfile, ingestqueue, obslog_comment, program, publication, programpublication TO fitsdata;COMMIT;")
        pg_db.execute("GRANT UPDATE ON tape_id_seq, notification_id_seq, qareport_id_seq, qametriciq_id_seq, qametriczp_id_seq, qametricsb_id_seq, qametricpe_id_seq, archiveuser_id_seq, userprogram_id_seq, usagelog_id_seq, querylog_id_seq, downloadlog_id_seq, filedownloadlog_id_seq, fileuploadlog_id_seq, ingestqueue_id_seq, obslog_comment_id_seq, program_id_seq, publication_id_seq, programpublication_id_seq TO fitsdata;COMMIT;")
        pg_db.execute("GRANT DELETE ON notification, ingestqueue TO fitsdata;COMMIT;")

    # Make a dummy publication
    # pub = Publication(
    #     bibcode='1993ApJ...415...50C',
    #     author='Cavaliere, A.; Colafrancesco, S.; Menci, N.',
    #     journal='Astrophysical Journal, Part 1, vol.415, no. 1, p. 50-57.',
    #     year='1993',
    #     title='Distant clusters of galaxies detected by X-rays'
    # )
    # session.add(pub)


def drop_tables(session):
    """
    Drops all the database tables. Very unsubtle. Use with caution

    Parameters
    ----------
    session : :class:`sqlalchemy.orm.session.Session`
        The current SQL Alchemy session (future proofing, for now it all routes through `pg_db`)
    """
    # TODO is this even used anywhere?  I think we should kill it here and in the create_tables script
    File.metadata.drop_all(bind=pg_db)
