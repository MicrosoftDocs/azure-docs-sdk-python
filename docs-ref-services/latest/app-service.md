---
title: Azure App Service SDK for Python
description: Reference for Azure App Service SDK for Python
ms.date: 07/29/2024
ms.topic: reference
ms.devlang: python
ms.service: appservice
---
# Azure Web Apps libraries for Python

## Overview

Deploy and scale websites, web applications, services, and REST APIs with [Azure App Service](/azure/app-service).

To get started with Azure App Service, see [Create a Python web app in Azure](/azure/app-service-web/app-service-web-get-started-python).

## Management API

Deploy, manage, and scale elements hosted in the Azure App Service with the management API.

Install the library via pip.

```bash
pip install azure-mgmt-web
```

### Example

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

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure-mgmt-web)

## Samples

* [Manage Azure websites with python][1]
* [Create a Logic App workflow][2]

View the [complete list](https://azure.microsoft.com/resources/samples/?platform=python&term=web-app) of web application samples.

[1]: https://github.com/Azure-Samples/app-service-web-python-manage
[2]: /azure/python/python-sdk-azure-samples-logic-app-workflow