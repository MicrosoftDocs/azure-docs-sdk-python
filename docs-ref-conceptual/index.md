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

<ul class="cardsY panelContent">
    <li>
        <a href="python-azure-tools.md">
            <div class="cardSize">
                <div class="cardPadding">
                    <div class="card" style="height: 84px">
                        <div class="cardImageOuter" style="margin-top: 12px">
                            <div class="cardImage">
                                <img src="/media/common/i_tools.svg" alt="" />
                            </div>
                        </div>
                        <div class="cardText">
                            <h3 style="margin-bottom: 0; font-size: 24px">Tools</h3>
                            <p style="font-size: 1rem">Download Azure tools and plug-ins</p>
                        </div>
                    </div>
                </div>
            </div>
        </a>
    </li>
    <li>
        <a href="python-sdk-azure-install.md">
            <div class="cardSize">
                <div class="cardPadding">
                    <div class="card" style="height: 84px">
                        <div class="cardImageOuter" style="margin-top: 12px">
                            <div class="cardImage">
                                <img src="/media/common/i_reference.svg" alt="" />
                            </div>
                        </div>
                        <div class="cardText">
                            <h3 style="margin-bottom: 0; font-size: 24px">Libraries</h3>
                            <p style="font-size: 1rem">Use services and manage Azure resources</p>
                        </div>
                    </div>
                </div>
            </div>
        </a>
    </li>
</ul>


## 5-Minute quickstarts
Learn how to build Python apps with Azure services.
<ul>
   <li><a href="https://docs.microsoft.com/azure/app-service-web/app-service-web-get-started-python">Deploy a Python webapp</a></li>
    <li><a href="https://docs.microsoft.com/azure/sql-database/sql-database-connect-query-python">Connect to Azure SQL Database</a></li>
    <li><a href="https://docs.microsoft.com/azure/cosmos-db/documentdb-python-application">Build a NoSQL app with CosmosDB</a></li>
</ul>

## Management APIs

Install [Azure management modules](python-sdk-azure-install.md) to manage Azure resources. 

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

[Get started with the Azure management modules for Python](python-sdk-azure-get-started.md)

## Step-by-Step Tutorials

Learn how to use Azure services in your Python apps.
<ul>
    <li><a href="https://docs.microsoft.com/azure/app-service-web/app-service-web-tutorial-docker-python-postgresql-app">Create a Flask app with PostgreSQL</a></li>
</ul>