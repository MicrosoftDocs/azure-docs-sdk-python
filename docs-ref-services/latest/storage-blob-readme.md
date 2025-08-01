---
title: Azure Storage Blobs client library for Python
keywords: Azure, python, SDK, API, azure-storage-blob, storage
ms.date: 07/16/2025
ms.topic: reference
ms.devlang: python
ms.service: storage
---
# Azure Storage Blobs client library for Python - version 12.26.0 

Azure Blob storage is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data, such as text or binary data.

Blob storage is ideal for:

* Serving images or documents directly to a browser
* Storing files for distributed access
* Streaming video and audio
* Storing data for backup and restore, disaster recovery, and archiving
* Storing data for analysis by an on-premises or Azure-hosted service

[Source code](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/azure/storage/blob)
| [Package (PyPI)](https://pypi.org/project/azure-storage-blob/)
| [Package (Conda)](https://anaconda.org/microsoft/azure-storage/)
| [API reference documentation](https://aka.ms/azsdk-python-storage-blob-ref)
| [Product documentation](https://learn.microsoft.com/azure/storage/)
| [Samples](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples)


## Getting started

### Prerequisites
* Python 3.8 or later is required to use this package. For more details, please read our page on [Azure SDK for Python version support policy](https://github.com/Azure/azure-sdk-for-python/wiki/Azure-SDKs-Python-version-support-policy).
* You must have an [Azure subscription](https://azure.microsoft.com/free/) and an
[Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-overview) to use this package.

### Install the package
Install the Azure Storage Blobs client library for Python with [pip](https://pypi.org/project/pip/):

```bash
pip install azure-storage-blob
```

### Create a storage account
If you wish to create a new storage account, you can use the
[Azure Portal](https://learn.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-portal),
[Azure PowerShell](https://learn.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-powershell),
or [Azure CLI](https://learn.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-cli):

```bash
# Create a new resource group to hold the storage account -
# if using an existing resource group, skip this step
az group create --name my-resource-group --location westus2

# Create the storage account
az storage account create -n my-storage-account-name -g my-resource-group
```

### Create the client
The Azure Storage Blobs client library for Python allows you to interact with three types of resources: the storage
account itself, blob storage containers, and blobs. Interaction with these resources starts with an instance of a
[client](#clients). To create a client object, you will need the storage account's blob service account URL and a
credential that allows you to access the storage account:

```python
from azure.storage.blob import BlobServiceClient

service = BlobServiceClient(account_url="https://<my-storage-account-name>.blob.core.windows.net/", credential=credential)
```

#### Looking up the account URL
You can find the storage account's blob service URL using the
[Azure Portal](https://learn.microsoft.com/azure/storage/common/storage-account-overview#storage-account-endpoints),
[Azure PowerShell](https://learn.microsoft.com/powershell/module/az.storage/get-azstorageaccount),
or [Azure CLI](https://learn.microsoft.com/cli/azure/storage/account?view=azure-cli-latest#az-storage-account-show):

```bash
# Get the blob service account url for the storage account
az storage account show -n my-storage-account-name -g my-resource-group --query "primaryEndpoints.blob"
```

#### Types of credentials
The `credential` parameter may be provided in a number of different forms, depending on the type of
[authorization](https://learn.microsoft.com/azure/storage/common/storage-auth) you wish to use:
1. To use an [Azure Active Directory (AAD) token credential](https://learn.microsoft.com/azure/storage/common/storage-auth-aad),
   provide an instance of the desired credential type obtained from the
   [azure-identity](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/identity/azure-identity#credentials) library.
   For example, [DefaultAzureCredential](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/identity/azure-identity#defaultazurecredential)
   can be used to authenticate the client.

   This requires some initial setup:
   * [Install azure-identity](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/identity/azure-identity#install-the-package)
   * [Register a new AAD application](https://learn.microsoft.com/azure/active-directory/develop/quickstart-register-app) and give permissions to access Azure Storage
   * [Grant access](https://learn.microsoft.com/azure/storage/common/storage-auth-aad-rbac-portal) to Azure Blob data with RBAC in the Azure Portal
   * Set the values of the client ID, tenant ID, and client secret of the AAD application as environment variables:
     AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET

   Use the returned token credential to authenticate the client:
    ```python
    from azure.identity import DefaultAzureCredential
    from azure.storage.blob import BlobServiceClient
    token_credential = DefaultAzureCredential()

    blob_service_client = BlobServiceClient(
        account_url="https://<my_account_name>.blob.core.windows.net",
        credential=token_credential
    )
    ```

2. To use a [shared access signature (SAS) token](https://learn.microsoft.com/azure/storage/common/storage-sas-overview),
   provide the token as a string. If your account URL includes the SAS token, omit the credential parameter.
   You can generate a SAS token from the Azure Portal under "Shared access signature" or use one of the `generate_sas()`
   functions to create a sas token for the storage account, container, or blob:

    ```python
    from datetime import datetime, timedelta
    from azure.storage.blob import BlobServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions

    sas_token = generate_account_sas(
        account_name="<storage-account-name>",
        account_key="<account-access-key>",
        resource_types=ResourceTypes(service=True),
        permission=AccountSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1)
    )

    blob_service_client = BlobServiceClient(account_url="https://<my_account_name>.blob.core.windows.net", credential=sas_token)
    ```

3. To use a storage account [shared key](https://learn.microsoft.com/rest/api/storageservices/authenticate-with-shared-key/)
   (aka account key or access key), provide the key as a string. This can be found in the Azure Portal under the "Access Keys"
   section or by running the following Azure CLI command:

    ```az storage account keys list -g MyResourceGroup -n MyStorageAccount```

    Use the key as the credential parameter to authenticate the client:
    ```python
    from azure.storage.blob import BlobServiceClient
    service = BlobServiceClient(account_url="https://<my_account_name>.blob.core.windows.net", credential="<account_access_key>")
    ```
    
    If you are using **customized url** (which means the url is not in this format `<my_account_name>.blob.core.windows.net`),
    please instantiate the client using the credential below:
    ```python
    from azure.storage.blob import BlobServiceClient
    service = BlobServiceClient(account_url="https://<my_account_name>.blob.core.windows.net", 
       credential={"account_name": "<your_account_name>", "account_key":"<account_access_key>"})
    ```

4. To use [anonymous public read access](https://learn.microsoft.com/azure/storage/blobs/storage-manage-access-to-resources),
   simply omit the credential parameter.

#### Creating the client from a connection string
Depending on your use case and authorization method, you may prefer to initialize a client instance with a storage
connection string instead of providing the account URL and credential separately. To do this, pass the storage
connection string to the client's `from_connection_string` class method:

```python
from azure.storage.blob import BlobServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=xxxx;AccountKey=xxxx;EndpointSuffix=core.windows.net"
service = BlobServiceClient.from_connection_string(conn_str=connection_string)
```

The connection string to your storage account can be found in the Azure Portal under the "Access Keys" section or by running the following CLI command:

```bash
az storage account show-connection-string -g MyResourceGroup -n MyStorageAccount
```

## Key concepts
The following components make up the Azure Blob Service:
* The storage account itself
* A container within the storage account
* A blob within a container

The Azure Storage Blobs client library for Python allows you to interact with each of these components through the
use of a dedicated client object.

### Clients
Four different clients are provided to interact with the various components of the Blob Service:
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

### Async Clients 
This library includes a complete async API supported on Python 3.5+. To use it, you must
first install an async transport, such as [aiohttp](https://pypi.org/project/aiohttp/).
See
[azure-core documentation](https://github.com/Azure/azure-sdk-for-python/blob/azure-storage-blob_12.26.0/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#transport)
for more information.

Async clients and credentials should be closed when they're no longer needed. These
objects are async context managers and define async `close` methods.

### Blob Types
Once you've initialized a Client, you can choose from the different types of blobs:
* [Block blobs](https://learn.microsoft.com/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs#about-block-blobs)
  store text and binary data, up to approximately 4.75 TiB. Block blobs are made up of blocks of data that can be
  managed individually
* [Append blobs](https://learn.microsoft.com/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs#about-append-blobs)
  are made up of blocks like block blobs, but are optimized for append operations. Append blobs are ideal for scenarios
  such as logging data from virtual machines
* [Page blobs](https://learn.microsoft.com/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs#about-page-blobs)
  store random access files up to 8 TiB in size. Page blobs store virtual hard drive (VHD) files and serve as disks for
  Azure virtual machines

## Examples
The following sections provide several code snippets covering some of the most common Storage Blob tasks, including:

* [Create a container](#create-a-container "Create a container")
* [Uploading a blob](#uploading-a-blob "Uploading a blob")
* [Downloading a blob](#downloading-a-blob "Downloading a blob")
* [Enumerating blobs](#enumerating-blobs "Enumerating blobs")

Note that a container must be created before to upload or download a blob.

### Create a container

Create a container from where you can upload or download blobs.
```python
from azure.storage.blob import ContainerClient

container_client = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="mycontainer")

container_client.create_container()
```

Use the async client to create a container

```python
from azure.storage.blob.aio import ContainerClient

container_client = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="mycontainer")

await container_client.create_container()
```

### Uploading a blob
Upload a blob to your container

```python
from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="mycontainer", blob_name="my_blob")

with open("./SampleSource.txt", "rb") as data:
    blob.upload_blob(data)
```

Use the async client to upload a blob

```python
from azure.storage.blob.aio import BlobClient

blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="mycontainer", blob_name="my_blob")

with open("./SampleSource.txt", "rb") as data:
    await blob.upload_blob(data)
```

### Downloading a blob
Download a blob from your container

```python
from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="mycontainer", blob_name="my_blob")

with open("./BlockDestination.txt", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)
```

Download a blob asynchronously

```python
from azure.storage.blob.aio import BlobClient

blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="mycontainer", blob_name="my_blob")

with open("./BlockDestination.txt", "wb") as my_blob:
    stream = await blob.download_blob()
    data = await stream.readall()
    my_blob.write(data)
```

### Enumerating blobs
List the blobs in your container

```python
from azure.storage.blob import ContainerClient

container = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="mycontainer")

blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name + '\n')
```

List the blobs asynchronously

```python
from azure.storage.blob.aio import ContainerClient

container = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="mycontainer")

blob_list = []
async for blob in container.list_blobs():
    blob_list.append(blob)
print(blob_list)
```

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
* __encryption_version__ (str): Specifies the version of encryption to use. Current options are `'2.0'` or `'1.0'` and
the default value is `'1.0'`. Version 1.0 is deprecated, and it is **highly recommended** to use version 2.0.
* __key_encryption_key__ (object): The user-provided key-encryption-key. The instance must implement the following methods:
    - `wrap_key(key)`--wraps the specified key using an algorithm of the user's choice.
    - `get_key_wrap_algorithm()`--returns the algorithm used to wrap the specified symmetric key.
    - `get_kid()`--returns a string key id for this key-encryption-key.
* __key_resolver_function__ (callable): The user-provided key resolver. Uses the kid string to return a key-encryption-key
implementing the interface defined above.

### Other client / per-operation configuration

Other optional configuration keyword arguments that can be specified on the client or per-operation.

**Client keyword arguments:**

* __connection_timeout__ (int): The number of seconds the client will wait to establish a connection to the server.
Defaults to 20 seconds.
* __read_timeout__ (int): The number of seconds the client will wait, between consecutive read operations, for a
response from the server. This is a socket level timeout and is not affected by overall data size. Client-side read 
timeouts will be automatically retried. Defaults to 60 seconds.
* __transport__ (Any): User-provided transport to send the HTTP request.

**Per-operation keyword arguments:**

* __raw_response_hook__ (callable): The given callback uses the response returned from the service.
* __raw_request_hook__ (callable): The given callback uses the request before being sent to service.
* __client_request_id__ (str): Optional user specified identification of the request.
* __user_agent__ (str): Appends the custom value to the user-agent header to be sent with the request.
* __logging_enable__ (bool): Enables logging at the DEBUG level. Defaults to False. Can also be passed in at
the client level to enable it for all requests.
* __logging_body__ (bool): Enables logging the request and response body. Defaults to False. Can also be passed in at
the client level to enable it for all requests.
* __headers__ (dict): Pass in custom headers as key, value pairs. E.g. `headers={'CustomValue': value}`

## Troubleshooting
### General
Storage Blob clients raise exceptions defined in [Azure Core](https://github.com/Azure/azure-sdk-for-python/blob/azure-storage-blob_12.26.0/sdk/core/azure-core/README.md).

This list can be used for reference to catch thrown exceptions. To get the specific error code of the exception, use the `error_code` attribute, i.e, `exception.error_code`.

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
```python
service_client.get_service_stats(logging_enable=True)
```

## Next steps

### More sample code

Get started with our [Blob samples](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples).

Several Storage Blobs Python SDK samples are available to you in the SDK's GitHub repository. These samples provide example code for additional scenarios commonly encountered while working with Storage Blobs:

* [blob_samples_container_access_policy.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_container_access_policy.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_container_access_policy_async.py)) - Examples to set Access policies:
    * Set up Access Policy for container

* [blob_samples_hello_world.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_hello_world.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_hello_world_async.py)) - Examples for common Storage Blob tasks:
    * Set up a container
    * Create a block, page, or append blob
    * Upload blobs
    * Download blobs
    * Delete blobs

* [blob_samples_authentication.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_authentication.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_authentication_async.py)) - Examples for authenticating and creating the client:
    * From a connection string
    * From a shared access key
    * From a shared access signature token
    * From active directory

* [blob_samples_service.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_service.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_service_async.py)) - Examples for interacting with the blob service:
    * Get account information
    * Get and set service properties
    * Get service statistics
    * Create, list, and delete containers
    * Get the Blob or Container client

* [blob_samples_containers.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_containers.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_containers_async.py)) - Examples for interacting with containers:
    * Create a container and delete containers
    * Set metadata on containers
    * Get container properties
    * Acquire a lease on container
    * Set an access policy on a container
    * Upload, list, delete blobs in container
    * Get the blob client to interact with a specific blob

* [blob_samples_common.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_common.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_common_async.py)) - Examples common to all types of blobs:
    * Create a snapshot
    * Delete a blob snapshot
    * Soft delete a blob
    * Undelete a blob
    * Acquire a lease on a blob
    * Copy a blob from a URL

* [blob_samples_directory_interface.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.26.0/sdk/storage/azure-storage-blob/samples/blob_samples_directory_interface.py) - Examples for interfacing with Blob storage as if it were a directory on a filesystem:
    * Copy (upload or download) a single file or directory
    * List files or directories at a single level or recursively
    * Delete a single file or recursively delete a directory

### Additional documentation
For more extensive documentation on Azure Blob storage, see the [Azure Blob storage documentation](https://learn.microsoft.com/azure/storage/blobs/) on learn.microsoft.com.

## Contributing
This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

