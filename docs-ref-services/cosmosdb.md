 ---
title: Azure Cosmos DB libraries for Python
description: Reference documentation for the Python client libraries for Azure Cosmos DB
keywords: Azure, Python, SDK, API, SQL, database, PostGres,Cosmos DB, NoSQL 
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 03/20/2018
ms.topic: article
ms.devlang: python
ms.service: cosmosdb
---

# Azure Cosmos DB libraries for Python

## Overview

Use Azure Cosmos DB in your Python applications to store and query JSON documents in a NoSQL data store.

Learn more about [Azure Cosmos DB](https://docs.microsoft.com/azure/cosmos-db/introduction).

## Client library
 ```bash
pip install pydocumentdb
 ```

## Management library
```bash
pip install azure-mgmt-cosmosdb
```

### Example

Find matching documents in Azure CosmosDB using a SQL-like query interface:

```python
import pydocumentdb
import pydocumentdb.document_client as document_client

# Initialize the Python Azure Cosmos DB client
client = document_client.DocumentClient(config['ENDPOINT'], {'masterKey': config['MASTERKEY']})
# Create a database
db = client.CreateDatabase({ 'id': config['DOCUMENTDB_DATABASE'] })

# Create collection options
options = {
    'offerEnableRUPerMinuteThroughput': True,
    'offerVersion': "V2",
    'offerThroughput': 400
}

# Create a collection
collection = client.CreateCollection(db['_self'], { 'id': config['DOCUMENTDB_COLLECTION'] }, options)

# Create some documents
document1 = client.CreateDocument(collection['_self'],
    { 
        'id': 'server1',
        'Web Site': 0,
        'Cloud Service': 0,
        'Virtual Machine': 0,
        'name': 'some' 
    })

# Query them in SQL
query = { 'query': 'SELECT * FROM server s' }    

options = {} 
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryDocuments(collection['_self'], query, options)
results = list(result_iterable)

print(results)
```
> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/cosmosdb/management)

## Samples

[Develop a Python app using Azure Cosmos DB](https://azure.microsoft.com/resources/samples/azure-cosmos-db-documentdb-python-getting-started/)


