# Bulk-File-Renaming
### Background
There are a lot of different use cases for renaming a bulk of files,
from organizing your Machine Learning datasets, simply locate and move specific types of files, etc.

I found many programs/scripts that are doing that, but their code is more difficult as it should be,
most of the time this is caused by feature fatigue.

So this simple script is here to solve it, easy to follow, and change it for your usages.

**Feel free to open an issue for any bug you find or another feature you think might feet.**


#### **HELP menu**
usage: `Bulk-File-Renaming.py [-h] [-d [DST]] [-p PATTERN] [-r [RECURSIVE]] [-n [NEW_NAME]] [-c [HANDLE_COLLISIONS]]
                             src`


positional arguments:
  src

optional arguments:
  * -h, --help  show this help message and exit
  * -d, --dst Destination folder files are going to be move to.
  * -p, --pattern Use pattern to filter the files that will be effected, e.g: "*.py$" -> effects all files with "py" suffix.
  * -r, --recursive Effects all files including those located in sub-directories.
  * -n, --new-name set new name for matching files with an id (e.g xxx-1, xxx-2).
  * -c, --handle-collisions Automatically handle name collision that might occur when moving files without defining "-n" arg
##### **Requirements**

* Python 3.4+