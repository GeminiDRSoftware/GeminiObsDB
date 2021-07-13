from contextlib import contextmanager
from datetime import date, datetime

from sqlalchemy import create_engine, String, Date, DateTime
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql.sqltypes import NullType

from gemini_obs_db.db.db_config import fits_database, fits_database_pool_size, fits_database_max_overflow


if fits_database.startswith('postgresql://'):
    args = {'pool_size': fits_database_pool_size, 'max_overflow': fits_database_max_overflow,
            'echo': False}
else:
    args = {'echo': False}
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
    :class:`~sqlalchemy.orm.Session`
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


class _StringLiteral(String):
    """
    Literal used for a custom SQLAlchemy dialect for debugging.

    To debug SQLAlchemy queries, it is useful to have this custom
    dialect that will convert the query, not into SQL, but into
    a readable text string.  This class helps with that.
    """
    def literal_processor(self, dialect):
        super_processor = super(_StringLiteral, self).literal_processor(dialect)

        def process(value):
            if isinstance(value, (date, datetime)) or value is None:
                return str(value)
            return super_processor(value)
        return process


class _LiteralDialect(postgresql.dialect):
    """
    Literal used for a custom SQLAlchemy dialect for debugging.

    To debug SQLAlchemy queries, it is useful to have this custom
    dialect that will convert the query, not into SQL, but into
    a readable text string.  This class is the top level dialect
    description for that purpose.
    """
    colspecs = {
        Date: _StringLiteral,
        DateTime: _StringLiteral,
        NullType: _StringLiteral
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
    return stmt.compile(dialect=_LiteralDialect(), compile_kwargs={'literal_binds': True})