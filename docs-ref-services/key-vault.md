---
title: Azure Key Vault libraries for Python
description: Reference documentation for the Python client libraries for Azure Key Vault
author: lisawong19
keywords: Azure, Python, SDK, API, Keys, Key Vault, Authentication, Secret, key, security
manager: douge
ms.author: liwong
ms.date: 06/26/2017
ms.topic: article
ms.devlang: python
ms.service: keyvault
---

# Overview

Create, update, and delete keys and secrets in Azure Key Vault with the client libraries.

Use the Azure Key Vault management libraries to create key vaults, authorize applications, and manage permissions. 

Learn more about [Azure Key Vault](/azure/key-vault/key-vault-whatis).

## Install the libraries

### Client library

```bash
pip install azure-keyvault
```

### Management 

```bash
pip install azure-mgmt-keyvault
```

## Example

Retrieve a [JSON web key](https://tools.ietf.org/html/draft-ietf-jose-json-web-key-18) from a Key Vault.

```python
client = KeyVaultClient(credentials)

key_bundle = client.get_key(vault_url, key_name, key_version)
json_key = key_bundle.key
```

## Samples

| Key Vault ||
|--- | --- |
| [Manage Key Vaults][1] | Create and delete a key vault.  |
| [Key Vault recovery][2] | Use the soft delete and backup restore features of Azure Key Vault to backup, restore, recover, and purge deleted vaults, secrets, keys, and certificates. |

[1]: https://azure.microsoft.com/resources/samples/key-vault-python-manage/
[2]: https://azure.microsoft.com/resources/samples/key-vault-recovery-python/

Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.