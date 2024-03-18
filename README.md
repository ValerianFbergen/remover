# remover

usage: remover.py [-h] [-mac] [-ds] [-mso] [-tmp] [-w TEXT] [-r] [-s] [-q] filepath [filepath ...]

Recursively search and optionally delete files using built-in or user-specified wildcards. Useful for removing hidden
temp files files placed by Mac OS (._* and .DS_STORE) and MS Office (~$*)

positional arguments:
  filepath              Specify one or more filepaths for cleanup

options:
  -h, --help            show this help message and exit
  -mac                  Cleanup ._* files
  -ds                   Cleanup .DS_STORE
  -mso                  Cleanup ~$*
  -tmp                  Cleanup *.tmp
  -w TEXT, -wildcard TEXT
                        Input custom wildcard
  -r, -remove           Remove found files. Disabled by default.
  -s, -stat             Show statistics instead of filenames.
  -q, -quiet            Quiet mode - suppress output

at least one of -w, -mac, -ds, -mso, -tmp arguments/flags must be specified

# FAQ

- Help can't delete ~$WRL1969.tmp!

MS Office temp files have "system" attribute, you need to call remover.py from cmd.exe run as admin.

- Can i accidentaly rm -rf / myself?

Yes. Please don't do that.
(There are 2 failsafes, but if you are smart enough you can bypass them)
