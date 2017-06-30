---
title: Azure Batch libraries for Python
description: Reference documentation for the Python Batch libraries 
keywords: Azure, Python, SDK, API, Batch, processing, scheduling, long-running
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/28/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: batch
---

# Azure Batch libraries for python

## Overview

The Azure Batch client libraries let you configure compute nodes and pools, define tasks and configure them to run in jobs, and set up a job manager to control and monitor job execution. [Learn more](https://docs.microsoft.com/en-us/azure/batch/batch-api-basics) about using these objects to run large-scale parallel compute solutions.

Use the Azure Batch management libraries to create and delete batch accounts, read and regenerate batch account keys, and manage batch account storage.

## Install the libraries

### Client library

```bash
pip install azure-batch
```

### Management 

```bash
pip install azure-mgmt-batch
```

## Example

Set up a pool of Linux compute nodes in a batch account:

```python
# create the batch client for an account using its URI and keys
creds = batchauth.SharedKeyCredentials(account, key)
config = batch.BatchServiceClientConfiguration(creds, base_url = batch_url)
client = batch.BatchServiceClient(config)

# Create the VirtualMachineConfiguration, specifying
# the VM image reference and the Batch node agent to
# be installed on the node.
vmc = batchmodels.VirtualMachineConfiguration(
    image_reference = ir,
    node_agent_sku_id = "batch.node.ubuntu 14.04")

# Assign the virtual machine configuration to the pool
new_pool.virtual_machine_configuration = vmc

# Create pool in the Batch service
client.pool.add(new_pool)
```

Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.