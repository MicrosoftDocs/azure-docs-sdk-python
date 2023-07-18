---
title: Azure DevTest Labs SDK for Python
description: Reference for Azure DevTest Labs SDK for Python
author: lmazuel
ms.author: lmazuel
ms.data: 07/18/2023
ms.topic: reference
ms.devlang: python
ms.service: devtest-lab
ms.date: 06/07/2023
---
# Azure DevTest Labs libraries for python

## Management API

```bash
pip install azure-mgmt-devtestlabs
```

## Create the management client

The following code creates an instance of the management client.

You will need to provide your ``subscription_id`` which can be retrieved from [your subscription list](https://manage.windowsazure.com/#Workspaces/AdminTasks/SubscriptionMapping).

See [Resource Management Authentication](/python/azure/python-sdk-azure-authenticate) for details on handling Azure Active Directory authentication with the Python SDK, and creating a ``Credentials`` instance.

```python
from azure.mgmt.devtestlabs import DevTestLabsClient
from azure.common.credentials import UserPassCredentials

# Replace this with your subscription id
subscription_id = '33333333-3333-3333-3333-333333333333'

# See above for details on creating different types of AAD credentials
credentials = UserPassCredentials(
    'user@domain.com',  # Your user
    'my_password',      # Your password
)

devtestlabs_client = DevTestLabsClient(
    credentials,
    subscription_id
)
```

## Create lab

```python
async_lab = self.client.lab.create_or_update_resource(
    'MyResourceGroup',
    'MyLab',
    {'location': 'westus'}
)
lab = async_lab.result() # Blocking wait
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/mgmt-devtestlabs-readme)