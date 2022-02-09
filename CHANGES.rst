1.0.8
=====

file_parser
^^^^^^^^^^^

- WCS first, then fallback to repair WCS, then fallback to ra() or dec()
- smarter about unexpected text format RA
- error reporting for really bad RA/DEC values

1.0.6
=====

gemini_metadata_utils.py
^^^^^^^^^^^^^^^^^^^^^^^^

- fix parsing of observation number from new regex

1.0.5
=====

gemini_obs_db
^^^^^^^^^^^^^

- added pre-ping for Postgres connections so we don't use an expired connection

1.0.4
=====

gemini_metadata_utils.py
^^^^^^^^^^^^^^^^^^^^^^^^

- fix for parsing of datalabels with updated regex
- fix for checking for a datetime string when not handling a range

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

