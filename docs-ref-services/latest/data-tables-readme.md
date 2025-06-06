---
title: Azure Tables client library for Python
keywords: Azure, python, SDK, API, azure-data-tables, tables
ms.date: 05/06/2025
ms.topic: reference
ms.devlang: python
ms.service: tables
---
# Azure Tables client library for Python - version 12.7.0 


Azure Tables is a NoSQL data storage service that can be accessed from anywhere in the world via authenticated calls using HTTP or HTTPS.
Tables scales as needed to support the amount of data inserted, and allow for the storing of data with non-complex accessing.
The Azure Tables client can be used to access Azure Storage or Cosmos accounts. This document covers [`azure-data-tables`][Tables_pypi].

Please note, this package is a replacement for [`azure-cosmosdb-tables`](https://github.com/Azure/azure-cosmos-table-python/tree/master/azure-cosmosdb-table) which is now deprecated. See the [migration guide][migration_guide] for more details.

[Source code][source_code]
| [Package (PyPI)][Tables_pypi]
| [Package (Conda)](https://anaconda.org/microsoft/azure-data-tables/)
| [API reference documentation][Tables_ref_docs]
| [Samples][Tables_samples]

## Getting started
The Azure Tables SDK can access an Azure Storage or CosmosDB account.

### Prerequisites
* Python 3.9 or later is required to use this package.
* You must have an [Azure subscription][azure_subscription] and either
    * an [Azure Storage account][azure_storage_account] or
    * an [Azure Cosmos Account][azure_cosmos_account].

#### Create account
* To create a new storage account, you can use [Azure Portal][azure_portal_create_account], [Azure PowerShell][azure_powershell_create_account], or [Azure CLI][azure_cli_create_account]:
* To create a new cosmos storage account, you can use the [Azure CLI][azure_cli_create_cosmos] or [Azure Portal][azure_portal_create_cosmos].

### Install the package
Install the Azure Tables client library for Python with [pip][pip_link]:
```bash
pip install azure-data-tables
```

#### Create the client
The Azure Tables library allows you to interact with two types of resources:
* the tables in your account
* the entities within those tables.
Interaction with these resources starts with an instance of a [client](#clients). To create a client object, you will need the account's table service endpoint URL and a credential that allows you to access the account. The `endpoint` can be found on the page for your storage account in the [Azure Portal][azure_portal_account_url] under the "Access Keys" section or by running the following Azure CLI command:

```bash
# Get the table service URL for the account
az storage account show -n mystorageaccount -g MyResourceGroup --query "primaryEndpoints.table"
```

Once you have the account URL, it can be used to create the service client:
```python
from azure.data.tables import TableServiceClient
service = TableServiceClient(endpoint="https://<my_account_name>.table.core.windows.net/", credential=credential)
```

For more information about table service URL's and how to configure custom domain names for Azure Storage check out the [official documentation][azure_portal_account_url]

#### Types of credentials
The `credential` parameter may be provided in a number of different forms, depending on the type of authorization you wish to use. The Tables library supports the following authorizations:
* Shared Key
* Connection String
* Shared Access Signature Token
* TokenCredential (Microsoft Entra ID)(Supported on Storage)

##### Creating the client from a shared key
To use an account [shared key][azure_shared_key] (aka account key or access key), provide the key as a string. This can be found in your storage account in the [Azure Portal][azure_portal_account_url] under the "Access Keys" section or by running the following Azure CLI command:

```bash
az storage account keys list -g MyResourceGroup -n MyStorageAccount
```

Use the key as the credential parameter to authenticate the client:

```python
from azure.data.tables import TableServiceClient
from azure.core.credentials import AzureNamedKeyCredential

credential = AzureNamedKeyCredential("my_account_name", "my_access_key")
with TableServiceClient(
    endpoint="https://<my_account_name>.table.core.windows.net", credential=credential
) as table_service_client:
    properties = table_service_client.get_service_properties()
    print(f"{properties}")
```

##### Creating the client from a connection string
Depending on your use case and authorization method, you may prefer to initialize a client instance with a connection string instead of providing the account URL and credential separately. To do this, pass the connection string to the client's `from_connection_string` class method. If the connection string does not specify a fully qualified endpoint URL (`"TableEndpoint"`), or URL suffix (`"EndpointSuffix"`), the endpoint will be assumed to be an Azure Storage account, and the URL automatically formatted accordingly.

For Tables Storage, the connection string can be found in your storage account in the [Azure Portal][azure_portal_account_url] under the "Access Keys" section or with the following Azure CLI command:

```bash
az storage account show-connection-string -g MyResourceGroup -n MyStorageAccount
```

For Tables Cosmos, the connection string can be found in your cosmos account in the [Azure Portal][azure_portal_account_url] under the "Connection Strings" section or with the following Azure CLI command:

```bash
az cosmosdb list-connection-strings -g MyResourceGroup -n MyCosmosAccount
```

Create a client from a connection string:

```python
from azure.data.tables import TableServiceClient

connection_string = "AccountName=<my_account_name>;AccountKey=<my_account_key>;EndpointSuffix=<endpoint_suffix>"
with TableServiceClient.from_connection_string(conn_str=connection_string) as table_service_client:
    properties = table_service_client.get_service_properties()
    print(f"{properties}")
```

##### Creating the client from a SAS token
To use a [shared access signature (SAS) token][azure_sas_token], provide the token as a string. If your account URL includes the SAS token, omit the credential parameter. You can generate a SAS token from the Azure Portal under [Shared access signature](https://learn.microsoft.com/rest/api/storageservices/create-service-sas) or use one of the `generate_*_sas()` functions to create a sas token for the account or table:

```python
from datetime import datetime, timedelta
from azure.data.tables import TableServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions
from azure.core.credentials import AzureNamedKeyCredential, AzureSasCredential

credential = AzureNamedKeyCredential("my_account_name", "my_access_key")
# Create a SAS token to use for authentication of a client
sas_token = generate_account_sas(
    credential,
    resource_types=ResourceTypes(service=True),
    permission=AccountSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=1),
)

with TableServiceClient(
    endpoint="https://<my_account_name>.table.core.windows.net", credential=AzureSasCredential(sas_token)
) as table_service_client:
    properties = table_service_client.get_service_properties()
    print(f"{properties}")
```

##### Creating the client from a TokenCredential

Azure Tables provides integration with Microsoft Entra ID for identity-based authentication of requests to the Table service when targeting a Storage endpoint. With Microsoft Entra ID, you can use role-based access control (RBAC) to grant access to your Azure Table resources to users, groups, or applications.

To access a table resource with a TokenCredential, the authenticated identity should have either the "Storage Table Data Contributor" or "Storage Table Data Reader" role.

With the `azure-identity` package, you can seamlessly authorize requests in both development and production environments. To learn more about Microsoft Entra ID integration in Azure Storage, see the [azure-identity README](https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/identity/azure-identity/README.md)

```python
from azure.data.tables import TableServiceClient
from azure.identity import DefaultAzureCredential

with TableServiceClient(
    endpoint="https://<my_account_name>.table.core.windows.net", credential=DefaultAzureCredential()
) as table_service_client:
    properties = table_service_client.get_service_properties()
    print(f"{properties}")
```

###### Configure client for an Azure sovereign cloud

When TokenCredential authentication is used, all clients are configured to use the Azure public cloud by default. To configure a client for a sovereign cloud, you should provide the correct `audience` keyword argument when creating the client. The following table lists some known audiences:

| Cloud | Audience |
|-------|----------|
| Azure Public | https://storage.azure.com / https://cosmos.azure.com |
| Azure US Government | https://storage.azure.us / https://cosmos.azure.us |
| Azure China | https://storage.chinacloudapi.cn / https://cosmos.chinacloudapi.cn |

The following example shows how to configure the `TableServiceClient` to connect to Azure US Government:

```python
from azure.data.tables import TableServiceClient
from azure.identity import AzureAuthorityHosts, DefaultAzureCredential

# Authority can also be set via the AZURE_AUTHORITY_HOST environment variable.
credential = DefaultAzureCredential(authority=AzureAuthorityHosts.AZURE_GOVERNMENT)

table_service_client = TableServiceClient(
    endpoint="https://<my_account_name>.table.core.usgovcloudapi.net",
    credential=credential,
    audience="https://storage.azure.us"
)
```


## Key concepts
Common uses of the Table service included:
* Storing TBs of structured data capable of serving web scale applications
* Storing datasets that do not require complex joins, foreign keys, or stored procedures and can be de-normalized for fast access
* Quickly querying data using a clustered index
* Accessing data using the OData protocol and LINQ filter expressions

[comment]: # ( cspell:ignore LINQ )

The following components make up the Azure Tables Service:
* The account
* A table within the account, which contains a set of entities
* An entity within a table, as a dictionary

The Azure Tables client library for Python allows you to interact with each of these components through the
use of a dedicated client object.

### Clients
Two different clients are provided to interact with the various components of the Table Service:
1. **`TableServiceClient`** -
    * Get and set account setting
    * Query, create, and delete tables within the account.
    * Get a `TableClient` to access a specific table using the `get_table_client` method.
2. **`TableClient`** -
    * Interacts with a specific table (which need not exist yet).
    * Create, delete, query, and upsert entities within the specified table.
    * Create or delete the specified table itself.

### Entities
Entities are similar to rows. An entity has a **`PartitionKey`**, a **`RowKey`**, and a set of properties. A property is a name value pair, similar to a column. Every entity in a table does not need to have the same properties. Entities can be represented as dictionaries like this as an example:
```python
entity = {
    'PartitionKey': 'color',
    'RowKey': 'brand',
    'text': 'Marker',
    'color': 'Purple',
    'price': '5'
}
```
* **[create_entity][create_entity]** - Add an entity to the table.
* **[delete_entity][delete_entity]** - Delete an entity from the table.
* **[update_entity][update_entity]** - Update an entity's information by either merging or replacing the existing entity.
    * `UpdateMode.MERGE` will add new properties to an existing entity it will not delete an existing properties
    * `UpdateMode.REPLACE` will replace the existing entity with the given one, deleting any existing properties not included in the submitted entity
* **[query_entities][query_entities]** - Query existing entities in a table using [OData filters][odata_syntax].
* **[get_entity][get_entity]** - Get a specific entity from a table by partition and row key.
* **[upsert_entity][upsert_entity]** - Merge or replace an entity in a table, or if the entity does not exist, inserts the entity.
    * `UpdateMode.MERGE` will add new properties to an existing entity it will not delete an existing properties
    * `UpdateMode.REPLACE` will replace the existing entity with the given one, deleting any existing properties not included in the submitted entity

## Examples

The following sections provide several code snippets covering some of the most common Table tasks, including:

* [Creating a table](#creating-a-table "Creating a table")
* [Creating entities](#creating-entities "Creating entities")
* [Querying entities](#querying-entities "Querying entities")


### Creating a table
Create a table in your account and get a `TableClient` to perform operations on the newly created table:

```python
from azure.data.tables import TableServiceClient
table_service_client = TableServiceClient.from_connection_string(conn_str="<connection_string>")
table_name = "myTable"
table_client = table_service_client.create_table(table_name=table_name)
```

### Creating entities
Create entities in the table:

```python
from azure.data.tables import TableServiceClient
from datetime import datetime

PRODUCT_ID = u'001234'
PRODUCT_NAME = u'RedMarker'

my_entity = {
    u'PartitionKey': PRODUCT_NAME,
    u'RowKey': PRODUCT_ID,
    u'Stock': 15,
    u'Price': 9.99,
    u'Comments': u"great product",
    u'OnSale': True,
    u'ReducedPrice': 7.99,
    u'PurchaseDate': datetime(1973, 10, 4),
    u'BinaryRepresentation': b'product_name'
}

table_service_client = TableServiceClient.from_connection_string(conn_str="<connection_string>")
table_client = table_service_client.get_table_client(table_name="myTable")

entity = table_client.create_entity(entity=my_entity)
```

### Querying entities
Querying entities in the table:

```python
from azure.data.tables import TableClient
my_filter = "PartitionKey eq 'RedMarker'"
table_client = TableClient.from_connection_string(conn_str="<connection_string>", table_name="myTable")
entities = table_client.query_entities(my_filter)
for entity in entities:
    for key in entity.keys():
        print(f"Key: {key}, Value: {entity[key]}")
```

## Optional Configuration
Optional keyword arguments can be passed in at the client and per-operation level. The azure-core [reference documentation][azure_core_ref_docs] describes available configurations for retries, logging, transport protocols, and more.


### Retry Policy configuration

Use the following keyword arguments when instantiating a client to configure the retry policy:

* __retry_total__ (int): Total number of retries to allow. Takes precedence over other counts.
Pass in `retry_total=0` if you do not want to retry on requests. Defaults to 10.
* __retry_connect__ (int): How many connection-related errors to retry on. Defaults to 3.
* __retry_read__ (int): How many times to retry on read errors. Defaults to 3.
* __retry_status__ (int): How many times to retry on bad status codes. Defaults to 3.
* __retry_to_secondary__ (bool): Whether the request should be retried to secondary, if able.
This should only be enabled of RA-GRS accounts are used and potentially stale data can be handled.
Defaults to `False`.

### Other client / per-operation configuration

Other optional configuration keyword arguments that can be specified on the client or per-operation.

**Client keyword arguments:**

* __connection_timeout__ (int): Optionally sets the connect and read timeout value, in seconds.
* __transport__ (Any): User-provided transport to send the HTTP request.

**Per-operation keyword arguments:**

* __raw_response_hook__ (callable): The given callback uses the response returned from the service.
* __raw_request_hook__ (callable): The given callback uses the request before being sent to service.
* __client_request_id__ (str): Optional user specified identification of the request.
* __user_agent__ (str): Appends the custom value to the user-agent header to be sent with the request.
* __logging_enable__ (bool): Enables logging at the DEBUG level. Defaults to False. Can also be passed in at
the client level to enable it for all requests.
* __headers__ (dict): Pass in custom headers as key, value pairs. E.g. `headers={'CustomValue': value}`


## Troubleshooting

### General
Azure Tables clients raise exceptions defined in [Azure Core][azure_core_readme].
When you interact with the Azure table library using the Python SDK, errors returned by the service respond to the same HTTP status codes for [REST API][tables_rest] requests. The Table service operations will throw a `HttpResponseError` on failure with helpful [error codes][tables_error_codes].

For examples, if you try to create a table that already exists, a `409` error is returned indicating "Conflict".
```python
from azure.data.tables import TableServiceClient
from azure.core.exceptions import HttpResponseError
table_name = 'YourTableName'

service_client = TableServiceClient.from_connection_string(connection_string)

# Create the table if it does not already exist
tc = service_client.create_table_if_not_exists(table_name)

try:
    service_client.create_table(table_name)
except HttpResponseError:
    print(f"Table with name {table_name} already exists")
```

### Logging
This library uses the standard
[logging][python_logging] library for logging.
Basic information about HTTP sessions (URLs, headers, etc.) is logged at INFO
level.

Detailed DEBUG level logging, including request/response bodies and unredacted
headers, can be enabled on a client with the `logging_enable` argument:
```python
import sys
import logging
from azure.data.tables import TableServiceClient
# Create a logger for the 'azure' SDK
logger = logging.getLogger('azure')
logger.setLevel(logging.DEBUG)

# Configure a console output
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

# This client will log detailed information about its HTTP sessions, at DEBUG level
service_client = TableServiceClient.from_connection_string("your_connection_string", logging_enable=True)
```

Similarly, `logging_enable` can enable detailed logging for a single operation,
even when it is not enabled for the client:
```python
service_client.create_entity(entity=my_entity, logging_enable=True)
```

## Next steps

Get started with our [Table samples][tables_samples].

Several Azure Tables Python SDK samples are available to you in the SDK's GitHub repository. These samples provide example code for additional scenarios commonly encountered while working with Tables.

### Common Scenarios
These code samples show common scenario operations with the Azure Tables client library. The async versions of the samples (the python sample files appended with _async) show asynchronous operations.

* Create and delete tables: [sample_create_delete_table.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_create_delete_table.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/async_samples/sample_create_delete_table_async.py))
* List and query tables: [sample_query_tables.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_query_tables.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/async_samples/sample_query_tables_async.py))
* Insert and delete entities: [sample_insert_delete_entities.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_insert_delete_entities.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/async_samples/sample_insert_delete_entities_async.py))
* Query and list entities: [sample_query_table.py](https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_query_table.py) ([async version](https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/async_samples/sample_query_table_async.py))
* Update, upsert, and merge entities: [sample_update_upsert_merge_entities.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_update_upsert_merge_entities.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/async_samples/sample_update_upsert_merge_entities_async.py))
* Committing many requests in a single transaction: [sample_batching.py](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_batching.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/async_samples/sample_batching_async.py))

### Additional documentation
For more extensive documentation on Azure Tables, see the [Azure Tables documentation][Tables_product_doc] on learn.microsoft.com.

## Known Issues
A list of currently known issues relating to Cosmos DB table endpoints can be found [here](https://aka.ms/tablesknownissues).

## Contributing
This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct][msft_oss_coc]. For more information see the [Code of Conduct FAQ][msft_oss_coc_faq] or contact [opencode@microsoft.com][contact_msft_oss] with any additional questions or comments.

<!-- LINKS -->
[source_code]:https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables
[Tables_pypi]:https://aka.ms/azsdk/python/tablespypi
[Tables_ref_docs]:https://learn.microsoft.com/python/api/overview/azure/data-tables-readme?view=azure-python
[Tables_product_doc]:https://learn.microsoft.com/azure/cosmos-db/table-introduction
[Tables_samples]:https://github.com/Azure/azure-sdk-for-python/tree/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples
[migration_guide]:https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/migration_guide.md

[azure_subscription]:https://azure.microsoft.com/free/
[azure_storage_account]:https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal
[azure_cosmos_account]:https://learn.microsoft.com/azure/cosmos-db/create-cosmosdb-resources-portal
[pip_link]:https://pypi.org/project/pip/

[azure_create_cosmos]:https://learn.microsoft.com/azure/cosmos-db/create-cosmosdb-resources-portal
[azure_cli_create_cosmos]:https://learn.microsoft.com/azure/cosmos-db/scripts/cli/table/create
[azure_portal_create_cosmos]:https://learn.microsoft.com/azure/cosmos-db/create-cosmosdb-resources-portal
[azure_portal_create_account]:https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal
[azure_powershell_create_account]:https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-powershell
[azure_cli_create_account]: https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-cli

[azure_cli_account_url]:https://learn.microsoft.com/cli/azure/storage/account?view=azure-cli-latest#az-storage-account-show
[azure_powershell_account_url]:https://learn.microsoft.com/powershell/module/az.storage/get-azstorageaccount?view=azps-4.6.1
[azure_portal_account_url]:https://learn.microsoft.com/azure/storage/common/storage-account-overview#storage-account-endpoints

[azure_sas_token]:https://learn.microsoft.com/azure/storage/common/storage-sas-overview
[azure_shared_key]:https://learn.microsoft.com/rest/api/storageservices/authorize-with-shared-key

[odata_syntax]:https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/README.md#writing-filters

[azure_core_ref_docs]: https://azuresdkdocs.z19.web.core.windows.net/python/azure-core/latest/azure.core.html
[azure_core_readme]: https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/core/azure-core/README.md

[python_logging]: https://docs.python.org/3/library/logging.html
[tables_error_codes]: https://learn.microsoft.com/rest/api/storageservices/table-service-error-codes

[msft_oss_coc]:https://opensource.microsoft.com/codeofconduct/
[msft_oss_coc_faq]:https://opensource.microsoft.com/codeofconduct/faq/
[contact_msft_oss]:mailto:opencode@microsoft.com

[tables_rest]: https://learn.microsoft.com/rest/api/storageservices/table-service-rest-api

[create_entity]:https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_insert_delete_entities.py#L67-L73
[delete_entity]:https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_insert_delete_entities.py#L89-L92
[update_entity]:https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_update_upsert_merge_entities.py#L165-L181
[query_entities]:https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_query_table.py#L75-L89
[get_entity]:https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_update_upsert_merge_entities.py#L67-L71
[upsert_entity]:https://github.com/Azure/azure-sdk-for-python/blob/azure-data-tables_12.7.0/sdk/tables/azure-data-tables/samples/sample_update_upsert_merge_entities.py#L155-L163

