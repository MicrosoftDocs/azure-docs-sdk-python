---
title: Azure Scheduler libraries for python
description: Reference for Azure Scheduler libraries for python
keywords: Azure, python, SDK, API, Scheduler
author: lisawong19
ms.author: ramyar
manager: mbaldwin

ms.date: 02/21/2018
ms.topic: reference
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
---

# Azure Scheduler libraries for python

## Install the libraries

## Management

```bash
pip install azure-mgmt-scheduler
```
## Example

### Create the management client

The following code creates an instance of the management client.

You will need to provide your ``subscription_id`` which can be retrieved
from [your subscription list](https://manage.windowsazure.com/#Workspaces/AdminTasks/SubscriptionMapping).

See [Resource Management Authentication](/python/azure/python-sdk-azure-authenticate) for details on handling Azure Active Directory authentication with the Python SDK, and creating a ``Credentials`` instance.

```python
from azure.mgmt.scheduler import SchedulerManagementClient
from azure.common.credentials import UserPassCredentials

# Replace this with your subscription id
subscription_id = '33333333-3333-3333-3333-333333333333'

# See above for details on creating different types of AAD credentials
credentials = UserPassCredentials(
    'user@domain.com',	# Your user
    'my_password',		# Your password
)

scheduler_client = SchedulerManagementClient(
    credentials,
    subscription_id
)
```

### Create a job collection

The following code creates a job collection under an existing resource group.
To create or manage resource groups, see [Resource Management](/python/api/overview/azure/azure.mgmt.resource).

```python
from azure.mgmt.scheduler.models import JobCollectionDefinition, JobCollectionProperties, Sku

group_name = 'myresourcegroup'
job_collection_name = "myjobcollection"
scheduler_client.job_collections.create_or_update(
    group_name,
    job_collection_name,
    JobCollectionDefinition(
        location = "West US",
        properties = JobCollectionProperties(
            sku = Sku(
                name="Free"
            )
        )
    )
)
# scheduler_client is a JobCollectionDefinition instance
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/scheduler/management)
