---
title: Azure MySQL libraries for Python
description: 
keywords: Azure, Python, SDK, API, SQL, database, MySQL
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/12/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: mysql
---
# Azure MySQL libraries for Python 

## Overview

Work with resources and data stored in [Azure MySQL Database](/azure/mysql/overview) from python with the MySQL manager and pyodbc.

## Client ODBC driver and pyodbc

The recommended client library for accessing Azure Database for MySQL is the Microsoft [ODBC driver](/azure/sql-database/sql-database-connect-query-python#install-the-python-and-database-communication-libraries). Use the ODBC driver to connect to the database and execute SQL statements directly.

### Example

Connect to a Azure Database for MySQL and select all records in the sales table. You can get the ODBC connection string for the database from the Azure Portal.

```python
server = SERVER_NAME+'.mysql.database.azure.com'
database = DATABASE_NAME
username = USER_NAME
password = PASSWORD
driver = '{MySQL ODBC 5.3 UNICODE Driver}'

cnxn = pyodbc.connect(
    'DRIVER=' + driver + ';PORT=3306;SERVER=' + server + ';PORT=3306;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
selectsql = "SELECT * FROM SALES"
cursor.execute(selectsql)
```

## Management API

Create and manage MySQL resources in your subscription with the management API.

```bash
pip install azure-mgmt-rdbms
```

### Example

Create a MySQL Database resource and restrict access to a range of IP addresses using a firewall rule.

# EXTREMELY ENORMOUS __TODO__: CDA/DEV PLEASE WRITE THIS SAMPLE.

There's some issue where the required `create_mode` param doesn't seem to actually accept standard MySQL `create_mode` values. Who knows.

### Samples

* [Use Python to connect and query data][1]   

[1]: https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python

View the [complete list](https://azure.microsoft.com/resources/samples/?platform=python&term=SQL) of Azure SQL database samples. 