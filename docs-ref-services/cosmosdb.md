---
title: Azure CosmosDB libraries for Python
description: Reference documentation for the Python client libraries for CosmosDB
keywords: Azure, Python, SDK, API, SQL, database, PostGres,CosmosDB, NoSQL 
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 08/09/2017
ms.topic: article
ms.devlang: python
ms.service: cosmosdb
---

# Azure CosmosDB libraries for Python

## Overview

Use CosmosDB in your Python applications to store and query JSON documents in a NoSQL data store.

Learn more about [Azure CosmosDB](https://docs.microsoft.com/azure/cosmos-db/introduction).

## Client library
 ```bash
pip install pydocumentdb
 ```

## Management library
```bash
pip install azure-mgmt-cosmosdb
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
> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/cosmosdb/managementlibrary)

## Samples

[Develop a Python app using Azure Cosmos DB's DocumentDB API](https://azure.microsoft.com/resources/samples/azure-cosmos-db-documentdb-python-getting-started/)


