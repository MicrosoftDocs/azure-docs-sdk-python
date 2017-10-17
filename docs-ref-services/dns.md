---
title: Azure DNS libraries for python
description: Reference for Azure DNS libraries for python
keywords: Azure, python, SDK, API, DNS
author: sptramer
ms.author: sttramer
manager: douge

ms.date: 07/10/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
---

# Azure DNS libraries for python

## Overview

[Azure DNS](/azure/dns/dns-overview) is a hosting service for DNS domains that provides DNS resolution via the Azure infrastructure.

To get started with Azure DNS, see [Get started with Azure DNS using the Azure portal](/azure/dns/dns-getstarted-portal).

## Management APIs

Create and manage DNS zones and records with the management API.

Install the management package with pip.

```bash
pip install azure-mgmt-dns
```

### Example

Create a new DNS zone.

```python
from azure.mgmt.dns import DnsManagementClient

dns_client = DnsManagementClient(credentials, 'your-subscription-id')
zone = dns_client.zones.create_or_update('resource-group',
                                         'zone_name_no_dot',
                                         {
                                            "location": "global"
                                         })

```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/dns/managementlibrary)
