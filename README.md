# FitsStorageDB

This project is for the database ORM mappings for the common FitsStore and
calibration related observation metadata.  This used to  live in the 
`FitsStorage` project, but is being broken out as a dependency for 
`DRAGONS` and with an eye towards eventually being a public project.

## Installation

The `FitsStorage` installation expects `FitsStorageDB` to be checked out as that
folder name alongside the `FitsStorage` folder.  It will then copy the files from
 there to the target host when installing the FitsStore.

In future, this will be replaced by a github checkout of a specific tag/etc and
eventually installing from a python package repo.

## DRAGONS Dependencies

Unfortunately, this project still has some dependency on `DRAGONS`, which in turn 
depends on `FitsStorageDB`.  The `DRAGONS` dependency stems from the use of 
`astrodata` to read the FITS files.  This is done when building `Header` objects
for the SQLite database for the `DRAGONS` calibration management.  The same logic
is used for creating `Header` records in the FitsStore.

Two possible long-term solutions would be to break out the `astrodata` from
`DRAGONS` as a separate library, or integrate this `FitsStorageDB` project directly
into the DRAGONS codebase.