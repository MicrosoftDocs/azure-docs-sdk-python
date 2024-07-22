---
title: Azure Resources SDK for Python
description: Reference for Azure Resources SDK for Python
ms.date: 07/22/2024
ms.topic: reference
ms.devlang: python
ms.service: resources
---
# Azure Resources libraries for python

## Overview 
Deploy, monitor, and manage resources in groups with [Azure Resource Manager](https://docs.microsoft.com/azure/azure-resource-manager/resource-group-overview).

## Management API
Use the management API to create resource groups and deploy resources from templates.

```bash
pip install azure-mgmt-resource
```
### Example 
Create a new resource group in the Azure Eastern US region.

```python
from azure.mgmt.resource import ResourceManagementClient

LOCATION = 'eastus'
GROUP_NAME ='sample_resource_group'

resource_client = ResourceManagementClient(credentials, subscription_id)
resource_client.resource_groups.create_or_update(GROUP_NAME, {'location': LOCATION})
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/azure.mgmt.resource)

## Samples
[Manage Azure resources and resource groups](https://github.com/Azure-Samples/resource-manager-python-resources-and-groups)

View the [complete list](https://azure.microsoft.com/resources/samples/?platform=python&term=resource) of Azure Resource Manager samples.