---
title: Azure Key Vault SDK for Python
description: Reference for Azure Key Vault SDK for Python
ms.date: 07/26/2024
ms.topic: reference
ms.devlang: python
ms.service: keyvault
manager: carmonm
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
|    azure-keyvault-certificates   |    [Reference](keyvault-certificates-readme)    |    [PyPI](https://pypi.org/project/azure-keyvault-certificates/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-certificates)    |
|    azure-keyvault-keys    |    [Reference](keyvault-keys-readme)    |    [PyPI](https://pypi.org/project/azure-keyvault-keys/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-keys)    |
|    azure-keyvault-secrets    |    [Reference](keyvault-secrets-readme)    |    [PyPI](https://pypi.org/project/azure-keyvault-secrets/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets)    |

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
|    azure-mgmt-keyvault    |    [Reference](/python/api/overview/azure/mgmt-keyvault-readme)    |    [PyPI](https://pypi.org/project/azure-mgmt-keyvault/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-mgmt-keyvault)    |