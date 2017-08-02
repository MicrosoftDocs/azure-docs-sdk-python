---
title: Azure Network libraries for python
description: Reference for Azure Network libraries for python
keywords: Azure, python, SDK, API, Network
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

# Azure Network libraries for python

## Overview

[Azure Virtual Network](/azure/virtual-network/virtual-networks-overview) allows you to connect Azure resources, and also connect them to your on-premises network.

To get started with Azure Virtual Network, see [Create your first virtual network](/azure/virtual-network/virtual-network-get-started-vnet-subnet).

## Management APIs

Inspect, manage, and configure Azure virtual networks with the management APIs.

Unlike other Azure python APIs, the networking APIs are explicitly versioned into separage packages. You do not need to import them individually since the package information is specified in the client constructor.

Install the management package with pip.

```bash
pip install azure-mgmt-network
```

### Example

Create a virtual network and an associated subnet.

```python
from azure.mgmt.network import NetworkManagementClient

GROUP_NAME = 'resource-group'
VNET_NAME = 'your-vnet-identifier'
LOCATION = 'region'
SUBNET_NAME = 'your-subnet-identifier'

network_client = NetworkManagementClient(credentials, 'your-subscription-id')

async_vnet_creation = network_client.virtual_networks.create_or_update(
    GROUP_NAME,
    VNET_NAME,
    {
        'location': LOCATION,
        'address_space': {
            'address_prefixes': ['10.0.0.0/16']
        }
    }
)
async_vnet_creation.wait()

# Create Subnet
async_subnet_creation = network_client.subnets.create_or_update(
    GROUP_NAME,
    VNET_NAME,
    SUBNET_NAME,
    {'address_prefix': '10.0.0.0/24'}
)
subnet_info = async_subnet_creation.result()
```

[!div class="nextstepaction"]
[Explore the management APIs]

### Samples

* [Getting started with Azure Resource Manager for load balancers in Python][1]

View the [complete list](https://azure.microsoft.com/en-us/resources/samples/?platform=python&term=virtual%20network) of Azure Virtual Network samples.

[1]: [https://azure.microsoft.com/en-us/resources/samples/network-python-manage-loadbalancer/]
