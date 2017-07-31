---
title: Azure Redis libraries for Python
description: Reference documentation for the Python client libraries for Redis
keywords: Azure, Python, Redis, API, SDK, database, NoSQL
author: sptramer
ms.author: sttramer
manager: douge
ms.date: 06/26/2017
ms.topic: article
ms.devlang: python
ms.service: redis
---

# Azure Redis Cache libraries for Python

## Overview

Azure Redis Cache is based on the popular open source Redis project. It gives you access to a secure, dedicated Redis instance, managed by Microsoft and accessible from your Azure apps.

Redis is an advanced key-value store, where keys can contain data structures such as strings, hashes, lists, sets, and sorted sets. Redis supports a set of atomic operations on these data types.

Learn more about [Azure Redis Cache](https://docs.microsoft.com/azure/redis-cache/).

## Install the libraries

```bash
pip install azure-mgmt-redis
```

## Example

The following example creates a new Redis cache:

```python
from azure.mgmt.redis.models import Sku, RedisCreateOrUpdateParameters

group_name = 'myresourcegroup'
cache_name = 'mycachename'
redis_cache = redis_client.redis.create_or_update(
    group_name,
    cache_name,
    RedisCreateOrUpdateParameters(
        sku = Sku(name = 'Basic', family = 'C', capacity = '1'),
        location = "East US"
    )
)
# redis_cache is a RedisResourceWithAccessKey instance
```

Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.
