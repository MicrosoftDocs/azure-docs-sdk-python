---
title: Azure Authorization SDK for Python
description: Reference for Azure Authorization SDK for Python
ms.date: 07/23/2024
ms.topic: reference
ms.devlang: python
ms.service: authorization
---
# Azure Authorization libraries for python

## [Management API](/python/api/overview/azure/authorization/management)

```bash
pip install azure-mgmt-authorization
```

## Create the management client

The following code creates an instance of the management client.

You will need to provide your ``subscription_id`` which can be retrieved from [your subscription list](https://manage.windowsazure.com/#Workspaces/AdminTasks/SubscriptionMapping).

See [Resource Management Authentication](/python/azure/python-sdk-azure-authenticate) for details on handling Azure Active Directory authentication with the Python SDK, and creating a ``Credentials`` instance.

```python
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.common.credentials import UserPassCredentials

# Replace this with your subscription id
subscription_id = '33333333-3333-3333-3333-333333333333'

# See above for details on creating different types of AAD credentials
credentials = UserPassCredentials(
    'user@domain.com',	# Your user
    'my_password' 		# Your password
)

authorization_client = AuthorizationManagementClient(
    credentials,
    subscription_id
)
```

## Check permissions for a resource group

The following code checks permissions in a given resource group. To create or manage resource groups, see [Resource Management](/python/api/overview/azure/azure.mgmt.resource).

```python
from azure.mgmt.redis.models import Sku, RedisCreateOrUpdateParameters

group_name = 'myresourcegroup'
permissions = self.authorization_client.permissions.list_for_resource_group(
    group_name
)
# permissions is a iterable of Permissions instances
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure-mgmt-authorization)