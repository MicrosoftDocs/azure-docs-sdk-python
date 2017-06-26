---
title: Azure CosmosDB libraries for Python
description: Reference documentation for the Python client libraries for CosmosDB
keywords: Azure, Python, SDK, API, SQL, database, PostGres,CosmosDB, NoSQL 
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/26/2017
ms.topic: article
ms.devlang: python
ms.service: cosmosdb
---

# Azure CosmosDB libraries for Python

## Overview

Use CosmosDB in your Python applications to store and query JSON documents in a NoSQL data store.

Learn more about [Azure CosmosDB](https://docs.microsoft.com/en-us/azure/cosmos-db/introduction)

## Install the libraries
```bash
pip install azure-mgmt-documentdb
```

## Example

Find matching documents in CosmosDB using a SQL-like query interface:

```python
query = { 'query': 'SELECT * FROM server s' }    

options = {} 
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryDocuments(collection['_self'], query, options)
results = list(result_iterable)

print(results)
```

## Samples

| **Cosmos DB** ||
|---|---|
| [Develop a Python app using Azure Cosmos DB's DocumentDB API][1] | Use  Azure Cosmos DB with the DocumentDB API to store and access data from a python application | 


[1]: https://azure.microsoft.com/resources/samples/azure-cosmos-db-documentdb-python-getting-started/

Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.

