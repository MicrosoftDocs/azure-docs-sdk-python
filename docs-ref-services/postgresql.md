---
title: Azure PostgreSQL libraries for Python
description: 
keywords: Azure, Python, SDK, API, SQL, database, PostGres, PostgreSQL
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

Connect to a Azure Database for PostgreSQL and select all records in the sales table. You can get the ODBC connection string for the database from the Azure Portal.

```python
import pyodbc

server = 'your_server_name.postgres.database.azure.com'
DATABASE = 'your_db_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'

driver = '{PostgreSQL ODBC Driver}'
cnxn = pyodbc.connect(
    'DRIVER=' + driver + ';PORT=5432;SERVER=' + server + ';PORT=5432;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
selectsql = "SELECT * FROM SALES"
cursor.execute(selectsql)
```

## Management API
```bash
pip install azure-mgmt-rdbms-postgresql
```
> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure.mgmt.rdbms.postgresql)

### Example
```python
```


