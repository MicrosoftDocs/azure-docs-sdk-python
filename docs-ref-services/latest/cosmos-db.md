---
title: Azure Cosmos DB SDK for Python
description: Reference for Azure Cosmos DB SDK for Python
ms.date: 07/23/2024
ms.topic: reference
ms.devlang: python
ms.service: cosmosdb
---
# Azure Cosmos DB libraries for Python

## Overview

Use Azure Cosmos DB in your Python applications to store and query JSON documents in a NoSQL data store.

Learn more about [Azure Cosmos DB](https://docs.microsoft.com/azure/cosmos-db/introduction).

## Client library - For Applications Development and Data Exploration
 ```bash
pip install azure-cosmos
 ```

## Management library - For Account Level Management Operations
```bash
pip install azure-mgmt-cosmosdb
```

### Key Examples

* [Common Tasks](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/cosmos/azure-cosmos/samples/examples.py):
    * Create Database
    * Create Container
    * CRUD operations on Items in Container 
    * Query a Container for Items
    * Create a Database user

* [Database Management](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/cosmos/azure-cosmos/samples/database_management.py):
    * Basic CRUD operations on a Database resource
    * Query for Database
    * List all Database resources on an account
    
* [Container Management](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/cosmos/azure-cosmos/samples/container_management.py):
    * Basic CRUD operations on a Container resource
    * Query for Container
    * Manage Container Provisioned Throughput
    * List all Container resources in a Database

## Develop Python Applications

* [Develop a Python app to access and manage data stored in Azure Cosmos DB SQL API account](https://github.com/Azure-Samples/azure-cosmos-db-python-getting-started.git)

* [Develop a Python app to access and manage data stored in Azure Cosmos DB MongoDB API account](https://github.com/Azure-Samples/CosmosDB-Flask-Mongo-Sample.git)

* [Develop a Python app to access and manage data stored in Azure Cosmos DB Gremlin API account](https://github.com/Azure-Samples/azure-cosmos-db-graph-python-getting-started.git)

* [Develop a Python app to access and manage data stored in Azure Cosmos DB Cassandra API account](https://github.com/Azure-Samples/azure-cosmos-db-cassandra-python-getting-started.git)

* [Develop a Python app to access and manage data stored in Azure Cosmos DB Table API account](https://github.com/Azure-Samples/storage-python-getting-started.git)