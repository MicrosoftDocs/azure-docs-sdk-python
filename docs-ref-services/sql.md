---
title: Azure SQL Database libraries for Python
description: 
keywords: Azure, Python, SDK, API, SQL, database , pyodbc
author: lisawong19  
ms.author: liwong
manager: douge
ms.date: 06/09/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: java
ms.service: 
---

# Azure SQL Database libraries for Python

## Overview

Work with data stored in  [Azure SQL Database](https://docs.microsoft.com/azure/sql-database/sql-database-technical-overview) from Python with the Azure SQL database ODBC driver. 

The management libraries provide an interface to create, manage, and scale Azure SQL Database deployments from your Python code. Set up and manage databases in [elastic pools](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-elastic-pool) to share resources and configure databases across multiple regions from your code.

## Import the libraries

### ODBC driver 
[Instructions](https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python#install-the-python-and-database-communication-libraries) for downloading driver for different operating systems. 

```bash
# Mac OS
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap microsoft/msodbcsql https://github.com/Microsoft/homebrew-msodbcsql-preview
brew update
brew install msodbcsql
sudo pip install pyodbc
```   

### Management

```bash
pip install --pre azure-mgmt-sql
```

## Example

Connect to a Azure SQL database and select all records in the sales table.

```python
server = SERVER_NAME+'.database.windows.net'
database = DATABASE_NAME
username = USER_NAME
password = PASSWORD
driver = '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect(
    'DRIVER=' + driver + ';PORT=1433;SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
selectsql = "SELECT * FROM SALES"
cursor.execute(selectsql)
```

## Samples

| ||
|---|---|
| [Create and manage SQL databases][1] | Create SQL databases, list database usages, and configure firewalls.  | 
| [Use Python to connect and query data][2] | Use Transact-SQL statements to query, insert, update, and delete data in the database. | 

[1]: https://github.com/Azure-Samples/sql-database-python-manage
[2]: https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python


Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.