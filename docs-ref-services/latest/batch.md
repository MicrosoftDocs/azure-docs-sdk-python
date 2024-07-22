---
title: Azure Batch SDK for Python
description: Reference for Azure Batch SDK for Python
ms.date: 07/22/2024
ms.topic: reference
ms.devlang: python
ms.service: batch
---
# Azure Batch libraries for python

## Overview

Run large-scale parallel and high-performance computing applications efficiently in the cloud with [Azure Batch](/azure/batch/batch-technical-overview).

To get started with Azure Batch, see [Create a Batch account with the Azure portal](/azure/batch/batch-account-create-portal).

## Install the libraries

## Client library
The Azure Batch client libraries let you configure compute nodes and pools, define tasks and configure them to run in jobs, and set up a job manager to control and monitor job execution. [Learn more](/azure/batch/batch-api-basics) about using these objects to run large-scale parallel compute solutions.

```bash
pip install azure-batch
```
### Example

Set up a pool of Linux compute nodes in a batch account:

```python
import azure.batch
from azure.batch import batch_auth, BatchServiceClient, models

# create the batch client for an account using its URI and keys
creds = batch_auth.SharedKeyCredentials(account, key)
client = BatchServiceClient(creds, batch_url)

# Create the VirtualMachineConfiguration, specifying
# the VM image reference and the Batch node agent to
# be installed on the node.
vmc = models.VirtualMachineConfiguration(
    image_reference = models.ImageReference(
        publisher='Canonical',
        offer='UbuntuServer',
        sku='18.04-LTS'
        ),
    node_agent_sku_id = "batch.node.ubuntu 18.04")

# Assign the virtual machine configuration to the pool
new_pool = models.PoolAddParameter(
    id = 'new_pool',
    vm_size='standard_d2_v2',
    virtual_machine_configuration = vmc
)

# Create pool in the Batch service
client.pool.add(new_pool)
```

> [!div class="nextstepaction"]
> [Explore the Client APIs](/python/api/azure-batch)

## Management API
Use the Azure Batch management libraries to create and delete batch accounts, read and regenerate batch account keys, and manage batch account storage.

```bash
pip install azure-mgmt-batch
```

### Example
Create an Azure Batch account and configure a new application and Azure storage account for it.

```python
from azure.mgmt.batch import BatchManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

LOCATION ='eastus'
GROUP_NAME ='batchresourcegroup'
STORAGE_ACCOUNT_NAME ='batchstorageaccount'

# Create Resource group
print('Create Resource Group')
resource_client.resource_groups.create_or_update(GROUP_NAME, {'location': LOCATION})

# Create a storage account
storage_async_operation = storage_client.storage_accounts.create(
    GROUP_NAME,
    STORAGE_ACCOUNT_NAME,
    StorageAccountCreateParameters(
        sku=Sku(SkuName.standard_ragrs),
        kind=Kind.storage,
        location=LOCATION
    )
)
storage_account = storage_async_operation.result()

# Create a Batch Account, specifying the storage account we want to link
storage_resource = storage_account.id
batch_account_parameters = azure.mgmt.batch.models.BatchAccountCreateParameters(
    location=LOCATION,
    auto_storage=azure.mgmt.batch.models.AutoStorageBaseProperties(storage_resource)
)
creating = batch_client.batch_account.begin_create('MyBatchResourceGroup', 'MyBatchAccount', batch_account_parameters)
creating.wait()
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure-mgmt-batch)