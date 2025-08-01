---
title: Azure Commerce SDK for Python
description: Reference for Azure Commerce SDK for Python
ms.date: 08/01/2025
ms.topic: reference
ms.devlang: python
ms.service: commerce
---
# Azure Commerce libraries for python

## [Management API](/python/api/overview/azure/commerce/management)

```bash
pip install azure-mgmt-commerce
```
## Create the commerce client

The following code creates an instance of the management client.

You will need to provide your ``subscription_id`` which can be retrieved from [your subscription list](https://manage.windowsazure.com/#Workspaces/AdminTasks/SubscriptionMapping).

See [Resource Management Authentication](/python/azure/python-sdk-azure-authenticate) for details on handling Azure Active Directory authentication with the Python SDK, and creating a ``Credentials`` instance.

```python
from azure.mgmt.commerce import UsageManagementClient
from azure.common.credentials import UserPassCredentials

# Replace this with your subscription id
subscription_id = '33333333-3333-3333-3333-333333333333'

# See above for details on creating different types of AAD credentials
credentials = UserPassCredentials(
    'user@domain.com',	# Your user
    'my_password',		# Your password
)

commerce_client = UsageManagementClient(
    credentials,
    subscription_id
)
``` 

## Get rate card

```python
# OfferDurableID: https://azure.microsoft.com/en-us/support/legal/offer-details/
rate = commerce_client.rate_card.get(
    "OfferDurableId eq 'MS-AZR-0062P' and Currency eq 'USD' and Locale eq 'en-US' and RegionInfo eq 'US'"
)
```

## Get Usage

```python
from datetime import date, timedelta

# Takes onky dates in full ISO8601 with 'T00:00:00Z'
# Return an iterator like object: https://docs.python.org/3/library/stdtypes.html#iterator-types
usage_iterator = commerce_client.usage_aggregates.list(
    str(date.today() - timedelta(days=1))+'T00:00:00Z',
    str(date.today())+'T00:00:00Z'
)
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure-mgmt-commerce)