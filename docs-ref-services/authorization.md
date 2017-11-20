---
title: Azure Authorization libraries for python
description: Reference for Azure Authorization libraries for python
keywords: Azure, python, SDK, API, Authorization
author: lisawong19
ms.author: liwong
manager: douge

ms.date: 08/04/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
---

# Azure Authorization libraries for python

## Overview 
Sign-on users and control access to applications and APIs with [Azure Active Directory](/azure/active-directory/active-directory-whatis).

## Management API

```bash
pip install azure-mgmt-authorization
```

### Example
```python
from azure.mgmt.authorization import AuthorizationManagementClient

authorization_client = AuthorizationManagementClient(
    credentials,
    subscription_id
)
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/authorization/managementlibrary)