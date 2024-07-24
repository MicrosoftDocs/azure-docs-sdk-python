---
title: Azure Data Factory SDK for Python
description: Reference for Azure Data Factory SDK for Python
ms.date: 07/24/2024
ms.topic: reference
ms.devlang: python
ms.service: datafactory
---
# Azure Data Factory libraries for Python

Compose data storage, movement, and processing services into automated data pipelines with [Azure Data Factory](/azure/data-factory/)

[Learn more](/azure/data-factory/introduction) about Data Factory and get started with the [Create a data factory and pipeline using Python quickstart](/azure/data-factory/quickstart-create-data-factory-python). 

## Management module

Create and manage Data Factory instances in your subscription with the management module.

### Installation

Install the package with [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip install azure-mgmt-datafactory 
```

### Example 

Create a Data Factory in your subscription on the East US region.

```python
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *
import time

#Create a data factory
subscription_id = '<Specify your Azure Subscription ID>'
credentials = ServicePrincipalCredentials(client_id='<Active Directory application/client ID>', secret='<client secret>', tenant='<Active Directory tenant ID>')
adf_client = DataFactoryManagementClient(credentials, subscription_id)

rg_params = {'location':'eastus'}
df_params = {'location':'eastus'}  

df_resource = Factory(location='eastus')
df = adf_client.factories.create_or_update(rg_name, df_name, df_resource)
print_item(df)
while df.provisioning_state != 'Succeeded':
    df = adf_client.factories.get(rg_name, df_name)
    time.sleep(1)
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure-mgmt-datafactory)