---
title: Azure Storage SDK for Python
description: Reference for Azure Storage SDK for Python
ms.date: 07/22/2024
ms.topic: reference
ms.devlang: python
ms.service: storage
---
# Azure Storage client libraries for Python

## Client Packages (12.X.X) - Latest

| Package Name | Reference                                     | Package Manager                                   | Source                                                 |
|--------------|-----------------------------------------------|---------------------------------------------------|--------------------------------------------------------|
| Storage Blob | [Reference](storage-blob-readme.md) | [PyPi](https://pypi.org/project/azure-storage-blob/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob) |
| Storage Queue | [Reference](storage-queue-readme.md) | [PyPi](https://pypi.org/project/azure-storage-queue/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/azure/storage/queue) |
| Storage File Share | [Reference](storage-file-share-readme.md) | [PyPi](https://pypi.org/project/azure-storage-file-share/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-file-share/azure/storage/fileshare) |
| Storage File Data Lake (Preview) | [Reference](storage-file-datalake-readme.md) | [PyPi](https://pypi.org/project/azure-storage-file-datalake/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-file-datalake/azure/storage/filedatalake) |
|              |                                               |                                                   |                                                        |

## Client Packages (2.X.X) - Legacy
| Package Name | Reference                                     | Package Manager                                   | Source                                                 |
|--------------|-----------------------------------------------|---------------------------------------------------|--------------------------------------------------------|
| Storage Blob | [Reference](/python/api/azure-storage-blob/?view=azure-python-previous&preserve-view=true) | [PyPi](https://pypi.org/project/azure-storage-blob/2.1.0/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob) |
| Storage Queue | [Reference](/python/api/azure-storage-queue/?view=azure-python-previous&preserve-view=true) | [PyPi](https://pypi.org/project/azure-storage-queue/2.1.0/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/azure/storage/queue) |
| Storage File Share | [Reference](/python/api/azure-storage-file/?view=azure-python-previous&preserve-view=true) | [PyPi](https://pypi.org/project/azure-storage-file/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-file-share/azure/storage/fileshare) |
|              |                                               |                                                   |                                                        |

## Management
| Package Name | Reference                                     | Package Manager                                   | Source                                                 |
|--------------|-----------------------------------------------|---------------------------------------------------|--------------------------------------------------------|
| Storage Management | [Reference](/python/api/azure-mgmt-storage/) | [PyPi](https://pypi.org/project/azure-mgmt-storage/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-mgmt-storage) |
|              |                                               |                                                   |                                                        |


## Install the libraries

### Client

Azure Storage Client Libraries consist of 3 packages: Blob, File Share, and Queue. To install the blob package, run:

```bash
pip install azure-storage-blob
```

### Management

```bash
pip install azure-mgmt-storage
```

## Samples

| Article | Description |
|--|--|
| [Get started with Azure Blob Storage in Python](/azure/storage/blobs/storage-python-how-to-use-blob-storage) | Create, read, update, restrict access, and delete files and objects in Azure Storage. |
| [Manage Azure Storage accounts](/samples/azure-samples/azure-samples-python-management/storage) | Create, update, and delete storage accounts. Retrieve and regenerate storage account access keys.

Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.

## Known issues

This section details known issues for the Azure Storage client libraries for Python.

### InvalidHeaderValue error message when using beta version of SDK

In rare scenarios, applications that have upgraded to the latest beta or generally available version of the SDK can receive an `InvalidHeaderValue` error message. This issue can occur when using any of the Storage libraries. The error message looks similar to the following sample:

```console
HTTP/1.1 400 The value for one of the HTTP headers is not in the correct format.
Content-Length: 328
Content-Type: application/xml
Server: Microsoft-HTTPAPI/2.0
x-ms-request-id: <REMOVED>
Date: Fri, 19 May 2023 17:10:33 GMT
 
<?xml version="1.0" encoding="utf-8"?><Error><Code>InvalidHeaderValue</Code><Message>The value for one of the HTTP headers is not in the correct format.
RequestId:<REMOVED>
Time:2023-05-19T17:10:34.2972651Z</Message><HeaderName>x-ms-version</HeaderName><HeaderValue>yyyy-mm-dd</HeaderValue></Error> 
```

If you've upgraded to the latest beta or generally available of the SDK and you experience this error, it's recommended that you downgrade to the previous generally available version of the SDK to see if the issue resolves. If the issue persists, or if the recommendation is not feasible, [open a support ticket](https://ms.portal.azure.com/#create/Microsoft.Support) to explore further options.