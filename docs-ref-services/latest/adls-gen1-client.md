---
title: Azure Data Lake Storage Gen1 library for Python
description: A python interface to the Azure Data-lake Storage system gen 1
keywords: Azure, Python, SDK, API, DataLake, ADLS
author: akharit
ms.author: akharit
manager: pkasturi
ms.date: 08/26/2019
ms.topic: reference
ms.technology: azure
ms.devlang: python
ms.service: datalake-store
---

# azure-datalake-store

A pure-python interface to the Azure Data Lake Storage gen 1 system, providing
pythonic file-system and file objects, seamless transition between Windows and
POSIX remote paths, high-performance up- and down-loader.

This software is under active development and not yet recommended for general
use.

## Installation

Using `pip`:

```
pip install azure-datalake-store
```

Manually (bleeding edge):

* Download the repo from [https://github.com/Azure/azure-data-lake-store-python](https://github.com/Azure/azure-data-lake-store-python)

* checkout the `dev` branch

* install the requirements (`pip install -r dev_requirements.txt`)

* install in develop mode (`python setup.py develop`)

* optionally: build the documentation (including this page) by running `make html` in the docs directory.

## Auth

Although users can generate and supply their own tokens to the base file-system
class, and there is a password-based function in the `lib` module for
generating tokens, the most convenient way to supply credentials is via
environment parameters. This latter method is the one used by default in
library. The following variables are required:

* azure_tenant_id

* azure_username

* azure_password

* azure_store_name

* azure_url_suffix (optional)

## Pythonic Filesystem

The `AzureDLFileSystem` object is the main API for library usage of this
package. It provides typical file-system operations on the remote azure
store

```
token = lib.auth(tenant_id, username, password)
adl = core.AzureDLFileSystem(store_name, token)
# alternatively, adl = core.AzureDLFileSystem()
# uses environment variables

print(adl.ls())  # list files in the root directory
for item in adl.ls(detail=True):
    print(item)  # same, but with file details as dictionaries
print(adl.walk(''))  # list all files at any directory depth
print('Usage:', adl.du('', deep=True, total=True))  # total bytes usage
adl.mkdir('newdir')  # create directory
adl.touch('newdir/newfile') # create empty file
adl.put('remotefile', '/home/myuser/localfile') # upload a local file
```

In addition, the file-system generates file objects that are compatible with
the python file interface, ensuring compatibility with libraries that work on
python files. The recommended way to use this is with a context manager
(otherwise, be sure to call `close()` on the file object).

```
with adl.open('newfile', 'wb') as f:
    f.write(b'index,a,b\n')
    f.tell()   # now at position 9
    f.flush()  # forces data upstream
    f.write(b'0,1,True')

with adl.open('newfile', 'rb') as f:
    print(f.readlines())

with adl.open('newfile', 'rb') as f:
    df = pd.read_csv(f) # read into pandas.
```

To seamlessly handle remote path representations across all supported platforms,
the main API will take in numerous path types: string, Path/PurePath, and
AzureDLPath. On Windows in particular, you can pass in paths separated by either
forward slashes or backslashes.

```
import pathlib  # only >= Python 3.4
from pathlib2 import pathlib  # only <= Python 3.3

from azure.datalake.store.core import AzureDLPath

# possible remote paths to use on API
p1 = '\\foo\\bar'
p2 = '/foo/bar'
p3 = pathlib.PurePath('\\foo\\bar')
p4 = pathlib.PureWindowsPath('\\foo\\bar')
p5 = pathlib.PurePath('/foo/bar')
p6 = AzureDLPath('\\foo\\bar')
p7 = AzureDLPath('/foo/bar')

# p1, p3, and p6 only work on Windows
for p in [p1, p2, p3, p4, p5, p6, p7]:
  with adl.open(p, 'rb') as f:
      print(f.readlines())
```

## Performant up-/down-loading

Classes `ADLUploader` and `ADLDownloader` will chunk large files and send
many files to/from azure using multiple threads. A whole directory tree can
be transferred, files matching a specific glob-pattern or any particular file.

```
# download the whole directory structure using 5 threads, 16MB chunks
ADLDownloader(adl, '', 'my_temp_dir', 5, 2**24)
```
