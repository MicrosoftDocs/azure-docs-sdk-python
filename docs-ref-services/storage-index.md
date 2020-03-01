---
title: Azure Storage libraries for Python
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

# Azure Storage libraries for Python

## Client Packages (12.X.X)

|Service| PyPi package| Examples|Getting Started Guide|
|---|---|---|--|
|**Storage Blob**|[azure-storage-blob](https://pypi.org/project/azure-storage-blob/)|[storage-blob-python-examples](https://docs.microsoft.com/en-us/samples/azure/azure-sdk-for-python/storage-blob-samples/)|[Azure Storage Blob Quickstart](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python)|
|**Storage Queue**|[azure-storage-queue](https://pypi.org/project/azure-storage-queue/)|[storage-queue-python-examples](https://docs.microsoft.com/en-us/samples/azure/azure-sdk-for-python/storage-queue-samples/)|[Azure Storage Queue Quickstart](https://docs.microsoft.com/en-us/azure/storage/queues/storage-quickstart-queues-python)|
|**Storage File Share**|[azure-storage-file-share](https://pypi.org/project/azure-storage-file-share/)|[storage-file-share-python-examples](https://docs.microsoft.com/en-us/samples/azure/azure-sdk-for-python/storage-file-share-samples/)||
|||||

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

## Example
```python
from azure.storage.blob import ContainerClient, BlobClient

container_client = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="my_container")

container_client.create_container()

blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="my_container", blob_name="my_blob")

with open("./SampleSource.txt", "rb") as data:
    blob.upload_blob(data)

```

## Samples

| | |
|--|--|
| [Get started with Azure Blob Storage in Python](https://docs.microsoft.com/azure/storage/blobs/storage-python-how-to-use-blob-storage) | Create, read, update, restrict access, and delete files and objects in Azure Storage. |
| [Manage Azure Storage accounts](https://azure.microsoft.com/resources/samples/storage-python-manage) | Create, update , and delete storage accounts. Retrieve and regenerate storage account access keys.

Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.
