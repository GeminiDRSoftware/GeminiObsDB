from os.path import join


__all__ = [
    "using_apache",
    "use_utc",
    "z_staging_area",
    "storage_root",
    "sqlite_db_path",
    "database_url",
    "postgres_database_pool_size",
    "postgres_database_max_overflow",
]


using_apache = False
use_utc = False
z_staging_area = ''
storage_root = '/tmp'
sqlite_db_path = join(storage_root, 'gemini_obs_db.db')
database_url = 'sqlite:///' + sqlite_db_path

# These two are only used if we are using a Postgres database
# However, we define then anyway so they are available for import
postgres_database_pool_size = 30
postgres_database_max_overflow = 10


# Slightly naughty cyclical dependency on FitsStorage remains here.  This trick will pull in
# the FitsStorage configuration, if it exists.  If we are not running within the FitsStore, the
# import will fail which is fine.  In that case, we just want the settings as above.
# try:
#     from fits_storage import fits_storage_config
#     using_apache = True
#     use_utc = fits_storage_config.use_as_archive
#     storage_root = fits_storage_config.storage_root
#     z_staging_area = fits_storage_config.z_staging_area
#     database_url = fits_storage_config.fits_database
#     postgres_database_pool_size = fits_storage_config.fits_database_pool_size
#     postgres_database_max_overflow = fits_storage_config.fits_database_max_overflow
# except:
#     # ok, not running in FITS Server context
#     pass
