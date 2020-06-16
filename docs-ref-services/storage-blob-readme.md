---
title: Azure Storage Blob client library for Python
keywords: Azure, python, SDK, API, azure-storage-blob, azure-storage-blob
author: maggiepint
ms.author: magpint
ms.date: 05/28/2020
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: azure-storage-blob
---

Blob storage is ideal for:

* Serving images or documents directly to a browser
* Storing files for distributed access
* Streaming video and audio
* Storing data for backup and restore, disaster recovery, and archiving
* Storing data for analysis by an on-premises or Azure-hosted service

[Source code](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/azure/storage/blob) | [Package (PyPI)](https://pypi.org/project/azure-storage-blob/) | [API reference documentation](https://aka.ms/azsdk-python-storage-blob-ref) | [Product documentation](https://docs.microsoft.com/azure/storage/) | [Samples](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples)


## Getting started

## 1: Set up your local development environment
 
If you haven't already, follow all the instructions on [Configure your local Python dev environment for Azure](https://docs.microsoft.com/azure/developer/python/configure-local-development-environment?tabs=bash).
 
Be sure to create a service principal for local development, and create and activate a virtual environment for this project.

## 2. Create a storage account

[Create a storage account](https://docs.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)

## 3. Install the package

```bash
pip install azure-storage-blob
```


## 4. Create the client
The Azure Storage Blobs client library for Python allows you to interact with three types of resources: the storage
account itself, blob storage containers, and blobs. Interaction with these resources starts with an instance of a
[client](#clients). To create a client object, you will need the storage account's blob service account URL and a
credential that allows you to access the storage account:

```python
from azure.storage.blob import BlobServiceClient

service = BlobServiceClient(account_url="https://<my-storage-account-name>.blob.core.windows.net/", credential=new DefaultAzureCredential())
```

*Notes:* If you have created a service principal following the [configure your local environment documentation](https://docs.microsoft.com/azure/developer/python/configure-local-development-environment?tabs=bash), `Default Azure Credential` works without additional parameters. For additional configuration options see [Authorizing access to data in Azure Storage](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth?toc=/azure/storage/blobs/toc.json).

You can find the storage account's blob service URL using the [Azure Portal](https://docs.microsoft.com/azure/storage/common/storage-account-overview#storage-account-endpoints).

## Examples
The following sections provide several code snippets covering some of the most common Storage Blob tasks, including:

* [Uploading a blob](#uploading-a-blob "Uploading a blob")
* [Downloading a blob](#downloading-a-blob "Downloading a blob")
* [Enumerating blobs](#enumerating-blobs "Enumerating blobs")

Note that a container must be created before to upload or download a blob.

### Create a container

Create a container from where you can upload or download blobs.
```python
from azure.storage.blob import ContainerClient

container_client = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="my_container")

container_client.create_container()
```

Use the async client to upload a blob

```python
from azure.storage.blob.aio import ContainerClient

container_client = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="my_container")

await container_client.create_container()
```

### Uploading a blob
Upload a blob to your container

```python
from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="my_container", blob_name="my_blob")

with open("./SampleSource.txt", "rb") as data:
    blob.upload_blob(data)
```

Use the async client to upload a blob

```python
from azure.storage.blob.aio import BlobClient

blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="my_container", blob_name="my_blob")

with open("./SampleSource.txt", "rb") as data:
    await blob.upload_blob(data)
```

### Downloading a blob
Download a blob from your container

```python
from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(conn_str="my_connection_string", container_name="my_container", blob_name="my_blob")

with open("./BlockDestination.txt", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)
```

Download a blob asynchronously

```python
from azure.storage.blob.aio import BlobClient

blob = BlobClient.from_connection_string(conn_str="my_connection_string", container_name="my_container", blob_name="my_blob")

with open("./BlockDestination.txt", "wb") as my_blob:
    stream = await blob.download_blob()
    data = await stream.readall()
    my_blob.write(data)
```

### Enumerating blobs
List the blobs in your container

```python
from azure.storage.blob import ContainerClient

container = ContainerClient.from_connection_string(conn_str="my_connection_string", container_name="my_container")

blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name + '\n')
```

List the blobs asynchronously

```python
from azure.storage.blob.aio import ContainerClient

container = ContainerClient.from_connection_string(conn_str="my_connection_string", container_name="my_container")

blob_list = []
async for blob in container.list_blobs():
    blob_list.append(blob)
print(blob_list)
```

## Understanding the Examples
The following components make up the Azure Blob Service:
* The storage account itself
* A container within the storage account
* A blob within a container

The Azure Storage Blobs client library for Python allows you to interact with each of these components through the
use of a dedicated client object.

### Clients
Four different clients are provided to to interact with the various components of the Blob Service:
1. [BlobServiceClient](https://aka.ms/azsdk-python-storage-blob-blobserviceclient) -
    this client represents interaction with the Azure storage account itself, and allows you to acquire preconfigured
    client instances to access the containers and blobs within. It provides operations to retrieve and configure the
    account properties as well as list, create, and delete containers within the account. To perform operations on a
    specific container or blob, retrieve a client using the `get_container_client` or `get_blob_client` methods.
2. [ContainerClient](https://aka.ms/azsdk-python-storage-blob-containerclient) -
    this client represents interaction with a specific container (which need not exist yet), and allows you to acquire
    preconfigured client instances to access the blobs within. It provides operations to create, delete, or configure a
    container and includes operations to list, upload, and delete the blobs within it. To perform operations on a
    specific blob within the container, retrieve a client using the `get_blob_client` method.
3. [BlobClient](https://aka.ms/azsdk-python-storage-blob-blobclient) -
    this client represents interaction with a specific blob (which need not exist yet). It provides operations to
    upload, download, delete, and create snapshots of a blob, as well as specific operations per blob type.
4. [BlobLeaseClient](https://aka.ms/azsdk-python-storage-blob-blobleaseclient) -
    this client represents lease interactions with a `ContainerClient` or `BlobClient`. It provides operations to
    acquire, renew, release, change, and break a lease on a specified resource.

### Blob Types
Once you've initialized a Client, you can choose from the different types of blobs:
* [Block blobs](https://docs.microsoft.com/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs#about-block-blobs)
  store text and binary data, up to approximately 4.75 TiB. Block blobs are made up of blocks of data that can be
  managed individually
* [Append blobs](https://docs.microsoft.com/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs#about-append-blobs)
  are made up of blocks like block blobs, but are optimized for append operations. Append blobs are ideal for scenarios
  such as logging data from virtual machines
* [Page blobs](https://docs.microsoft.com/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs#about-page-blobs)
  store random access files up to 8 TiB in size. Page blobs store virtual hard drive (VHD) files and serve as disks for
  Azure virtual machines


## Optional Configuration

Optional keyword arguments that can be passed in at the client and per-operation level. 

### Retry Policy configuration

Use the following keyword arguments when instantiating a client to configure the retry policy:

* __retry_total__ (int): Total number of retries to allow. Takes precedence over other counts.
Pass in `retry_total=0` if you do not want to retry on requests. Defaults to 10.
* __retry_connect__ (int): How many connection-related errors to retry on. Defaults to 3.
* __retry_read__ (int): How many times to retry on read errors. Defaults to 3.
* __retry_status__ (int): How many times to retry on bad status codes. Defaults to 3.
* __retry_to_secondary__ (bool): Whether the request should be retried to secondary, if able.
This should only be enabled of RA-GRS accounts are used and potentially stale data can be handled.
Defaults to `False`.

### Encryption configuration

Use the following keyword arguments when instantiating a client to configure encryption:

* __require_encryption__ (bool): If set to True, will enforce that objects are encrypted and decrypt them.
* __key_encryption_key__ (object): The user-provided key-encryption-key. The instance must implement the following methods:
    - `wrap_key(key)`--wraps the specified key using an algorithm of the user's choice. 
    - `get_key_wrap_algorithm()`--returns the algorithm used to wrap the specified symmetric key.
    - `get_kid()`--returns a string key id for this key-encryption-key.
* __key_resolver_function__ (callable): The user-provided key resolver. Uses the kid string to return a key-encryption-key
implementing the interface defined above.

### Other client / per-operation configuration

Other optional configuration keyword arguments that can be specified on the client or per-operation.

**Client keyword arguments:**

* __connection_timeout__ (int): Optionally sets the connect and read timeout value, in seconds.
* __transport__ (Any): User-provided transport to send the HTTP request.

**Per-operation keyword arguments:**

* __raw_response_hook__ (callable): The given callback uses the response returned from the service.
* __raw_request_hook__ (callable): The given callback uses the request before being sent to service.
* __client_request_id__ (str): Optional user specified identification of the request.
* __user_agent__ (str): Appends the custom value to the user-agent header to be sent with the request.
* __logging_enable__ (bool): Enables logging at the DEBUG level. Defaults to False. Can also be passed in at
the client level to enable it for all requests.
* __headers__ (dict): Pass in custom headers as key, value pairs. E.g. `headers={'CustomValue': value}`

## Troubleshooting
### General
Storage Blob clients raise exceptions defined in [Azure Core](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/core/azure-core/README.md).
All Blob service operations will throw a `StorageErrorException` on failure with helpful [error codes](https://docs.microsoft.com/rest/api/storageservices/blob-service-error-codes).

### Logging
This library uses the standard
[logging](https://docs.python.org/3/library/logging.html) library for logging.
Basic information about HTTP sessions (URLs, headers, etc.) is logged at INFO
level.

Detailed DEBUG level logging, including request/response bodies and unredacted
headers, can be enabled on a client with the `logging_enable` argument:
```python
import sys
import logging
from azure.storage.blob import BlobServiceClient

# Create a logger for the 'azure.storage.blob' SDK
logger = logging.getLogger('azure.storage.blob')
logger.setLevel(logging.DEBUG)

# Configure a console output
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

# This client will log detailed information about its HTTP sessions, at DEBUG level
service_client = BlobServiceClient.from_connection_string("your_connection_string", logging_enable=True)
```

Similarly, `logging_enable` can enable detailed logging for a single operation,
even when it isn't enabled for the client:
```py
service_client.get_service_stats(logging_enable=True)
```
## Next steps

# Azure Storage Blob client library for Python - Version 12.3.1 
 Samples

These are code samples that show common scenario operations with the Azure Storage Blob client library.
The async versions of the samples (the python sample files appended with `_async`) show asynchronous operations, 
and require Python 3.5 or later.

Several Storage Blobs Python SDK samples are available to you in the SDK's GitHub repository. These samples provide example code for additional scenarios commonly encountered while working with Storage Blobs:

* [blob_samples_hello_world.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_hello_world.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_hello_world_async.py)) - Examples for common Storage Blob tasks:
    * Set up a container
    * Create a block, page, or append blob
    * Upload blobs
    * Download blobs
    * Delete blobs

* [blob_samples_authentication.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_authentication.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_authentication_async.py)) - Examples for authenticating and creating the client:
    * From a connection string
    * From a shared access key
    * From a shared access signature token
    * From active directory
    
* [blob_samples_service.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_service.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_service_async.py)) - Examples for interacting with the blob service:
    * Get account information
    * Get and set service properties
    * Get service statistics
    * Create, list, and delete containers
    * Get the Blob or Container client

* [blob_samples_containers.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_containers.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_containers_async.py)) - Examples for interacting with containers:
    * Create a container and delete containers
    * Set metadata on containers
    * Get container properties
    * Acquire a lease on container
    * Set an access policy on a container
    * Upload, list, delete blobs in container
    * Get the blob client to interact with a specific blob

* [blob_samples_common.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_common.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_common_async.py)) - Examples common to all types of blobs:
    * Create a snapshot
    * Delete a blob snapshot
    * Soft delete a blob
    * Undelete a blob
    * Acquire a lease on a blob
    * Copy a blob from a URL

* [blob_samples_directory_interface.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_directory_interface.py) - Examples for interfacing with Blob storage as if it were a directory on a filesystem:
    * Copy (upload or download) a single file or directory
    * List files or directories at a single level or recursively
    * Delete a single file or recursively delete a directory

* [blob_samples_batch_delete_blobs.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_batch_delete_blobs.py) - Examples for batch
deleting blobs
    * Delete multiple blobs at the same time.

* [blob_samples_container_access_policy.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_container_access_policy.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_container_access_policy_async.py)) - Examples to
get and set access policies:
    * Get and Set container Access Policy

* [blob_samples_copy_blob.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_copy_blob.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_copy_blob_async.py)) - Examples to start and abort copy:
    * Start a copy from url and abort it.

* [blob_samples_enumerate_blobs.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_enumerate_blobs.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_enumerate_blobs_async.py)) - Example to enumerate blobs
    * List all the blobs in a container.

* [blob_samples_walk_blob_hierarchy.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_walk_blob_hierarchy.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_walk_blob_hierarchy_async.py)) - Example to walk through containers and blobs in a hierarchical structure.
    * Walk through the container.

* [blob_samples_network_activity_logging.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_network_activity_logging.py) - Examples to enable logging to the console.
    * Log the network activity at different levels.

* [blob_samples_proxy_configuration.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples/blob_samples_proxy_configuration.py) - Examples to work with a proxy.
    * Work with a proxy using the storage account.

## Prerequisites
* Python 2.7, or 3.5 or later is required to use this package (3.5 or later if using asyncio)
* You must have an [Azure subscription](https://azure.microsoft.com/free/) and an
[Azure storage account](https://docs.microsoft.com/azure/storage/common/storage-account-overview) to run these samples.

## Setup

1. Install the Azure Storage Blob client library for Python - Version 12.3.1 
 with [pip](https://pypi.org/project/pip/):

```bash
pip install azure-storage-blob
```

2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## Running the samples

1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. Follow the usage described in the file, e.g. `python blob_samples_hello_world.py`

## Next steps

Check out the [API reference documentation](https://aka.ms/azsdk-python-storage-blob-ref) to learn more about
what you can do with the Azure Storage Blob client library.

