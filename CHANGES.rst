1.0.3
=====

User-Facing Changes
-------------------

gemini_metadata_utils
^^^^^^^^^^^^^

- Support for YYYYMMDDTHHMMSS-YYYYMMDDTHHMMSS style datetime ranges for SCALeS [#4]

1.0.2
=====

Other
-----

file_parser.py
^^^^^^^^^^^^^^

- Fix for bad telescope values from IGRINS [#2]
- Properly detect IGRINS files and use the correct parser (IGRINS parser can handle uncorrected IGRINS files) [#3]

gemini_metadata_utils.py
^^^^^^^^^^^^^^^^^^^^^^^^

- Support for new-style non-site-specific program IDs [#1]

header.py
^^^^^^^^^

- removed some debug output


1.0.0
=====

User-Facing Changes
-------------------

gemini_obs_db
^^^^^^^^^^^^^

- Initial version now decoupled from the FitsStorage codebase

Other
-----

file_parser.py
^^^^^^^^^^^^^^

- Converting non-string values in program IDs

