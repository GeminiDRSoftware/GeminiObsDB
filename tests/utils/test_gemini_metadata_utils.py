import pytest

from gemini_obs_db.utils.gemini_metadata_utils import ratodeg, ratodeg_old, dectodeg, dectodeg_old, GeminiProgram, \
    GeminiDataLabel


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


def test_program_ids():
    gp = GeminiProgram('G-2020A-Q-123')
    assert gp.is_q
    gp = GeminiProgram('G-2020A-C-123')
    assert gp.is_c

    gp = GeminiProgram('G-2020A-ENG-123')
    assert gp.is_eng
    gp = GeminiProgram('G-2020A-CAL-123')
    assert gp.is_cal
    # this looks not true, cal program sidesteps the subcategories (at least per the original logic)
    # gp = GeminiProgram('G-2020V-CAL-123')
    # assert gp.is_sv
    # gp = GeminiProgram('G-2020F-CAL-123')
    # assert gp.is_ft
    # gp = GeminiProgram('G-2020S-CAL-123')
    # assert gp.is_ds

    gp = GeminiProgram('GN-2020A-SV-123')
    assert gp.is_sv
    gp = GeminiProgram('GN-2020A-FT-123')
    assert gp.is_ft
    gp = GeminiProgram('GN-2020A-DS-123')
    assert gp.is_ds

    gp = GeminiProgram('GN-CAL20200123')
    assert gp.is_cal
    gp = GeminiProgram('GN-ENG20200123')
    assert gp.is_eng

    # test trim of leading 0s for old-style program IDs
    gp = GeminiProgram('GN-2020A-DS-0123')
    assert gp.program_id == 'GN-2020A-DS-123'


def test_url_parsing_helpers():
    dl = GeminiDataLabel("GN-CAL20220502-5-001")
    assert(dl.projectid == "GN-CAL20220502")
    assert(dl.observation_id == "GN-CAL20220502-5")
    assert(dl.obsnum == "5")
    assert(dl.datalabel == "GN-CAL20220502-5-001")
    assert(dl.dlnum == "001")


if __name__ == "__main__":
    pytest.main()
