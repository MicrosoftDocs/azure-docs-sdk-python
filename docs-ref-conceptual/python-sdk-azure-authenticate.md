---
title: Authenticate with the Azure management libraries for Python
description: Authenticate with a service principal into the Azure management libraries for Python
keywords: Azure, Python, SDK, API, authentication, active directory, service principal
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/13/2017
ms.topic: article
ms.technology: azure
ms.devlang: python
ms.service: multiple
ms.assetid: 
---

# Authenticate with the Azure Management Libraries for Python

## <a name="mgmt-auth"></a>Azure management libraries for Python authentication

Several options are available to authenticate your application with Azure when using the Python management libraries to create and manage resources.

### Authenticate with token credentials

Store the credentials securely in a configuration file, the registry, or Azure KeyVault. It is recommended to use [ADAL](https://github.com/AzureAD/azure-activedirectory-library-for-python)
and the SDK ADAL wrapper. Please refer to the ADAL website for all the available scenarios
list and samples.

The following example uses a [Service Principal](https://docs.microsoft.com/cli/azure/create-an-azure-service-principal-azure-cli?toc=%2fazure%2fazure-resource-manager%2ftoc.json) for authentication.

> [!NOTE]
> You can create a Service Principal via the Azure CLI 2.0
> ```bash
> az ad sp create-for-rbac --name "MY-PRINCIPAL-NAME" --password "STRONG-SECRET-PASSWORD"
> ```

```python
    import adal
    from msrestazure.azure_active_directory import AdalAuthentication
    from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD

    # Tenant ID for your Azure Subscription
    TENANT_ID = 'ABCDEFGH-1234-1234-1234-ABCDEFGHIJKL'

    # Your Service Principal App ID
    CLIENT = 'a2ab11af-01aa-4759-8345-7803287dbd39'

    # Your Service Principal Password
    KEY = 'password'

    LOGIN_ENDPOINT = AZURE_PUBLIC_CLOUD.endpoints.active_directory
    RESOURCE = AZURE_PUBLIC_CLOUD.endpoints.active_directory_resource_id

    context = adal.AuthenticationContext(LOGIN_ENDPOINT + '/' + TENANT_ID)
    credentials = AdalAuthentication(
        context.acquire_token_with_client_credentials,
        RESOURCE,
        CLIENT,
        KEY
    )
```

> [Note!]
> To connect to one of the Azure sovereign clouds, import the relevant cloud environment instead of `AZURE_PUBLIC_CLOUD`, e.g. `AZURE_CHINA_CLOUD` or `AZURE_GERMAN_CLOUD`.

All valid ADAL calls can be made with the `AdalAuthentication` class.

Next, create a client object to start working with the API:

```python
from azure.mgmt.compute import ComputeManagementClient

# Your Azure Subscription ID
subscription_id = '33333333-3333-3333-3333-333333333333'

client = ComputeManagementClient(credentials, subscription_id)
```

> [Note!]
> When using an Azure soverign cloud you must also specify the appropriate base URL (via the constants in `msrestazure.azure_cloud`) when creating the management client. For example for Azure China Cloud:
> ```python
> client = ComputeManagementClient(credentials, subscription_id,
      base_url=AZURE_CHINA_CLOUD.endpoints.active_directory_resource_id)
> ```

### CLI-based authentication

The SDK is able to create a client using your CLI active subscription.

> [!IMPORTANT]
> This should be used as quick start developer experience. For production purposes, use 
> [ADAL](#authenticate-with-token-credentials) or your own credentials system.
> Any change to your CLI configuration will impact the SDK execution.

To define active credentials, use [az login](https://docs.microsoft.com/cli/azure/authenticate-azure-cli).
Default subscription ID is either the only one you have, or you can define it using 
[az account](https://docs.microsoft.com/cli/azure/manage-azure-subscriptions-azure-cli)

```python
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient

client = get_client_from_cli_profile(ComputeManagementClient)
```

### Authenticate with token credentials (legacy)

In previous version of the SDK, ADAL was not yet available and only `UserPassCredentials` and `ServicePrincipalCredentials` classes were available. This is considered deprecated and should not be used anymore (for instance, these classes have no support for 
Germany or Government Azure).

This sample shows user/password scenario. This does not support 2FA.

```python
    from azure.common.credentials import UserPassCredentials

    credentials = UserPassCredentials(
        'user@domain.com',
        'my_smart_password',
    )
```

This sample shows Service Principal authentication.

```python
    from azure.common.credentials import ServicePrincipalCredentials

    credentials = ServicePrincipalCredentials(
        client_id = 'a2ab11af-01aa-4759-8345-7803287dbd39',
        secret = 'password',
        tenant = 'ABCDEFAB-1234-ABCD-1234-ABCDEFABCDEF'
    )
```