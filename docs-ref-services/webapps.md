---
title: Azure Web Apps libraries for Python
description: 
keywords: Azure, Python, SDK, API, web apps, App Service
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/12/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: appservice
---

# Azure Web Apps libraries for Python

## Overview

Deploy, manage, and scale web apps, APIs, and mobile apps running in [Azure App Service](https://docs.microsoft.com/azure/app-service) from your Python code using the management libraries. The management libraries also provide a Python interface for automating app configuration as an alternative to using the Azure Portal or [CLI](https://docs.microsoft.com/cli/azure/install-azure-cli).

## Import the libraries

```bash
pip install --pre azure-mgmt-web
```

## Example

Deploy a webapp from a GitHub repository into Azure Web App.

```python
siteConfiguration = SiteConfig(
    python_version='3.4'
)

# create a web app
web_client.web_apps.create_or_update(
    RESOURCE_GROUP_NAME,
    WEB_APP_NAME,
    Site(
        location='eastus',
        server_farm_id=SERVICE_PLAN_ID,
        site_config=siteConfiguration
    )
)

# continuous deployment with GitHub
source_control_async_operation = web_client.web_apps.create_or_update_source_control(
    RESOURCE_GROUP_NAME,
    WEB_APP_NAME,
    SiteSourceControl(
        location='GitHub',
        repo_url='https://github.com/lisawong19/python-docs-hello-world',
        branch='master'
    )
)
```

## Samples 

|||
|---|---|
| [Manage Azure websites with python][1] | Create, delete and list details of a web app. |
| [Create a Logic App workflow][2] | Create a Logic App workflow. |

[1]: https://azure.microsoft.com/resources/samples/app-service-web-python-manage
[2]: python-sdk-azure-samples-logic-app-workflow.md


Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.