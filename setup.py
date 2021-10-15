#!/usr/bin/env python

from setuptools import setup
from gemini_obs_db import __version__

setup(
    name='GeminiObsDB',
    version=__version__,
    # The following is need only if publishing this under PyPI or similar
    #description = '...',
    #author = 'Paul Hirst',
    #author_email = 'phirst@gemini.edu',
    license = 'License :: OSI Approved :: BSD License',
    packages = ['gemini_obs_db', 'gemini_obs_db.db', 'gemini_obs_db.orm', 'gemini_obs_db.utils'],
    install_requires = ['sqlalchemy >= 0.9.9', ]  # , 'pyfits', 'numpy']
)
