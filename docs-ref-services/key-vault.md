---
title: Azure Key Vault libraries for Python
description: Reference documentation for the Python client libraries for Azure Key Vault
author: kraigb
manager: barbkess
ms.author: kraigb
ms.date: 03/10/2020
ms.topic: conceptual
ms.devlang: python
ms.service: keyvault
---

# Azure Key Vault libraries for Python

[Azure Key Vault](/azure/key-vault/) provides secure cloud storage on Azure for cryptographic keys, secrets, and certificates. The Python SDK API for Key Vault provides both management and client libraries.

Use the management library to:

- Create, update, or delete new Key Vault stores
- Control vault access policies
- List vaults by subscription or resource group
- Check for vault name availability

Use the client library to:

- Access, update, or delete items stored in an Azure Key Vault
- Get metadata for stored certificates
- Verify signatures against symmetric keys in Key Vault

Also see [Azure Key Vault samples for Python](/samples/browse/?products=azure-key-vault&languages=python).

## Management library

Install the management library with `pip install azure-mgmt-keyvault`, along with the identity library with `pip install azure-identity`.

To manage a key vault, an application must first authenticate with the Key Vault service. Authentication is best done using [Azure Managed Identities](/azure/active-directory/managed-identities-azure-resources/overview) (part of Azure Active Directory), and can also also be done with a service principal.

To use Managed Identities, acquire a `DefaultAzureCredential` object as shown in the following code. (To run this code on a developer workstation, see [Using Managed Identities locally](using-managed-identities-locally)).

```python
from azure.identity import DefaultAzureCredential

# Acquire default Azure credentials, which are useful in most circumstances.
credentials = DefaultAzureCredential()
```

To use a service principal, acquire a `ServicePrincipalCredential` object as shown in the following code. Review [Authenticate with the Azure SDK for Python](/azure/python/python-sdk-azure-authenticate) for information on creating a service principal and obtaining a tenant ID, a client ID, and application (or client) secret using the `az ad sp create-for-rbac --sdk-auth` command.

To find the object ID for the service principal, go to the [Azure portal](https://portal.azure.com), navigate to your subscription, select **Access Control (IAM)**, select **Role assignments**, and locate the appropriate service principal. Select that service principal to open it, then find the object ID on the **Overview** page.

```python
from azure.common.credentials import ServicePrincipalCredentials

# Replace the values with your specific IDs
client_id = "your_client_id"
tenant_id = "your_tenant_id"
app_secret = "your_app_secret"

credentials = ServicePrincipalCredentials(client_id=client_id, secret=app_secret, tenant=tenant_id)
```

With the `credentials` variable initialized, you can then use the following code to create an Azure Key Vault named `msdocs-vault01` in an *existing* resource group named `KeyVault-rg`. With the Key Vault in place, you can then use the [client library](#client-library) to create, retrieve, and delete items.

```python
# You can place this import statement earlier in your code.
from azure.mgmt.keyvault import KeyVaultManagementClient

# The Azure subscription to use. NOTE: hard-coding such an ID is not recommended and is
# shown here for demonstration purposes only. In production code, use an environment
# variable or other means to store and retrieve the ID.
subscription_id = 'your_subscription_id'

client = KeyVaultManagementClient(credentials, subscription_id)

# The object ID and organization ID (tenant) of the user, application, or service principal for access policies.
# These values can be found through the Azure CLI, Azure PowerShell, or the Azure portal.
allow_object_id = "your_object_id"
allow_tenant_id = tenant_id

# The resource group in which to create the vault, which must already exist.
# This example uses "KeyVault-rg".
resource_group = "KeyVault-rg"

# The name of the key vault to create. This example uses "msdocs-vault01".
vault_name = "msdocs-vault01"

# You can change the location from eastus to any other suitable location. Vault properties
# may also be created by using the azure.mgmt.keyvault.models.VaultCreateOrUpdateParameters
# class, rather than a map.
operation = client.vaults.create_or_update(
    resource_group,
    vault_name,
    {
        'location': 'eastus',
        'properties': {
            'sku': {
                'name': 'standard'
            },
            'tenant_id': allow_tenant_id,
            'access_policies': [{
                'object_id': allow_object_id,
                'tenant_id': allow_tenant_id,
                'permissions': {
                    'keys': ['all'],
                    'secrets': ['all']
                }
            }]
        }
    }
)

# Run the operation
vault = operation.result()

# Show the URL of the created vault
print(f'New vault URI: {vault.properties.vault_uri}')
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/keyvault/management)

## Client library

Install the library with `pip install azure-keyvault`.

To access a key vault, an application must first authenticate with the Key Vault service. Authentication is best done using [Azure Managed Identities](/azure/active-directory/managed-identities-azure-resources/overview) (part of Azure Active Directory), and can also also be done with a service principal.

To use Managed Identities, acquire a `DefaultAzureCredential` object. (To run this code on a developer workstation, see [Using Managed Identities locally](using-managed-identities-locally)).

```python
from azure.identity import DefaultAzureCredential

# Acquire default Azure credentials, which are useful in most circumstances.
credentials = DefaultAzureCredential()
```

To use a service principal, acquire a `ServicePrincipalCredential` object. Review [Authenticate with the Azure SDK for Python](/azure/python/python-sdk-azure-authenticate) for information on obtaining a tenant ID, a client ID, and application secret.

```python
from azure.common.credentials import ServicePrincipalCredentials

# Replace the values with your specific IDs
client_id = "your_client_id"
tenant_id = "your_tenant_id"
app_secret = "your_app_secret"

credentials = ServicePrincipalCredentials(client_id, app_secret, tenant_id)
```

With the `credentials` variable initialized, you can then use the following code to create a secret named `ExampleSecret` in an Azure Key Vault named `msdocs-vault01` (as created using the code in the [management library](#management-library) section.

```python
# You can place this import statement earlier in your code.
from azure.keyvault.secrets import SecretClient

# The URL of your Key Vault obtained from the Azure portal, which ends in vault.azure.net.
# This example uses https://msdocs-vault01.vault.azure.net/
key_vault_uri = "https://msdocs-vault01.vault.azure.net/"

# Obtain the client object
secret_client = SecretClient(key_vault_uri, credentials)

# Create a secret. In production code deployed to a public server, such values
# would not appear in source code.
secret_name = "ExampleSecret"
secret_client.set_secret(secret_name, "value5502")
```

The `set_secret` method updates the value if the secret already exists.

Use the same `SecretClient` object to retrieve the secret value:

```python
secret = secret_client.get_secret(secret_name)
```

To delete the secret:

```python
client.begin_delete_secret(secret_name)
```

> [!div class="nextstepaction"]
> [Explore the Client APIs](/python/api/overview/azure/keyvault/client)

## Using Managed Identities locally

Managed Identities are a feature of Azure hosting environments and are not inherently available on local developer workstations. As a result, attempting to run code that uses `DefaultAzureCredential` may produce the following error:

<pre>
No credential in this chain provided a token.
Attempted credentials:
        EnvironmentCredential: Incomplete environment configuration
        ImdsCredential: IMDS endpoint unavailable
        SharedTokenCacheCredential: The shared cache contains no signed-in accounts. To authenticate with SharedTokenCacheCredential, login through developer tooling supporting Azure single sign on
</pre>

There are two options to run the code locally:

- Use a developer tool, like Visual Studio, that supports a single sign-on experience for Azure and therefore provides a SharedTokenCacheCredential.

- Configure a local service principal and create environment variables to provide the EnvironmentCredential:

    1. Install the [Azure CLI](/cli/azure/install-azure-cli?view=azure-cli-latest) if you don't have it installed already.

    1. In a terminal or command prompt, create a service principle using the Azure CLI [az ad sp create-for-rbac](/cli/azure/ad/sp?view=azure-cli-latest#az-ad-sp-create-for-rbac) command:

        ```azurecli
        az ad sp create-for-rbac --skip-assignment
        ```

        The command returns a JSON object similar to the following (your values will differ):

        <pre>
        {
          "appId": "8a1f0000-97c0-4f78-a750-9cb0000c81f9",
          "displayName": "azure-cli-2020-03-10-16-38-58",
          "name": "http://azure-cli-2020-03-10-16-38-58",
          "password": "05000052-3d77-4def-a457-53f428744af9",
          "tenant": "58efb1eb-d777-46f6-9479-0000a50bf2f3"
        }
        </pre>

    1. Create the following environment variables using values from the JSON:

        | Variable name | Value from create-for-rbac output |
        | `AZURE_CLIENT_ID` | `appId` |
        | `AZURE_CLIENT_SECRET` | `password` |
        | `AZURE_TENANT_ID` | `tenant` |

    1. Grant the service principal access to the key vault, replacing `<your-resource-group>` with resource group containing your key vault, `<your-keyvault-name>` with the name of the Key Vault, and `<client-id>` with the `appID` value from the previous JSON output:

        ```azurecli
        az keyvault set-policy -g <your-resource-group> -n <your-keyvault-name> --spn <your-clientId> --secret-permissions delete get list set --key-permissions create decrypt delete encrypt get list unwrapKey wrapKey
        ```

        When using the management APIs, this command obviously requires that the key vault already exists. In that case, you must create the key vault using the [Azure CLI](/azure/key-vault/quick-create-cli), [Azure PowerShell](/azure/key-vault/quick-create-powershell), or the [Azure Portal](/azure/key-vault/quick-create-portal) instead. You can then perform other management tasks through code.

    1. Using `DefaultAzureCredential` should now work. If the EnvironmentCredential error still appears, check your environment variables. If you encounter the error, "(Forbidden) Access denied. Caller was not found on any access policy.", check the arguments you gave to the `az keyvault set-policy` command.

## Samples

[Azure Key Vault samples for Python](/samples/browse/?products=azure-key-vault&languages=python)
