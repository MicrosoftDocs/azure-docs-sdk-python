# azure-datalake-store

A pure-python interface to the Azure Data-lake Storage system, providing
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
# API

#### class azure.datalake.store.core.AzureDLFileSystem(token=None, per_call_timeout_seconds=60, \*\*kwargs)
Access Azure DataLake Store as if it were a file-system


* **Parameters**

    **store_name: str (“”)**

        Store name to connect to.

    **token: credentials object**

        When setting up a new connection, this contains the authorization
        credentials (see lib.auth()).

    **url_suffix: str (None)**

        Domain to send REST requests to. The end-point URL is constructed
        using this and the store_name. If None, use default.

    **api_version: str (2018-09-01)**

        The API version to target with requests. Changing this value will
        change the behavior of the requests, and can cause unexpected behavior or
        breaking changes. Changes to this value should be undergone with caution.

    **per_call_timeout_seconds: float(60)**

        This is the timeout for each requests library call.

    **kwargs: optional key/values**

        See `lib.auth()`; full list: tenant_id, username, password, client_id,
        client_secret, resource


### Methods





















<!-- !! processed by numpydoc !! -->

#### access(self, path, invalidate_cache=True)
Does such a file/directory exist?


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **invalidate_cache: bool**

        Whether to invalidate cache



* **Returns**

    True or false depending on whether the path exists.


<!-- !! processed by numpydoc !! -->

#### cat(self, path)
Return contents of file


* **Parameters**

    **path: str or AzureDLPath**

        Path to query



* **Returns**

    Contents of file


<!-- !! processed by numpydoc !! -->

#### chmod(self, path, mod)
Change access mode of path

Note this is not recursive.


* **Parameters**

    **path: str**

        Location to change

    **mod: str**

        Octal representation of access, e.g., “0777” for public read/write.
        See [docs]([http://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-hdfs/WebHDFS.html#Permission](http://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-hdfs/WebHDFS.html#Permission))


<!-- !! processed by numpydoc !! -->

#### chown(self, path, owner=None, group=None)
Change owner and/or owning group

Note this is not recursive.


* **Parameters**

    **path: str**

        Location to change

    **owner: str**

        UUID of owning entity

    **group: str**

        UUID of group


<!-- !! processed by numpydoc !! -->

#### concat(self, outfile, filelist, delete_source=False)
Concatenate a list of files into one new file


* **Parameters**

    **outfile: path**

        The file which will be concatenated to. If it already exists,
        the extra pieces will be appended.

    **filelist: list of paths**

        Existing adl files to concatenate, in order

    **delete_source: bool (False)**

        If True, assume that the paths to concatenate exist alone in a
        directory, and delete that whole directory when done.



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### connect(self)
Establish connection object.

<!-- !! processed by numpydoc !! -->

#### cp(self, path1, path2)
Not implemented. Copy file between locations on ADL

<!-- !! processed by numpydoc !! -->

#### classmethod current()
Return the most recently created AzureDLFileSystem

<!-- !! processed by numpydoc !! -->

#### df(self, path)
Resource summary of path


* **Parameters**

    **path: str**

        Path to query


<!-- !! processed by numpydoc !! -->

#### du(self, path, total=False, deep=False, invalidate_cache=True)
Bytes in keys at path


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **total: bool**

        Return the sum on list

    **deep: bool**

        Recursively enumerate or just use files under current dir

    **invalidate_cache: bool**

        Whether to invalidate cache



* **Returns**

    List of dict of name:size pairs or total size.


<!-- !! processed by numpydoc !! -->

#### exists(self, path, invalidate_cache=True)
Does such a file/directory exist?


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **invalidate_cache: bool**

        Whether to invalidate cache



* **Returns**

    True or false depending on whether the path exists.


<!-- !! processed by numpydoc !! -->

#### get(self, path, filename)
Stream data from file at path to local filename


* **Parameters**

    **path: str or AzureDLPath**

        ADL Path to read

    **filename: str or Path**

        Local file path to write to



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### get_acl_status(self, path)
Gets Access Control List (ACL) entries for the specified file or directory.


* **Parameters**

    **path: str**

        Location to get the ACL.


<!-- !! processed by numpydoc !! -->

#### glob(self, path, details=False, invalidate_cache=True)
Find files (not directories) by glob-matching.


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **details: bool**

        Whether to include file details

    **invalidate_cache: bool**

        Whether to invalidate cache



* **Returns**

    List of files


<!-- !! processed by numpydoc !! -->

#### head(self, path, size=1024)
Return first bytes of file


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **size: int**

        How many bytes to return



* **Returns**

    First(size) bytes of file


<!-- !! processed by numpydoc !! -->

#### info(self, path, invalidate_cache=True, expected_error_code=None)
File information for path


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **invalidate_cache: bool**

        Whether to invalidate cache or not

    **expected_error_code:  int**

        Optionally indicates a specific, expected error code, if any.



* **Returns**

    File information


<!-- !! processed by numpydoc !! -->

#### invalidate_cache(self, path=None)
Remove entry from object file-cache


* **Parameters**

    **path: str or AzureDLPath**

        Remove the path from object file-cache



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### listdir(self, path='', detail=False, invalidate_cache=True)
List all elements under directory specified with path


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **detail: bool**

        Detailed info or not.

    **invalidate_cache: bool**

        Whether to invalidate cache or not



* **Returns**

    List of elements under directory specified with path


<!-- !! processed by numpydoc !! -->

#### ls(self, path='', detail=False, invalidate_cache=True)
List all elements under directory specified with path


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **detail: bool**

        Detailed info or not.

    **invalidate_cache: bool**

        Whether to invalidate cache or not



* **Returns**

    List of elements under directory specified with path


<!-- !! processed by numpydoc !! -->

#### merge(self, outfile, filelist, delete_source=False)
Concatenate a list of files into one new file


* **Parameters**

    **outfile: path**

        The file which will be concatenated to. If it already exists,
        the extra pieces will be appended.

    **filelist: list of paths**

        Existing adl files to concatenate, in order

    **delete_source: bool (False)**

        If True, assume that the paths to concatenate exist alone in a
        directory, and delete that whole directory when done.



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### mkdir(self, path)
Make new directory


* **Parameters**

    **path: str or AzureDLPath**

        Path to create directory



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### modify_acl_entries(self, path, acl_spec, recursive=False, number_of_sub_process=None)
Modify existing Access Control List (ACL) entries on a file or folder.
If the entry does not exist it is added, otherwise it is updated based on the spec passed in.
No entries are removed by this process (unlike set_acl).

Note: this is by default not recursive, and applies only to the file or folder specified.


* **Parameters**

    **path: str**

        Location to set the ACL entries on.

    **acl_spec: str**

        The ACL specification to use in modifying the ACL at the path in the format
        ‘[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,…’

    **recursive: bool**

        Specifies whether to modify ACLs recursively or not


<!-- !! processed by numpydoc !! -->

#### mv(self, path1, path2)
Move file between locations on ADL


* **Parameters**

    **path1:**

        Source Path

    **path2:**

        Destination path



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### open(self, path, mode='rb', blocksize=33554432, delimiter=None)
Open a file for reading or writing


* **Parameters**

    **path: string**

        Path of file on ADL

    **mode: string**

        One of ‘rb’, ‘ab’ or ‘wb’

    **blocksize: int**

        Size of data-node blocks if reading

    **delimiter: byte(s) or None**

        For writing delimiter-ended blocks


<!-- !! processed by numpydoc !! -->

#### put(self, filename, path, delimiter=None)
Stream data from local filename to file at path


* **Parameters**

    **filename: str or Path**

        Local file path to read from

    **path: str or AzureDLPath**

        ADL Path to write to

    **delimiter:**

        Optional delimeter for delimiter-ended blocks



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### read_block(self, fn, offset, length, delimiter=None)
Read a block of bytes from an ADL file

Starting at `offset` of the file, read `length` bytes.  If
`delimiter` is set then we ensure that the read starts and stops at
delimiter boundaries that follow the locations `offset` and `offset
+ length`.  If `offset` is zero then we start at zero.  The
bytestring returned WILL include the end delimiter string.

If offset+length is beyond the eof, reads to eof.


* **Parameters**

    **fn: string**

        Path to filename on ADL

    **offset: int**

        Byte offset to start read

    **length: int**

        Number of bytes to read

    **delimiter: bytes (optional)**

        Ensure reading starts and stops at delimiter bytestring


### Examples

```python
>>> adl.read_block('data/file.csv', 0, 13)  # doctest: +SKIP
b'Alice, 100\nBo'
>>> adl.read_block('data/file.csv', 0, 13, delimiter=b'\n')  # doctest: +SKIP
b'Alice, 100\nBob, 200\n'
```

Use `length=None` to read to the end of the file.
>>> adl.read_block(‘data/file.csv’, 0, None, delimiter=b’n’)  # doctest: +SKIP
b’Alice, 100nBob, 200nCharlie, 300’

<!-- !! processed by numpydoc !! -->

#### remove(self, path, recursive=False)
Remove a file or directory


* **Parameters**

    **path: str or AzureDLPath**

        The location to remove.

    **recursive: bool (True)**

        Whether to remove also all entries below, i.e., which are returned
        by walk().



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### remove_acl(self, path)
Remove the entire, non default, ACL from the file or folder, including unnamed entries.
Default entries cannot be removed this way, please use remove_default_acl for that.

Note: this is not recursive, and applies only to the file or folder specified.


* **Parameters**

    **path: str**

        Location to remove the ACL.


<!-- !! processed by numpydoc !! -->

#### remove_acl_entries(self, path, acl_spec, recursive=False, number_of_sub_process=None)
Remove existing, named, Access Control List (ACL) entries on a file or folder.
If the entry does not exist already it is ignored.
Default entries cannot be removed this way, please use remove_default_acl for that.
Unnamed entries cannot be removed in this way, please use remove_acl for that.

Note: this is by default not recursive, and applies only to the file or folder specified.


* **Parameters**

    **path: str**

        Location to remove the ACL entries.

    **acl_spec: str**

        The ACL specification to remove from the ACL at the path in the format (note that the permission portion is missing)
        ‘[default:]user|group|other:[entity id or UPN],[default:]user|group|other:[entity id or UPN],…’

    **recursive: bool**

        Specifies whether to remove ACLs recursively or not


<!-- !! processed by numpydoc !! -->

#### remove_default_acl(self, path)
Remove the entire default ACL from the folder.
Default entries do not exist on files, if a file
is specified, this operation does nothing.

Note: this is not recursive, and applies only to the folder specified.


* **Parameters**

    **path: str**

        Location to set the ACL on.


<!-- !! processed by numpydoc !! -->

#### rename(self, path1, path2)
Move file between locations on ADL


* **Parameters**

    **path1:**

        Source Path

    **path2:**

        Destination path



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### rm(self, path, recursive=False)
Remove a file or directory


* **Parameters**

    **path: str or AzureDLPath**

        The location to remove.

    **recursive: bool (True)**

        Whether to remove also all entries below, i.e., which are returned
        by walk().



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### rmdir(self, path)
Remove empty directory


* **Parameters**

    **path: str or AzureDLPath**

        Directory  path to remove



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### set_acl(self, path, acl_spec, recursive=False, number_of_sub_process=None)
Set the Access Control List (ACL) for a file or folder.

Note: this is by default not recursive, and applies only to the file or folder specified.


* **Parameters**

    **path: str**

        Location to set the ACL on.

    **acl_spec: str**

        The ACL specification to set on the path in the format
        ‘[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,…’

    **recursive: bool**

        Specifies whether to set ACLs recursively or not


<!-- !! processed by numpydoc !! -->

#### set_expiry(self, path, expiry_option, expire_time=None)
Set or remove the expiration time on the specified file.
This operation can only be executed against files.

Note: Folders are not supported.


* **Parameters**

    **path: str**

        File path to set or remove expiration time

    **expire_time: int**

        The time that the file will expire, corresponding to the expiry_option that was set

    **expiry_option: str**

        Indicates the type of expiration to use for the file:

            1. NeverExpire: ExpireTime is ignored.

            1. RelativeToNow: ExpireTime is an integer in milliseconds representing the expiration date relative to when file expiration is updated.

            1. RelativeToCreationDate: ExpireTime is an integer in milliseconds representing the expiration date relative to file creation.

            1. Absolute: ExpireTime is an integer in milliseconds, as a Unix timestamp relative to 1/1/1970 00:00:00.


<!-- !! processed by numpydoc !! -->

#### stat(self, path, invalidate_cache=True, expected_error_code=None)
File information for path


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **invalidate_cache: bool**

        Whether to invalidate cache or not

    **expected_error_code:  int**

        Optionally indicates a specific, expected error code, if any.



* **Returns**

    File information


<!-- !! processed by numpydoc !! -->

#### tail(self, path, size=1024)
Return last bytes of file


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **size: int**

        How many bytes to return



* **Returns**

    Last(size) bytes of file


<!-- !! processed by numpydoc !! -->

#### touch(self, path)
Create empty file


* **Parameters**

    **path: str or AzureDLPath**

        Path of file to create



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### unlink(self, path, recursive=False)
Remove a file or directory


* **Parameters**

    **path: str or AzureDLPath**

        The location to remove.

    **recursive: bool (True)**

        Whether to remove also all entries below, i.e., which are returned
        by walk().



* **Returns**

    None


<!-- !! processed by numpydoc !! -->

#### walk(self, path='', details=False, invalidate_cache=True)
Get all files below given path


* **Parameters**

    **path: str or AzureDLPath**

        Path to query

    **details: bool**

        Whether to include file details

    **invalidate_cache: bool**

        Whether to invalidate cache



* **Returns**

    List of files


<!-- !! processed by numpydoc !! -->

#### class azure.datalake.store.multithread.ADLUploader(adlfs, rpath, lpath, nthreads=None, chunksize=268435456, buffersize=4194304, blocksize=4194304, client=None, run=True, overwrite=False, verbose=False, progress_callback=None, timeout=0)
Upload local file(s) using chunks and threads

Launches multiple threads for efficient uploading, with chunksize
assigned to each. The path can be a single file, a directory
of files or a glob pattern.


* **Parameters**

    **adlfs: ADL filesystem instance**

    **rpath: str**

        remote path to upload to; if multiple files, this is the dircetory
        root to write within

    **lpath: str**

        local path. Can be single file, directory (in which case, upload
        recursively) or glob pattern. Recursive glob patterns using \*\* are
        not supported.

    **nthreads: int [None]**

        Number of threads to use. If None, uses the number of cores.

    **chunksize: int [2\*\*28]**

        Number of bytes for a chunk. Large files are split into chunks. Files
        smaller than this number will always be transferred in a single thread.

    **buffersize: int [2\*\*22]**

        Number of bytes for internal buffer. This block cannot be bigger than
        a chunk and cannot be smaller than a block.

    **blocksize: int [2\*\*22]**

        Number of bytes for a block. Within each chunk, we write a smaller
        block for each API call. This block cannot be bigger than a chunk.

    **client: ADLTransferClient [None]**

        Set an instance of ADLTransferClient when finer-grained control over
        transfer parameters is needed. Ignores nthreads and chunksize
        set by constructor.

    **run: bool [True]**

        Whether to begin executing immediately.

    **overwrite: bool [False]**

        Whether to forcibly overwrite existing files/directories. If False and
        remote path is a directory, will quit regardless if any files would be
        overwritten or not. If True, only matching filenames are actually
        overwritten.

    **progress_callback: callable [None]**

        Callback for progress with signature function(current, total) where
        current is the number of bytes transfered so far, and total is the
        size of the blob, or None if the total size is unknown.

    **timeout: int (0)**

        Default value 0 means infinite timeout. Otherwise time in seconds before the
        process will stop and raise an exception if  transfer is still in progress



* **Attributes**

    **hash**


### Methods



<!-- !! processed by numpydoc !! -->

#### active(self)
Return whether the uploader is active

<!-- !! processed by numpydoc !! -->

#### static clear_saved()
Remove references to all persisted uploads.

<!-- !! processed by numpydoc !! -->

#### static load()
Load list of persisted transfers from disk, for possible resumption.


* **Returns**

    A dictionary of upload instances. The hashes are auto

        generated unique. The state of the chunks completed, errored, etc.,
        can be seen in the status attribute. Instances can be resumed with
        `run()`.


<!-- !! processed by numpydoc !! -->

#### run(self, nthreads=None, monitor=True)
Populate transfer queue and execute downloads


* **Parameters**

    **nthreads: int [None]**

        Override default nthreads, if given

    **monitor: bool [True]**

        To watch and wait (block) until completion.


<!-- !! processed by numpydoc !! -->

#### save(self, keep=True)
Persist this upload

Saves a copy of this transfer process in its current state to disk.
This is done automatically for a running transfer, so that as a chunk
is completed, this is reflected. Thus, if a transfer is interrupted,
e.g., by user action, the transfer can be restarted at another time.
All chunks that were not already completed will be restarted at that
time.

See methods `load` to retrieved saved transfers and `run` to
resume a stopped transfer.


* **Parameters**

    **keep: bool (True)**

        If True, transfer will be saved if some chunks remain to be
        completed; the transfer will be sure to be removed otherwise.


<!-- !! processed by numpydoc !! -->

#### successful(self)
Return whether the uploader completed successfully.

It will raise AssertionError if the uploader is active.

<!-- !! processed by numpydoc !! -->

#### class azure.datalake.store.multithread.ADLDownloader(adlfs, rpath, lpath, nthreads=None, chunksize=268435456, buffersize=4194304, blocksize=4194304, client=None, run=True, overwrite=False, verbose=False, progress_callback=None, timeout=0)
Download remote file(s) using chunks and threads

Launches multiple threads for efficient downloading, with chunksize
assigned to each. The remote path can be a single file, a directory
of files or a glob pattern.


* **Parameters**

    **adlfs: ADL filesystem instance**

    **rpath: str**

        remote path/globstring to use to find remote files. Recursive glob
        patterns using \*\* are not supported.

    **lpath: str**

        local path. If downloading a single file, will write to this specific
        file, unless it is an existing directory, in which case a file is
        created within it. If downloading multiple files, this is the root
        directory to write within. Will create directories as required.

    **nthreads: int [None]**

        Number of threads to use. If None, uses the number of cores.

    **chunksize: int [2\*\*28]**

        Number of bytes for a chunk. Large files are split into chunks. Files
        smaller than this number will always be transferred in a single thread.

    **buffersize: int [2\*\*22]**

        Ignored in curret implementation.
        Number of bytes for internal buffer. This block cannot be bigger than
        a chunk and cannot be smaller than a block.

    **blocksize: int [2\*\*22]**

        Number of bytes for a block. Within each chunk, we write a smaller
        block for each API call. This block cannot be bigger than a chunk.

    **client: ADLTransferClient [None]**

        Set an instance of ADLTransferClient when finer-grained control over
        transfer parameters is needed. Ignores nthreads and chunksize set
        by constructor.

    **run: bool [True]**

        Whether to begin executing immediately.

    **overwrite: bool [False]**

        Whether to forcibly overwrite existing files/directories. If False and
        local path is a directory, will quit regardless if any files would be
        overwritten or not. If True, only matching filenames are actually
        overwritten.

    **progress_callback: callable [None]**

        Callback for progress with signature function(current, total) where
        current is the number of bytes transfered so far, and total is the
        size of the blob, or None if the total size is unknown.

    **timeout: int (0)**

        Default value 0 means infinite timeout. Otherwise time in seconds before the
        process will stop and raise an exception if  transfer is still in progress



* **Attributes**

    **hash**


### Methods




<!-- !! processed by numpydoc !! -->

#### active(self)
Return whether the downloader is active

<!-- !! processed by numpydoc !! -->

#### static clear_saved()
Remove references to all persisted downloads.

<!-- !! processed by numpydoc !! -->

#### static load()
Load list of persisted transfers from disk, for possible resumption.


* **Returns**

    A dictionary of download instances. The hashes are auto-

        generated unique. The state of the chunks completed, errored, etc.,
        can be seen in the status attribute. Instances can be resumed with
        `run()`.


<!-- !! processed by numpydoc !! -->

#### run(self, nthreads=None, monitor=True)
Populate transfer queue and execute downloads


* **Parameters**

    **nthreads: int [None]**

        Override default nthreads, if given

    **monitor: bool [True]**

        To watch and wait (block) until completion.


<!-- !! processed by numpydoc !! -->

#### save(self, keep=True)
Persist this download

Saves a copy of this transfer process in its current state to disk.
This is done automatically for a running transfer, so that as a chunk
is completed, this is reflected. Thus, if a transfer is interrupted,
e.g., by user action, the transfer can be restarted at another time.
All chunks that were not already completed will be restarted at that
time.

See methods `load` to retrieved saved transfers and `run` to
resume a stopped transfer.


* **Parameters**

    **keep: bool (True)**

        If True, transfer will be saved if some chunks remain to be
        completed; the transfer will be sure to be removed otherwise.


<!-- !! processed by numpydoc !! -->

#### successful(self)
Return whether the downloader completed successfully.

It will raise AssertionError if the downloader is active.

<!-- !! processed by numpydoc !! -->

#### azure.datalake.store.lib.auth(tenant_id=None, username=None, password=None, client_id='', client_secret=None, resource='https://datalake.azure.net/', require_2fa=False, authority=None, retry_policy=None, \*\*kwargs)
User/password authentication


* **Parameters**

    **tenant_id: str**

        associated with the user’s subscription, or “common”

    **username: str**

        active directory user

    **password: str**

        sign-in password

    **client_id: str**

        the service principal client

    **client_secret: str**

        the secret associated with the client_id

    **resource: str**

        resource for auth (e.g., [https://datalake.azure.net/](https://datalake.azure.net/))

    **require_2fa: bool**

        indicates this authentication attempt requires two-factor authentication

    **authority: string**

        The full URI of the authentication authority to authenticate against (such as [https://login.microsoftonline.com/](https://login.microsoftonline.com/))

    **kwargs: key/values**

        Other parameters, for future use



* **Returns**

    :type DataLakeCredential :mod: A DataLakeCredential object


<!-- !! processed by numpydoc !! -->
