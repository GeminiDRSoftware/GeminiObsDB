"""
This module contains the ORM classes for the tables in the fits storage
database.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.sqltypes import String, Date, DateTime, NullType
from datetime import datetime, date
from contextlib import contextmanager

__version__ = '1.0.0.dev'


__all__ = ["__version__", "fits_database", "fits_database_pool_size", "fits_database_max_overflow",
           "pg_db", "sessionfactory", "session_scope"]

from .db_config import fits_database, fits_database_pool_size, fits_database_max_overflow


args = {'echo': False}
if fits_database.startswith('postgresql://'):
    args = {'pool_size': fits_database_pool_size, 'max_overflow': fits_database_max_overflow,
            'echo': False}
pg_db = create_engine(fits_database, **args)
sessionfactory = sessionmaker(pg_db)


Base = declarative_base()


@contextmanager
def session_scope(no_rollback=False):
    """
    Provide a transactional scope around a series of operations

    Parameters
    ----------
    no_rollback: bool
        True if we want to always commit, default is False

    Returns
    -------
    sqlalchemy.orm.session.Session
        Session with automatic commit/rollback handling on leaving the context
    """
    session = sessionfactory()
    try:
        yield session
        session.commit()
    except:
        if not no_rollback:
            session.rollback()
        else:
            session.commit()
        raise
    finally:
        session.close()


class StringLiteral(String):
    """
    Literal used for a custom SQLAlchemy dialect for debugging.

    To debug SQLAlchemy queries, it is useful to have this custom
    dialect that will convert the query, not into SQL, but into
    a readable text string.  This class helps with that.
    """
    def literal_processor(self, dialect):
        super_processor = super(StringLiteral, self).literal_processor(dialect)

        def process(value):
            if isinstance(value, (date, datetime)) or value is None:
                return str(value)
            return super_processor(value)
        return process


class LiteralDialect(postgresql.dialect):
    """
    Literal used for a custom SQLAlchemy dialect for debugging.

    To debug SQLAlchemy queries, it is useful to have this custom
    dialect that will convert the query, not into SQL, but into
    a readable text string.  This class is the top level dialect
    description for that purpose.
    """
    colspecs = {
        Date: StringLiteral,
        DateTime: StringLiteral,
        NullType: StringLiteral
    }


def compiled_statement(stmt):
    """
    Returns a compiled query using the PostgreSQL dialect. Useful for
    example to print the real query, when debugging

    Parameters
    ----------
    stmt : :class:`~sqlalchemy.orm.statement.Statement

    Returns
    -------
    str
        String representation of the query
    """
    return stmt.compile(dialect=LiteralDialect(), compile_kwargs={'literal_binds': True})

