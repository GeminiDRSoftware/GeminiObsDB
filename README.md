# GeminiObsDB

This project provides a set of DB-backed classes to parse Gemini FITS
file metadata into various tables.  This is used by the GeminiCalMgr
to track and match calibration files.

## DRAGONS Dependencies

Unfortunately, this project still has some dependency on `DRAGONS`, which in turn 
depends on `GeminiObsDB`.  The `DRAGONS` dependency stems from the use of 
`astrodata` to read the FITS files.  This is done when building `Header` objects
for the SQLite database for the `DRAGONS` calibration management.  The same logic
is used for creating `Header` records in the FitsStore.

Two possible long-term solutions would be to break out the `astrodata` from
`DRAGONS` as a separate library, or integrate this `GeminiObsDB` project directly
into the DRAGONS codebase.
