---
title: Azure PostgreSQL libraries for Python
description: 
keywords: Azure, Python, SDK, API, SQL, database, PostGres, PostgreSQL
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/12/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: postgresql
---

#Azure PostgreSQL libraries for Python

## Overview
The recommended client library for accessing Azure Database for PostgreSQL is the Microsoft [ODBC driver](https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python#install-the-python-and-database-communication-libraries). Use the ODBC driver to connect to the database and execute SQL statements directly.

Learn more about [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/)

## Import the libraries
```bash
pip install azure-mgmt-rdbms
```
## Example
Connect to a Azure Database for PostgreSQL and select all records in the sales table. You can get the ODBC connection string for the database from the Azure Portal.

```python
connection_string = 'DRIVER={PostgreSQL ODBC Driver}; Server="samplepostgresdb.postgres.database.azure.com"; Port=5432; Database={your_database}; Uid="sampleuser@samplemysqldb"; Pwd={your_password};'

cnxn = pyodbc.connect(connection_string)
cursor = cnxn.cursor()
selectsql = "SELECT * FROM SALES"
cursor.execute(selectsql)
```


Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.