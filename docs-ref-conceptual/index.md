---
title: Azure for Python developers - Tutorials, API Reference | Microsoft Docs
description: Tools, SDKs, tutorials, and samples to help you create and deploy Python apps to Azure.
keywords: Azure, Python, SDK, API
author: lisawong19  
ms.author: liwong
manager: douge
layout: LandingPage
ms.date: 06/14/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
---

# Azure for Python developers

Get started building great Python apps on Azure.

<ul class="panelContent">
    <li>
        <div class="cardSize">
            <div class="cardPadding">
                <div class="card">
                    <div class="cardText">
                        <h2>Tools</h2>
                        <a href="python-azure-tools.md">Download Azure tools and plugins.</a>
                    </div>
                </div>
            </div>
        </div>
    </li><li>
        <div class="cardSize">
            <div class="cardPadding">
                <div class="card">
                    <div class="cardImageOuter">
                    </div>
                    <div class="cardText">
                        <h2>Libraries</h2>
                        <a href="python-sdk-azure-install.md">Use services and manage Azure resources.</a>
                    </div>
                </div>
            </div>
        </div>
    </li><li>
        <div class="cardSize">
            <div class="cardPadding">
                <div class="card">
                    <div class="cardImageOuter">
                    </div>
                    <div class="cardText">
                        <h2>Jenkins CI/CD</h2>
                        <a href="">Use Jenkins to deploy to Azure.</a>
                    </div>
                </div>
            </div>
        </div>
    </li>
</ul>

## Management APIs

Import the [Azure management libraries for Python](python-sdk-azure-get-started.md) to manage your Azure resources with an easy to use fluent API. 

```python
sql_client = SqlManagementClient(
    credentials,
    subscription_id
)

server = sql_client.servers.create_or_update(
    'myresourcegroup',
    'myservername',
    {
        'location': 'eastus',
        'version': '12.0', # Required for create
        'administrator_login': 'mysecretname', # Required for create
        'administrator_login_password': 'HusH_Sec4et' # Required for create
    }
)
```

[Get started with the Azure management libraries for Python](python-sdk-azure-get-started.md)

## Five-minute quickstarts
Create and deploy an app using your favorite tools in five minutes.
<ul>
   <li><a href="https://docs.microsoft.com/azure/app-service-web/app-service-web-get-started-python">Flask</a></li>
</ul>

## Tutorials and samples

Complete walkthroughs for app creation and deployment.

<ul>
    <li><a href="https://docs.microsoft.com/azure/app-service-web/app-service-web-tutorial-docker-python-postgresql-app">PostgreSQL</a></li>
    <li><a href="https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python">SQL Database</a></li>
    <li><a href="https://docs.microsoft.com/azure/cosmos-db/documentdb-python-application">CosmosDB</a></li>
    <li><a href="https://docs.microsoft.com/azure/storage/storage-python-how-to-use-blob-storage">Azure Storage</a></li>
</ul>