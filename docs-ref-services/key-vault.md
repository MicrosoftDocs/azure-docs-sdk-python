---
title: Azure Key Vault libraries for Python
description: Reference documentation for the Python client libraries for Azure Key Vault
author: sptramer
manager: carmonm
ms.author: sttramer
ms.date: 11/25/2019
ms.topic: conceptual
ms.devlang: python
ms.service: keyvault
---

# Azure Key Vault libraries for Python

[Azure Key Vault](/azure/key-vault/) is Azure's storage and management system for cryptographic keys, secrets, and certificate
management. The Python SDK API for Key Vault is split between client libraries and management libraries.

Use the following client libraries to:
- Create, store, and control access to the keys used to encrypt your data (azure-keyvault-keys)
- Securely store and control access to tokens, passwords, API keys, and other secrets (azure-keyvault-secrets)
- Create, manage, and deploy SSL/TLS certificates (azure-keyvault-certificates)

Use the management library to:
- Create, update, or delete new Key Vault stores
- Control vault access policies
- List vaults by subscription or resource group
- Check for vault name availability

## Install the libraries

### Client library

```bash
pip install azure-keyvault-secrets 
pip install azure-keyvault-keys
pip install azure-keyvault-certificates
pip install azure-identity
```

## Examples

Retrieve the public portion of an asymmetric key from a vault:

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient

credential = DefaultAzureCredential()

key_client = KeyClient("https://<vaultname>.vault.azure.net", credential)

//NOTE: please replace the ("<your-key-name>") with the name of your key in the vault 
key = key_client.get_key("<your-key-name>")
print(key.name)
```

Retrieve a secret from a vault:

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()

secret_client = SecretClient(vault_url="https://<vaultname>.vault.azure.net", credential=credential)

//NOTE: please replace the ("<your-secret-name>") with the name of the secret in your vault
secret = secret_client.get_secret("secret-name")

print(secret.name)
print(secret.value)

```
Find more details about latest packages [here](https://azure.github.io/azure-sdk/releases/latest/index.html).
Follow the link to the source code directory to find the latest key vault README, Change Log and Examples.

> [!div class="nextstepaction"]
> [Get Started with the Client APIs](/azure/key-vault/quick-create-python)

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
