---
title: Azure Key Vault libraries for Python
description: Reference documentation for the Python client libraries for Azure Key Vault
author: sptramer
manager: carmonm
ms.author: sttramer
ms.date: 06/10/2019
ms.topic: conceptual
ms.devlang: python
ms.service: key-vault
---

# Azure Key Vault libraries for Python

[Azure Key Vault](/azure/key-vault/) is Azure's storage and management system for cryptographic keys, secrets, and certificate
management. The Python SDK API for Key Vault is split between client libraries and management libraries.

Use the client library to:
- Access, update, or delete items stored in an Azure Key Vault
- Get metadata for stored certificates
- Verify signatures against symmetric keys in Key Vault

Use the management library to:
- Create, update, or delete new Key Vault stores
- Control vault access policies
- List vaults by subscription or resource group
- Check for vault name availability

## Install the libraries

### Client library

```bash
pip install azure-keyvault
```

## Examples

The following examples use service principal authentication, which is the recommended sign in method
for applications that connect to Azure. To learn about service principal authentication, see
[Authenticate with the Azure SDK for Python](https://docs.microsoft.com/en-us/python/azure/python-sdk-azure-authenticate)

Retrieve the public portion of an asymmetric key from a vault:

```python
from azure.keyvault import KeyVaultClient
from azure.common.credentials import ServicePrincipalCredentials

credentials = ServicePrincipalCredentials(
    client_id = '...',
    secret = '...',
    tenant = '...'
)

client = KeyVaultClient(credentials)

# VAULT_URL must be in the format 'https://<vaultname>.vault.azure.net'
# KEY_VERSION is required, and can be obtained with the KeyVaultClient.get_key_versions(self, vault_url, key_name) API
key_bundle = client.get_key(VAULT_URL, KEY_NAME, KEY_VERSION)
key = key_bundle.key
```

Retrieve a secret from a vault:

```python
from azure.keyvault import KeyVaultClient
from azure.common.credentials import ServicePrincipalCredentials

credentials = ServicePrincipalCredentials(
    client_id = '...',
    secret = '...',
    tenant = '...'
)

client = KeyVaultClient(credentials)

# VAULT_URL must be in the format 'https://<vaultname>.vault.azure.net'
# SECRET_VERSION is required, and can be obtained with the KeyVaultClient.get_secret_versions(self, vault_url, secret_id) API
secret_bundle = client.get_secret(VAULT_URL, SECRET_ID, SECRET_VERSION)
secret = secret_bundle.value
```

> [!div class="nextstepaction"]
> [Explore the Client APIs](/python/api/overview/azure/keyvault/client)

### Management library

```bash
pip install azure-mgmt-keyvault
```

### Example

The following example shows how to create an Azure Key Vault. 

```python
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.common.credentials import ServicePrincipalCredentials


credentials = ServicePrincipalCredentials(
    client_id = '...',
    secret = '...',
    tenant = '...'
)

# Even when using service principal credentials, a subscription ID is required. For service principals,
# this should be the subscription used to create the service principal. Storing a token like a valid
# subscription ID in code is not recommended and only shown here for example purposes.
SUBSCRIPTION_ID = '...'
client = KeyVaultManagementClient(credentials, SUBSCRIPTION_ID)

# The object ID and organization ID (tenant) of the user, application, or service principal for access policies.
# These values can be found through the Azure CLI or the Portal.
ALLOW_OBJECT_ID = '...'
ALLOW_TENANT_ID = '...'

RESOURCE_GROUP = '...'
VAULT_NAME = '...'

# Vault properties may also be created by using the azure.mgmt.keyvault.models.VaultCreateOrUpdateParameters
# class, rather than a map. 
operation = client.vaults.create_or_update(
    RESOURCE_GROUP,
    VAULT_NAME,
    {
        'location': 'eastus',
        'properties': {
            'sku': {
                'name': 'standard'
            },
            'tenant_id': ALLOW_TENANT_ID,
            'access_policies': [{
                'object_id': ALLOW_OBJECT_ID,
                'tenant_id': ALLOW_TENANT_ID,
                'permissions': {
                    'keys': ['all'],
                    'secrets': ['all']
                }
            }]
        }
    }
)

vault = operation.result()
print(f'New vault URI: {vault.properties.vault_uri}')
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/keyvault/management)

## Samples
* [Manage Azure Key Vaults][1] 
* [Azure Key Vault recovery][2]

[1]: https://azure.microsoft.com/resources/samples/key-vault-python-manage/
[2]: https://azure.microsoft.com/resources/samples/key-vault-recovery-python/

View the [complete list](https://azure.microsoft.com/resources/samples/?platform=python&term=key+vault) of Azure Key Vault samples. 
