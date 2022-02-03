---
title: Azure DNS libraries for python
description: Reference for Azure DNS libraries for python
keywords: Azure, python, SDK, API, DNS
author: sptramer
ms.author: sttramer
manager: douge

ms.date: 07/10/2017
ms.topic: reference
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
---

# Azure DNS libraries for python

## Overview

[Azure DNS](/azure/dns/dns-overview) is a hosting service for DNS domains that provides DNS resolution via the Azure infrastructure.

To get started with Azure DNS, see [Get started with Azure DNS using the Azure portal](/azure/dns/dns-getstarted-portal).

## [Management API](/python/api/overview/azure/dns/management)

```bash
pip install azure-mgmt-dns
```

## Create the management client

The following code creates an instance of the management client.

You will need to provide your ``subscription_id`` which can be retrieved
from [your subscription list](https://manage.windowsazure.com/#Workspaces/AdminTasks/SubscriptionMapping).

See [Resource Management Authentication](/python/azure/python-sdk-azure-authenticate)
for details on handling Azure Active Directory authentication with the Python SDK, and creating a ``Credentials`` instance.

```python 
from azure.mgmt.dns import DnsManagementClient
from azure.common.credentials import UserPassCredentials

# Replace this with your subscription id
subscription_id = '33333333-3333-3333-3333-333333333333'

# See above for details on creating different types of AAD credentials
credentials = UserPassCredentials(
	'user@domain.com',  # Your user
	'my_password',      # Your password
)

dns_client = DnsManagementClient(
	credentials,
	subscription_id
)
```

## Create DNS zone
```python
# The only valid value is 'global', otherwise you will get a:
# The subscription is not registered for the resource type 'dnszones' in the location 'westus'.
zone = dns_client.zones.create_or_update(
	'MyResourceGroup',
	'pydns.com',
	{
	        'zone_type': 'Public', # or Private
		'location': 'global'
	}
)
```
	
## Create a Record Set
```python
record_set = dns_client.record_sets.create_or_update(
	'MyResourceGroup',
	'pydns.com',
	'MyRecordSet',
	'A',
	{
			"ttl": 300,
			"arecords": [
				{
				"ipv4_address": "1.2.3.4"
				},
				{
				"ipv4_address": "1.2.3.5"
				}
			]
	}
)
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/dns/management)
