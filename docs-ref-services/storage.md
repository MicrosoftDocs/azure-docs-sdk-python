---
title: Azure Storage libraries for Python
description: 
keywords: Azure, Python, SDK, API, Storage
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/12/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: storage
---

# Azure Storage libraries for Python

## Overview
- Read and write objects and files from [Azure Blob storage](https://docs.microsoft.com/en-us/azure/storage/storage-python-how-to-use-blob-storage)
- Send and receive messages between cloud-connected applications with [Azure Queue storage](https://docs.microsoft.com/azure/storage/storage-python-how-to-use-queue-storage)
- Read and write large structured data with [Azure Table storage](https://docs.microsoft.com/azure/storage/storage-python-how-to-use-table-storage) 
- Share storage between apps with [Azure File storage](https://docs.microsoft.com/azure/storage/storage-python-how-to-use-file-storage)

## Import the libraries
```bash
pip install --pre azure-mgmt-storage
```

## Example
```python
storage_client = CloudStorageAccount(storage_account_name, storage_key)
blob_service = storage_client.create_block_blob_service()

blob_service.create_container(
    'mycontainername',
    public_access=PublicAccess.Blob
)

blob_service.create_blob_from_bytes(
    'mycontainername',
    'myblobname',
    b'<center><h1>Hello World!</h1></center>',
    content_settings=ContentSettings('text/html')
)

print(blob_service.make_blob_url('mycontainername', 'myblobname'))
```

## Samples

| | |
|--|--|
| [Get started with Azure Blob Storage in Python](https://azure.microsoft.com/resources/samples/storage-blob-python-getting-started/) | Create, read, update, restrict access, and delete files and objects in Azure Storage. |
| [Get started with Azure Queue Storage in Python](https://azure.microsoft.com/resources/samples/storage-queue-python-getting-started/) | Insert, peek, retrieve and delete messages from Azure Storage queues. | 
| [Manage Azure Storage accounts](https://azure.microsoft.com/resources/samples/storage-python-manage) | Create, update , and delete storage accounts. Retrieve and regenerate storage account access keys.

Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.