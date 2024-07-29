---
title: Azure Notification Hubs SDK for Python
description: Reference for Azure Notification Hubs SDK for Python
ms.date: 07/29/2024
ms.topic: reference
ms.devlang: python
ms.service: notificationhubs
---
# Azure Notification Hubs libraries for python

## [Management API](/python/api/overview/azure/notificationhubs/management)

```bash
pip install azure-mgmt-notificationhubs
```

## Create the management client

The following code creates an instance of the management client.

You will need to provide your ``subscription_id`` which can be retrieved from [your subscription list](https://manage.windowsazure.com/#Workspaces/AdminTasks/SubscriptionMapping).

See [Resource Management Authentication](/python/azure/python-sdk-azure-authenticate) for details on handling Azure Active Directory authentication with the Python SDK, and creating a ``Credentials`` instance.

```python
from azure.mgmt.notificationhubs import NotificationHubsManagementClient
from azure.common.credentials import UserPassCredentials

# Replace this with your subscription id
subscription_id = '33333333-3333-3333-3333-333333333333'

# See above for details on creating different types of AAD credentials
credentials = UserPassCredentials(
    'user@domain.com',	# Your user
    'my_password',		# Your password
)

redis_client = NotificationHubsManagementClient(
    credentials,
    subscription_id
)
```

## Check namespace availability

The following code check namespace availability of a notification hub.

```python
from azure.mgmt.notificationhubs.models import CheckAvailabilityParameters

account_name = 'mynotificationhub'
output = notificationhubs_client.namespaces.check_availability(
    azure.mgmt.notificationhubs.models.CheckAvailabilityParameters(
        name = account_name
    )
)
# output is a CheckAvailibilityResource instance
print(output.is_availiable) # Yes, it's 'availiable', it's a typo in the REST API
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure-mgmt-notificationhubs)