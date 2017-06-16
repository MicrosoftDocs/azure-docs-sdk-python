---
title: Authenticate with the Azure management libraries for Python
description: Authenticate with a service principal into the Azure management libraries for Python
keywords: Azure, Python, SDK, API, authentication, active directory, service principal
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/13/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
ms.assetid: 
---

# Authenticate with the Azure Management Libraries for Python

## <a name="mgmt-auth"></a>Azure management libraries for Python authentication

Several options are available to authenticate your application with Azure when using the Python management libraries to create and manage resources.

### Authenticate with token credentials

The first method is to build the token credential object in code.  Store the credentials securely in a configuration file, the registry, or Azure KeyVault. It is recommended to use [ADAL](https://github.com/AzureAD/azure-activedirectory-library-for-python)
and the SDK ADAL wrapper. Please refer to the ADAL website for all the available scenarios
list and samples. For instance for service principal authentication:

```python
    import adal
    from msrestazure.azure_active_directory import AdalAuthentication

    login_endpoint = 'https://login.microsoftonline.com/'
    tenant = 'ABCDEFGH-1234-1234-1234-ABCDEFGHIJKL'
    resource = 'https://management.core.windows.net/' #AAD graph resource

    client = 'a2ab11af-01aa-4759-8345-7803287dbd39'
    key = 'password'

    context = adal.AuthenticationContext(LOGIN_ENDPOINT+TENANT)
    credentials = AdalAuthentication(
        context.acquire_token_with_client_credentials,
        resource,
        client,
        key
    )
```

All ADAL valid calls can be used with the `AdalAuthentication` class.

The `client`, `tenant` and `key` are the same service principal values used with [file-based authentication](#file-based-authentication).

Then create a client object to start working with the API:

```python
from azure.mgmt.compute import ComputeManagementClient

# change for your actual subscription id
subscription_id = '33333333-3333-3333-3333-333333333333'

client = ComputeManagementClient(credentials, subscription_id)
```

### File-based authentication

File-based authentication allows you to put the service principal credentials in a plain text file and secure it within the file system.

Create a text file named `azureauth.properties` using the service principal credentials:

```plaintext
# sample management library properties file
subscription=15dbcfa8-4b93-4c9a-881c-6189d39f04d4
client=a2ab11af-01aa-4759-8345-7803287dbd39
key=password
tenant=43413cc1-5886-4711-9804-8cfea3d1c3ee
managementURI=https://management.core.windows.net/
baseURL=https://management.azure.com/
authURL=https://login.windows.net/
graphURL=https://graph.windows.net/
```

Save this file in a secure location on your system where your code can read it. Set an environment variable named `AZURE_AUTH_LOCATION` with the full path to the file, for example:

```bash
export "AZURE_AUTH_LOCATION"="~/.azure/azureauth.properties"
```

Read the contents of the file and create a client object to start working with the API:

```python
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.compute import ComputeManagementClient

client = get_client_from_auth_file(ComputeManagementClient)
```

You can also specifiy the path to the file if you do not want to use an environment variable.

```python
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.compute import ComputeManagementClient

client = get_client_from_auth_file(ComputeManagementClient, '/opt/prod/azureauth.properties')
```

### CLI-based authentication

The SDK is able to create a client using your CLI active subscription.

> [!IMPORTANT]
> This should be used as quick start developer experience. For production purpose use 
> [file-based authentication](#file-based-authentication) or your own credentials system.
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