---
title: Azure Cache for Redis SDK for Python
description: Reference for Azure Cache for Redis SDK for Python
author: lmazuel
ms.author: lmazuel
ms.data: 12/30/2022
ms.topic: reference
ms.devlang: python
ms.service: cache
---
# Azure Cache for Redis libraries for Python

## Overview

Azure Cache for Redis is based on the popular open-source Redis project. It gives you access to a secure, dedicated Redis server, managed by Microsoft and accessible from your Azure apps.

Redis server is an advanced key-value store, where keys can contain data structures such as strings, hashes, lists, sets, and sorted sets. A Redis server supports a set of atomic operations on these data types.

To learn more, see [Azure Cache for Redis](/azure/azure-cache-for-redis/).

## Management API

Create and manage your Azure Cache for Redis resources in your subscription with the Redis management API.

```bash
pip install redis
pip install azure-mgmt-redis
```

### Example

The following example creates a new cache:

```python
from azure.mgmt.redis import RedisManagementClient
from azure.mgmt.redis.models import Sku, RedisCreateOrUpdateParameters

redis_client = RedisManagementClient(
    credentials,
    subscription_id
)
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

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/redis/management)