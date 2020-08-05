---
title: Azure Storage client libraries for Python
description: 
keywords: Azure, Python, SDK, API, Storage
author: lisawong19
ms.author: routlaw
manager: douge
ms.date: 06/12/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: storage
---

# Azure Storage client libraries for Python

## Client Packages (12.X.X) - Latest

| Package Name | Reference                                     | Package Manager                                   | Source                                                 |
|--------------|-----------------------------------------------|---------------------------------------------------|--------------------------------------------------------|
| Storage Blob | [Reference](storage-blob-readme) | [PyPi](https://pypi.org/project/azure-storage-blob/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob) |
| Storage Queue | [Reference](storage-queue-readme) | [PyPi](https://pypi.org/project/azure-storage-queue/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/azure/storage/queue) |
| Storage File Share | [Reference](storage-file-share-readme) | [PyPi](https://pypi.org/project/azure-storage-file-share/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-file-share/azure/storage/fileshare) |
| Storage File Data Lake (Preview) | [Reference](storage-file-datalake-readme) | [PyPi](https://pypi.org/project/azure-storage-file-datalake/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-file-datalake/azure/storage/filedatalake) |
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
| Storage Management | [Reference](storage/management) | [PyPi](https://pypi.org/project/azure-mgmt-storage/) | [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-mgmt-storage) |
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

| | |
|--|--|
| [Get started with Azure Blob Storage in Python](https://docs.microsoft.com/azure/storage/blobs/storage-python-how-to-use-blob-storage) | Create, read, update, restrict access, and delete files and objects in Azure Storage. |
| [Manage Azure Storage accounts](https://azure.microsoft.com/resources/samples/storage-python-manage) | Create, update , and delete storage accounts. Retrieve and regenerate storage account access keys.

Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.
