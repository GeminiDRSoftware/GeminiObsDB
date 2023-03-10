import astrodata
from gemini_obs_db.orm.diskfile import DiskFile
from gemini_obs_db.orm.file import File
from gemini_obs_db.orm.header import Header
from gemini_obs_db.orm.nifs import Nifs
from tests.file_helper import ensure_file
import gemini_obs_db.db_config as dbc


def test_nifs(monkeypatch):
    monkeypatch.setattr(dbc, "storage_root", "/tmp")

    data_file = 'N20150505S0119.fits'

    ensure_file(data_file, '/tmp')
    ad = astrodata.open('/tmp/%s' % data_file)

    f = File(data_file)
    df = DiskFile(f, data_file, "")
    df.ad_object = ad
    h = Header(df)
    nifs = Nifs(h, ad)

    assert(nifs.filter_name == 'HK_G0603')
    assert(nifs.focal_plane_mask == '3.0_Mask_G5610')
    assert(nifs.disperser == 'K_G5605')
    assert(nifs.read_mode == 'Medium Object')
