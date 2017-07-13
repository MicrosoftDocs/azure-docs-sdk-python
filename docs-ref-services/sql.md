---
title: Azure SQL Database libraries for Python
description: 
keywords: Azure, Python, SDK, API, SQL, database , pyodbc
author: lisawong19  
ms.author: liwong
manager: douge
ms.date: 07/11/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: sql-database
---

# Azure SQL Database libraries for Python

## Overview

Work with data stored in  [Azure SQL Database](https://docs.microsoft.com/azure/sql-database/sql-database-technical-overview) from Python with the Microsoft ODBC driver and pyodbc. 

## Client ODBC driver and pyodbc
Connect to the Azure SQL Database from your applications using the [Microsoft ODBC driver and pyodbc](https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python#install-the-python-and-database-communication-libraries).

### Example

Connect to a SQL database and select all records in a table.

```python
import pyodbc 

SERVER = 'your_server_name.database.windows.net'
DATABASE = 'your_database_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'

driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+SERVER+';PORT=1443;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD)
cursor = cnxn.cursor()
selectsql = "SELECT * FROM SALES"
cursor.execute(selectsql)
```

## Management API

Create and manage Azure SQL Database resources in your subscription with the management API. 

```bash
pip install azure-mgmt-sql
```
> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure.mgmt.sql)

### Example

Create a SQL Database resource and restrict access to a range of IP addresses using a firewall rule.

```python
RESOURCE_GROUP = 'your_resource_group_name'
SQL_DB = 'your_sqldb_name'

# Create a SQL server
server = sql_client.servers.create_or_update(
    RESOURCE_GROUP,
    SQL_DB,
    {
        'location': LOCATION,
        'version': '12.0', # Required for create
        'administrator_login': USER_NAME, # Required for create
        'administrator_login_password': PASSWORD # Required for create
    }
)

# Open access to this server for IPs
firewall_rule = sql_client.firewall_rules.create_or_update(
    RESOURCE_GROUP
    SQL_DB,
    "firewall_rule_name_123.123.123.123",
    "123.123.123.123", # Start ip range
    "167.220.0.235"  # End ip range
)
```

## Samples

* [Create and manage SQL databases][1]    
* [Use Python to connect and query data][2]   


[1]: https://github.com/Azure-Samples/sql-database-python-manage
[2]: https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python


View the [complete list](https://azure.microsoft.com/resources/samples/?platform=python&term=SQL) of Azure SQL database samples. 