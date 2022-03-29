---
title: Azure CDN libraries for python
description: Reference for Azure CDN libraries for python
keywords: Azure, python, SDK, API, CDN
author: sptramer
ms.author: sttramer
manager: douge

ms.date: 07/10/2017
ms.topic: reference
ms.service: azure-cdn
ms.devlang: python
---

# Azure CDN libraries for python

## Overview

[Azure Content Delivery Network (CDN)](https://docs.microsoft.com/azure/cdn/cdn-overview) allows you to provide web content caches to ensure high-bandwidth availability across the globe.

To get started with Azure CDN, see [Getting started with Azure CDN](https://docs.microsoft.com/azure/cdn/cdn-create-new-endpoint).

## Management APIs

Create, query, and manage Azure CDNs with the management API.

Install the management package via pip.

```bash
pip install azure-mgmt-cdn
```

### Example

Creating a CDN profile with a single defined endpoint:

```python
from azure.mgmt.cdn import CdnManagementClient

cdn_client = CdnManagementClient(credentials, 'your-subscription-id')
profile_poller = cdn_client.profiles.create('my-resource-group',
                                            'cdn-name',
                                            {
                                                "location": "some_region", 
                                                "sku": {
                                                    "name": "sku_tier"
                                                } 
                                            })
profile = profile_poller.result()

endpoint_poller = cdn_client.endpoints.create('my-resource-group',
                                          'cdn-name',
                                          'unique-endpoint-name', 
                                          { 
                                              "location": "any_region", 
                                              "origins": [
                                                  {
                                                      "name": "origin_name", 
                                                      "host_name": "url"
                                                  }]
                                          })
endpoint = endpoint_poller.result()
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/cdn/management)
