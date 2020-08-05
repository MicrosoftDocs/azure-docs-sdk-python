---
title: Azure Key Vault libraries for Python
description: Reference documentation for the Python client libraries for Azure Key Vault
author: sptramer
manager: carmonm
ms.author: sttramer
ms.date: 11/25/2019
ms.topic: conceptual
ms.devlang: python
ms.service: key-vault
---

# Azure Key Vault libraries for Python

The Azure Key Vault client libraries for Python offer a convenient interface for making calls to Azure Key Vault. For more information about Azure Key Vault, see [Introduction to Azure Key Vault](https://docs.microsoft.com/azure/key-vault/general/overview).

## Libraries for data access

The latest version of the Azure Key Vault libraries is version 4.x.x. Microsoft recommends using version 4.x.x for new applications.

If you cannot update existing applications to version 4.x.x, then Microsoft recommends using version 1.x.x.

### Version 4.x.x

The version 4.x.x client libraries for Python are part of the Azure SDK for Python. The source code for the Azure Key Vault client libraries for Python is available on [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault).

Use the following version 4.x.x libraries to work with certificates, keys, and secrets:

| Library | Reference | Package | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    azure-keyvault-certificates   |    [Reference](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-keyvault-certificates/4.1.0/azure.keyvault.certificates.html)    |    [PyPI](https://pypi.org/project/azure-keyvault-certificates/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-certificates)    |
|    azure-keyvault-keys    |    [Reference](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-keyvault-keys/4.1.0/azure.keyvault.keys.html)    |    [PyPI](https://pypi.org/project/azure-keyvault-keys/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-keys)    |
|    azure-keyvault-secrets    |    [Reference](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-keyvault-secrets/4.1.0/azure.keyvault.secrets.html)    |    [PyPI](https://pypi.org/project/azure-keyvault-secrets/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets)    |

### Version 1.x.x

The source code for the Azure Key Vault client libraries for Python is available on [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/azure-keyvault_1.1.0/azure-keyvault).

Use the following version 1.x.x libraries to work with certificates, keys, and secrets:

| Library | Reference | Package | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    azure-keyvault   |    [Reference](https://docs.microsoft.com/python/api/overview/azure/keyvault?view=azure-python-previous)    |    [PyPI](https://pypi.org/project/azure-keyvault/1.1.0/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/azure-keyvault_1.1.0/azure-keyvault)    |

## Libraries for resource management

Use the following library to work with the Azure Key Vault resource provider:

|    Library    |    Reference    |    Package    |    Source    |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|    azure-mgmt-keyvault    |    [Reference](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-mgmt-keyvault/2.2.0/azure.mgmt.keyvault.html)    |    [PyPI](https://pypi.org/project/azure-mgmt-keyvault/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-mgmt-keyvault)    |
