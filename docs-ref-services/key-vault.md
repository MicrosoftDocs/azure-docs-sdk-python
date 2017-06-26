---
title: Azure Key Vault libraries for Python
description: Reference documentation for the Python client libraries for Azure Key Vault
author: sptramer
keywords: Azure, Python, SDK, API, Keys, Key Vault, Authentication, Secret, key, security
manager: douge
ms.author: sttramer
ms.date: 06/26/2017
ms.topic: article
ms.devlang: python
ms.service: keyvault
---

# Overview

Azure Key Vault provides a way to securely store keys and other secrets used by applications in the cloud, with limited direct access.

For full details, see [What is Key Vault?](/azure/key-vault/key-vault-whatis)

## Install the libraries

```bash
pip install azure-keyvault
```

## Example

The following example creates an instance of a Key Vault client:

> [!IMPORTANT]
> You must specify resource=”https://vault.azure.net” while authenticating to get a valid token.

```python
from azure.keyvault import KeyVaultClient
from azure.common.credentials import UserPassCredentials

# See above for details on creating different types of AAD credentials
credentials = UserPassCredentials(
    'user@domain.com',  # Your user
    'my_password',      # Your password
    resource='https://vault.azure.net'
)

client = KeyVaultClient(
    credentials
)
```

For more information on creating a `Credentials` instance and using Azure Active Directory, see [Authenticate with the Azure Management Libraries for Python](/python/azure/python-sdk-azure-authenticate).

## Samples

| Key Vault ||
|--- | --- |
| [Recovery scenario samples for Azure Key Vault using the Azure Python SDK][1] | Demonstrates how to use the soft delete and backup restore features of Azure Key Vault to backup, restore, recover, and purge deleted vaults, secrets, keys, and certificates using the Azure Python SDK. |
| [Manage key vaults with Python][2] | Demonstrates how to manage key vaults with the Azure Python SDK.  |

Explore more [sample Python code](https://azure.microsoft.com/en-us/resources/samples/?platform=python) you can use in your apps.

[1]: https://azure.microsoft.com/en-us/resources/samples/key-vault-recovery-python/
[2]: https://azure.microsoft.com/en-us/resources/samples/key-vault-python-manage/