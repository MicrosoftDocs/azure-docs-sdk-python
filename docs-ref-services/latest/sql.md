---
title: Azure SQL SDK for Python
description: Reference for Azure SQL SDK for Python
ms.date: 02/10/2026
ms.topic: reference
ms.devlang: python
ms.service: sql
ai-usage: ai-assisted
---
# Azure SQL Database libraries for Python

## Overview

Work with data stored in [Azure SQL Database](/azure/sql-database/sql-database-technical-overview) from Python with the [mssql-python](https://pypi.org/project/mssql-python/) driver, Microsoft's native Python driver for SQL Server. View the [quickstart](/sql/connect/python/mssql-python/python-sql-driver-mssql-python-quickstart) to connect to an Azure SQL database and run Transact-SQL queries.

## Install mssql-python

```bash
pip install mssql-python
```

The `mssql-python` package includes the Microsoft ODBC driver, so you don't need to install it separately. For more information, see the [mssql-python quickstart](/sql/connect/python/mssql-python/python-sql-driver-mssql-python-quickstart).

## Connect and execute a SQL query

### Connect to a SQL database

```python
from mssql_python import connect

connection_string = (
    "Server=your_server.database.windows.net;"
    "Database=your_database;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Authentication=ActiveDirectoryInteractive"
)

cnxn = connect(connection_string)
cursor = cnxn.cursor()
```

### Execute a SQL query

```python
cursor.execute(
    "SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName "
    "FROM [SalesLT].[ProductCategory] pc "
    "JOIN [SalesLT].[Product] p "
    "ON pc.productcategoryid = p.productcategoryid"
)
row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
```

> [!div class="nextstepaction"]
> [mssql-python quickstart](/sql/connect/python/mssql-python/python-sql-driver-mssql-python-quickstart)

## [Management API](/python/api/overview/azure/sql/management)

Create and manage Azure SQL Database resources in your subscription with the management API. 

```bash
pip install azure-common
pip install azure-mgmt-sql
pip install azure-mgmt-resource
```

## Example

Create a SQL Database resource and restrict access to a range of IP addresses using a firewall rule.

```python
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.sql import SqlManagementClient

RESOURCE_GROUP = 'YOUR_RESOURCE_GROUP_NAME'
LOCATION = 'eastus'  # example Azure availability zone, should match resource group
SQL_SERVER = 'yourvirtualsqlserver'
SQL_DB = 'YOUR_SQLDB_NAME'
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'

# create resource client
resource_client = get_client_from_cli_profile(ResourceManagementClient)
# create resource group
resource_client.resource_groups.create_or_update(RESOURCE_GROUP, {'location': LOCATION})

sql_client = get_client_from_cli_profile(SqlManagementClient)

# Create a SQL server
server = sql_client.servers.create_or_update(
    RESOURCE_GROUP,
    SQL_SERVER,
    {
        'location': LOCATION,
        'version': '12.0', # Required for create
        'administrator_login': USERNAME, # Required for create
        'administrator_login_password': PASSWORD # Required for create
    }
)

# Create a SQL database in the Basic tier
database = sql_client.databases.create_or_update(
    RESOURCE_GROUP,
    SQL_SERVER,
    SQL_DB,
    {
        'location': LOCATION,
        'collation': 'SQL_Latin1_General_CP1_CI_AS',
        'create_mode': 'default',
        'requested_service_objective_name': 'Basic'
    }
)

# Open access to this server for IPs
firewall_rule = sql_client.firewall_rules.create_or_update(
    RESOURCE_GROUP,
    SQL_DB,
    "firewall_rule_name_123.123.123.123",
    "123.123.123.123", # Start ip range
    "167.220.0.235"  # End ip range
)
```
> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure-mgmt-sql)