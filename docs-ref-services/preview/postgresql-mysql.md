---
title: Azure MySQL/PostgreSQL libraries for Python
description: 
keywords: Azure, Python, SDK, API, SQL, database, MySQL, PostgreSQL
author: lisawong19
ms.author: ramyar
manager: douge
ms.date: 10/02/2019
ms.topic: reference
ms.prod: azure
ms.technology: azure
ms.devlang: python
---

# Azure Database for MySQL/PostgreSQL libraries for Python

This article demonstrates how you can use Python to access data stored in Azure Database for MySQL and PostgreSQL.

## MySQL

Use Python to create and connect to an [Azure Database for MySQL](/azure/mysql/overview) server with the MySQL manager and pyodbc.

### Management API

Create and manage MySQL resources in your subscription with the management API.

Install the MySQL management libraries with pip.
```bash
pip install azure-mgmt-rdbms
```

Please see the [Python SDK authentication](https://docs.microsoft.com/python/azure/python-sdk-azure-authenticate) page for details on obtaining credentials to authenticate with the management client.

#### Create server example

Creates an Azure Database for MySQL server and restricts access to a range of IP addresses using a firewall rule.

Copy and paste the below code sample into a Python file (ex. `sample.py`) and update the subscription ID, resource group, server name, administrator user name, administrator password, and location with values of your own.

```python
from azure.mgmt.rdbms.mysql import MySQLManagementClient
from azure.mgmt.rdbms.mysql.models import *

SUBSCRIPTION_ID = "YOUR_AZURE_SUBSCRIPTION_ID"
RESOURCE_GROUP = "YOUR_AZURE_RESOURCE_GROUP"
SERVER = "YOUR_SERVER_NAME"
ADMIN_USER = "YOUR_ADMIN_USERNAME"
ADMIN_PASSWORD = "YOUR_ADMIN_PASSWORD"
LOCATION = "westus"

client = MySQLManagementClient(credentials=creds,
    subscription_id=SUBSCRIPTION_ID)

server_creation_poller = client.servers.create(
    RESOURCE_GROUP,
    SERVER,
    ServerForCreate(
        properties=ServerPropertiesForDefaultCreate(
            administrator_login=ADMIN_USER,
            administrator_login_password=ADMIN_PASSWORD,
            version=ServerVersion.one_one,
            storage_profile=StorageProfile(
                storage_mb=51200
            )
        ),
        location=LOCATION,
        sku=Sku(
            name="GP_Gen5_2"
        )
    )
)

server = server_creation_poller.result()

# Open access to this server for IPs
rule_creation_poller = client.firewall_rules.create_or_update(
    RESOURCE_GROUP,
    SERVER,
    "example_firewall_rule",  # Custom firewall rule name
    "123.123.123.123",  # Start ip range
    "123.123.123.124"  # End ip range
)

firewall_rule = rule_creation_poller.result()
```

### Client ODBC driver and pyodbc

The recommended client library for accessing Azure Database for MySQL is the Microsoft [ODBC driver](/azure/sql-database/sql-database-connect-query-python#prerequisites). Use the ODBC driver to connect to the database and execute SQL statements directly.

#### Example

Connect to an Azure Database for MySQL server and select all records in the sales table. You can get the ODBC connection string for the database from the Azure Portal.

```python
SERVER = 'YOUR_SEVER_NAME' + '.mysql.database.azure.com'
DATABASE = 'YOUR_DATABASE_NAME'
USERNAME = 'YOUR_MYSQL_USERNAME'
PASSWORD = 'YOUR_MYSQL_PASSWORD'

DRIVER = '{MySQL ODBC 5.3 UNICODE Driver}'
cnxn = pyodbc.connect(
    'DRIVER=' + DRIVER + ';PORT=3306;SERVER=' + SERVER + ';PORT=3306;DATABASE=' + DATABASE + ';UID=' + USERNAME + ';PWD=' + PASSWORD)
cursor = cnxn.cursor()
selectsql = "SELECT * FROM SALES"  # SALES is an example table name
cursor.execute(selectsql)
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/postgresql/mysql/management)

## PostgreSQL

Use Python to create and connect to an [Azure Database for PostgreSQL](/azure/postgresql/overview) server with the PostgreSQL manager and pyodbc.

Learn more about [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/).

### Management API
Create and manage MySQL resources in your subscription with the management API.

Install the PostgreSQL management libraries with pip.
```bash
pip install azure-mgmt-rdbms
```

Please see the [Python SDK authentication](https://docs.microsoft.com/python/azure/python-sdk-azure-authenticate) page for details on obtaining credentials to authenticate with the management client.

#### Create server example

Creates an Azure Database for PostgreSQL server and restricts access to a range of IP addresses using a firewall rule.

Copy and paste the below code sample into a Python file (ex. `sample.py`) and update the subscription ID, resource group, server name, administrator user name, administrator password, and location with values of your own.

```python
from azure.mgmt.rdbms.postgresql import PostgreSQLManagementClient
from azure.mgmt.rdbms.postgresql.models import *

SUBSCRIPTION_ID = "YOUR_AZURE_SUBSCRIPTION_ID"
RESOURCE_GROUP = "YOUR_AZURE_RESOURCE_GROUP"
SERVER = "YOUR_SERVER_NAME"
ADMIN_USER = "YOUR_ADMIN_USERNAME"
ADMIN_PASSWORD = "YOUR_ADMIN_PASSWORD"
LOCATION = "westus"

client = PostgreSQLManagementClient(credentials=creds,
    subscription_id=SUBSCRIPTION_ID)

server_creation_poller = client.servers.create(
    RESOURCE_GROUP,
    SERVER,
    ServerForCreate(
        properties=ServerPropertiesForDefaultCreate(
            administrator_login=ADMIN_USER,
            administrator_login_password=ADMIN_PASSWORD,
            version=ServerVersion.one_one,
            storage_profile=StorageProfile(
                storage_mb=51200
            )
        ),
        location=LOCATION,
        sku=Sku(
            name="GP_Gen5_2"
        )
    )
)

server = server_creation_poller.result()

# Open access to this server for IPs
rule_creation_poller = client.firewall_rules.create_or_update(
    RESOURCE_GROUP,
    SERVER,
    "example_firewall_rule",  # Custom firewall rule name
    "123.123.123.123",  # Start ip range
    "123.123.123.124"  # End ip range
)

firewall_rule = rule_creation_poller.result()
```

### Client ODBC driver and pyodbc
The recommended client library for accessing Azure Database for PostgreSQL is the Microsoft [ODBC driver and pyodbc](https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python#prerequisites).

#### Connect example

Connect to an Azure Database for PostgreSQL server and select all records in the `SALES` table. You can get the ODBC connection string for the database from the Azure Portal.

```python
import pyodbc

SERVER = 'YOUR_SERVER_NAME.postgres.database.azure.com'
DATABASE = 'YOUR_DB_NAME'
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'

DRIVER = '{PostgreSQL ODBC Driver}'
cnxn = pyodbc.connect(
    'DRIVER=' + DRIVER + ';PORT=5432;SERVER=' + SERVER +
    ';PORT=5432;DATABASE=' + DATABASE + ';UID=' + USERNAME +
    ';PWD=' + PASSWORD)
cursor = cnxn.cursor()
selectsql = "SELECT * FROM SALES" # SALES is an example table name
cursor.execute(selectsql)
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/postgresql/mysql/management)
