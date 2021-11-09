---
title: Azure Resources libraries for Python
description: 
keywords: Azure, Python, SDK, API, Resources
author: lisawong19
ms.author: ramyar
manager: douge
ms.date: 06/19/2017
ms.topic: reference
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: resources
---
# Azure Resources libraries for Python 

## Overview 
Manage Azure resources in resource groups.

| Package  |  Description |
|---|---|
|[azure.mgmt.resource.features][1]|Azure Feature Exposure Control (AFEC) provides a mechanism for the resource providers to control feature exposure to users.|
|[azure.mgmt.resource.links][2]|Azure resources can be linked together to form logical relationships. You can establish links between resources belonging to different resource groups.|
|[azure.mgmt.resource.locks][3]|Azure resources can be locked to prevent other users in your organization from deleting or modifying resources.|
|[azure.mgmt.resource.managedapplications][4]|ARM managed applications (appliances).|
|[azure.mgmt.resource.policy][5]|To manage and control access to your resources, you can define customized policies and assign them at a scope.|
|[azure.mgmt.resource.resources][6]| Provides operations for working with resources and resource groups.|
|[azure.mgmt.resource.subscriptions][7]|All resource groups and resources exist within subscriptions. These operation enable you get information about your subscriptions and tenants.|

[1]: /python/api/azure.mgmt.resource.features
[2]: /python/api/azure.mgmt.resource.links
[3]: /python/api/azure.mgmt.resource.locks
[4]: /python/api/azure.mgmt.resource.managedapplications
[5]: /python/api/azure.mgmt.resource.policy
[6]: /python/api/azure.mgmt.resource.resources
[7]: /python/api/azure.mgmt.resource.subscriptions

## Install the libraries 
```bash
pip install azure-mgmt-resource
```

## Example
The following is an example of how to create a resource group. 

```python
from azure.mgmt.resource import ResourceManagementClient
client = ResourceManagementClient(credentials, subscription_id)
client.resource_groups.create(RESOURCE_GROUP_NAME, {'location':'eastus'})
```

Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps. 
