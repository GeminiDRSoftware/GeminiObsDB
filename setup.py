#!/usr/bin/env python

from setuptools import setup

setup(
    name='FitsStorageDB',
    version='1.0.0',
    # The following is need only if publishing this under PyPI or similar
    #description = '...',
    #author = 'Paul Hirst',
    #author_email = 'phirst@gemini.edu',
    license = 'License :: OSI Approved :: BSD License',
    packages = ['utils',
                'gemini_obs_db'],
    # package_dir = {'gemini_calmgr': 'src'},
    install_requires = ['sqlalchemy >= 0.9.9', ]  # , 'pyfits', 'numpy']
)
