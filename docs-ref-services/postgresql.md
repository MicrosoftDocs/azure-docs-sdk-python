---
title: Azure PostgreSQL libraries for Python
description: 
keywords: Azure, Python, SDK, API, SQL, database, Postgres, PostgreSQL
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 07/11/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: postgresql
---

#Azure PostgreSQL libraries for Python

## Overview
Use the ODBC driver and pyodbc to connect to the database and execute SQL statements directly.

Learn more about [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/).

## Client ODBC driver and pyodbc
The recommended client library for accessing Azure Database for PostgreSQL is the Microsoft [ODBC driver and pyodbc](https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python#install-the-python-and-database-communication-libraries)

### Example 

Connect to a Azure Database for PostgreSQL and select all records in the `SALES` table. You can get the ODBC connection string for the database from the Azure Portal.

```python
import pyodbc

SERVER = 'your_server_name.postgres.database.azure.com'
DATABASE = 'your_db_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'

DRIVER = '{PostgreSQL ODBC Driver}'
cnxn = pyodbc.connect(
    'DRIVER=' + DRIVER + ';PORT=5432;SERVER=' + SERVER +
    ';PORT=5432;DATABASE=' + DATABASE + ';UID=' + USERNAME +
    ';PWD=' + PASSWORD)
cursor = cnxn.cursor()
selectsql = "SELECT * FROM SALES" # SALES is an example table name
cursor.execute(selectsql)
```

## Management API
### Requirements
You must install the PostgreSQL management libraries for Python.
```bash
import time

pip3 install azure-common  # needed for access credentials
pip3 install azure-mgmt-rdbms
```

You will also need to create an [Active Directory Service Principal](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?toc=%2fazure%2fazure-resource-manager%2ftoc.json) to obtain the necessary credentials for programmatic access to management functionality.
This can be done via the Azure CLI 2.0 as follows:

```bash
az ad sp create-for-rbac --name "MY-PRINCIPAL-NAME" --password "STRONG-SECRET-PASSWORD"
```

### Example
In this example we will create a new Postgres database on our existing Postgres server.
```python
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgtm.rdbms.postgresql import PostgreSQLManagementClient

SP_APP_ID = "YOUR-SERVICE-PRINCIPAL-APP-ID"
SP_PASSWORD = "YOUR-SERVICE_PRINCIPAL-PASSWORD"
SP_TENANT = "YOUR-SERVICE-PRINCIPAL-TENANT-ID"

SUBSCRIPTION_ID = "YOUR-AZURE-SUBSCRIPTION-ID"
RESOURCE_GROUP = "YOUR-AZURE-RESOURCE-GROUP-WITH-POSTGRES"
POSTGRES_SERVER = "YOUR-POSTGRES-SERVER-NAME"
DB_NAME = "YOUR-DESIRED-DATABASE-NAME"


credentials = ServicePrincipalCredentials(SP_APP_ID, SP_PASSWORD, tenant=SP_TENANT)
client = PostgreSQLManagementClient(credentials, SUBSCRIPTION_ID)

job_creation_poller = client.databases.create_or_update(
    resource_group_name=RESOURCE_GROUP,
    server_name=POSTGRES_SERVER, database_name=DB_NAME)
job = job_creation_poller.result()
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure.mgmt.rdbms.postgresql)

