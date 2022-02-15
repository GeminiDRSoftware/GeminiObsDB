import pytest

from gemini_obs_db.utils.gemini_metadata_utils import ratodeg, ratodeg_old, dectodeg, dectodeg_old


def test_ratodeg():
    ra_str = '03:48:30.113'
    ra = ratodeg(ra_str)
    ra_old = ratodeg_old(ra_str)
    assert pytest.approx(ra, 57.12547083333333)
    assert pytest.approx(ra_old, 57.12547083333333)


def test_dectodeg():
    dec_str = '+24:20:43.00'
    dec = dectodeg(dec_str)
    dec_old = dectodeg_old(dec_str)
    assert(pytest.approx(dec, 24.345277777777778))
    assert(pytest.approx(dec_old, 24.345277777777778))


if __name__ == "__main__":
    pytest.main()
