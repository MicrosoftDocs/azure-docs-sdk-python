---
title: Azure Key Vault libraries for Python
description: Reference documentation for the Python client libraries for Azure Key Vault
author: lisawong19
keywords: Azure, Python, SDK, API, Keys, Key Vault, Authentication, Secret, key, security
manager: douge
ms.author: liwong
ms.date: 07/18/2017
ms.topic: article
ms.devlang: python
ms.service: keyvault
---
# Azure Key Vault libraries for Python

## Overview

Create, update, and delete keys and secrets in Azure Key Vault with the client libraries.

Use the Azure Key Vault management libraries to create key vaults, authorize applications, and manage permissions. 

Learn more about [Azure Key Vault](/azure/key-vault/key-vault-whatis).

## Install the libraries

### Client library
```bash
pip install azure-keyvault
```

## Example
Retrieve a [JSON web key](https://tools.ietf.org/html/draft-ietf-jose-json-web-key-18) from a Key Vault.

```python
from azure.keyvault import KeyVaultClient

client = KeyVaultClient(credentials, subscription_id)
key_bundle = client.get_key(vault_url, key_name, key_version)
json_key = key_bundle.key
```

### Management API
```bash
pip install azure-mgmt-keyvault
```
> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure.mgmt.keyvault)

### Example
The following example shows how to create an Azure Key Vault. 

```python
from azure.mgmt.keyvault import KeyVaultManagementClient

GROUP_NAME = 'your_resource_group_name'
KV_NAME = 'your_key_vault_name'
#The object ID of the User or Application for access policies. Find this number in the portal
OBJECT_ID = '00000000-0000-0000-0000-000000000000'

kv_client = KeyVaultManagementClient(credentials, subscription_id)

vault = kv_client.vaults.create_or_update(
    GROUP_NAME,
    KV_NAME,
    {
        'location': 'eastus',
        'properties': {
            'sku': {
                'name': 'standard'
            },
            'tenant_id': os.environ['AZURE_TENANT_ID'],
            'access_policies': [{
                'tenant_id': os.environ['AZURE_TENANT_ID'],
                'object_id': OBJECT_ID,
                'permissions': {
                    'keys': ['all'],
                    'secrets': ['all']
                }
            }]
        }
    }
)
```

## Samples
* [Manage Key Vaults][1] 
* [Key Vault recovery][2]

[1]: https://azure.microsoft.com/resources/samples/key-vault-python-manage/
[2]: https://azure.microsoft.com/resources/samples/key-vault-recovery-python/

View the [complete list](https://azure.microsoft.com/resources/samples/?platform=python&term=key+vault) of Azure Key Vault samples. 