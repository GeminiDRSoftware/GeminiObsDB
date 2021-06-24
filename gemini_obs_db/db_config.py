from os.path import join as opjoin

using_apache = False
use_as_archive = False
z_staging_area = ''
storage_root = '/tmp'
fits_dbname = 'fitsdata.fdb'
db_path = opjoin(storage_root, fits_dbname)
fits_database = 'sqlite:///' + db_path
fits_database_pool_size = 30
fits_database_max_overflow = 10

try:
    from fits_storage import fits_storage_config
    using_apache = True
    use_as_archive = fits_storage_config.use_as_archive
    storage_root = fits_storage_config.storage_root
    z_staging_area = fits_storage_config.z_staging_area
    fits_database = fits_storage_config.fits_database
    fits_database_pool_size = fits_storage_config.fits_database_pool_size
    fits_database_max_overflow = fits_storage_config.fits_database_max_overflow
except:
    # ok, not running in FITS Server context
    pass
