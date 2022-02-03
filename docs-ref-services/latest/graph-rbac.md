---
title: Graph RBAC libraries for python
description: Reference for Graph RBAC libraries for python
keywords: Azure, python, SDK, API, Graph RBAC
author: ramya-rao-a
ms.author: ramyar
manager: jfriend

ms.date: 05/10/2019
ms.topic: reference
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
---

# Azure Active Directory Graph libraries for Python

> [!IMPORTANT]
>
> As of February 2019, we started the process to deprecate some earlier versions of Azure Active Directory Graph API in favor of the Microsoft Graph API. 
>
> For details, updates, and time frames, see [Microsoft Graph or the Azure AD Graph](https://developer.microsoft.com/office/blogs/microsoft-graph-or-azure-ad-graph/) in the Office Dev Center.
>
> Moving forward, applications should use the Microsoft Graph API. 

## Overview	

Sign-on users and control access to applications and APIs with [Active Directory Graph](/azure/active-directory/develop/active-directory-graph-api).	

## Client library	

 ```bash	
pip install azure-graphrbac	
```	

### Example	
> [!NOTE]	
> You need to change the resource parameter to https://graph.windows.net while creating the credentials instance	
 ```python	
from azure.graphrbac import GraphRbacManagementClient	
from azure.common.credentials import UserPassCredentials	
 credentials = UserPassCredentials(	
            'user@domain.com',      # Your user	
            'my_password',          # Your password	
            resource="https://graph.windows.net"	
    )	
 tenant_id = "myad.onmicrosoft.com"	
 graphrbac_client = GraphRbacManagementClient(	
    credentials,	
    tenant_id	
)	
```	
The following code creates a user, get it directly and by list filtering, and then delete it.	
```python	
from azure.graphrbac.models import UserCreateParameters, PasswordProfile	
 user = graphrbac_client.users.create(	
    UserCreateParameters(	
        user_principal_name="testbuddy@{}".format(MY_AD_DOMAIN),	
        account_enabled=False,	
        display_name='Test Buddy',	
        mail_nickname='testbuddy',	
        password_profile=PasswordProfile(	
            password='MyStr0ngP4ssword',	
            force_change_password_next_login=True	
        )	
    )	
)	
# user is a User instance	
self.assertEqual(user.display_name, 'Test Buddy')	
 user = graphrbac_client.users.get(user.object_id)	
self.assertEqual(user.display_name, 'Test Buddy')	
 for user in graphrbac_client.users.list(filter="displayName eq 'Test Buddy'"):	
    self.assertEqual(user.display_name, 'Test Buddy')	
 graphrbac_client.users.delete(user.object_id)	
```
