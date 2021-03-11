---
title: Microsoft Authentication Library (MSAL) for Python overview
titleSuffix: Microsoft Authentication Library (MSAL)
description: Learn how to integrate MSAL for Python with the Microsoft identity platform
services: active-directory
author: mmacy
manager: CelesteDG

ms.service: active-directory
ms.subservice: develop
ms.topic: conceptual
ms.workload: identity
ms.date: 01/19/2021
ms.author: marsma
ms.custom: marsma
#Customer intent: As an application developer, I want to know how to write a desktop app that calls web APIs by using the Microsoft identity platform.
---
# Microsoft Authentication Library (MSAL) for Python

The Microsoft Authentication Library for Python enables applications to integrate with the [Microsoft identity platform](https://aka.ms/aaddevv2). It allows you to sign in users or apps with Microsoft identities ([Azure AD](https://azure.microsoft.com/services/active-directory/), [Microsoft Accounts](https://account.microsoft.com) and [Azure AD B2C](https://azure.microsoft.com/services/active-directory-b2c/) accounts) and obtain tokens to call Microsoft APIs such as [Microsoft Graph](https://graph.microsoft.io/) or your own APIs registered with the Microsoft identity platform. It is built using industry standard OAuth2 and OpenID Connect protocols



[Getting Started](/azure/active-directory/develop/quickstart-v2-python-webapp) | [Documentation](https://github.com/AzureAD/microsoft-authentication-library-for-python/wiki) (GitHub) | [Samples](https://aka.ms/aaddevsamplesv2) |


## Installation

You can find MSAL Python on [Pypi](https://pypi.org/project/msal/).

1. If you haven't already, install [pip](https://pip.pypa.io/en/stable/installing/).
2. Execute `pip install msal` to install the package.

## Versions

This library follows [Semantic Versioning](http://semver.org/).

You can find the changes for each version under [Releases](https://github.com/AzureAD/microsoft-authentication-library-for-python/releases).

## Usage

Before using MSAL Python [register your application](/azure/active-directory/develop/quickstart-v2-register-an-app) with the Microsoft identity platform.

Acquiring tokens with MSAL Python follows this 3-step pattern. This is the high level conceptual pattern. There will be some variations for different flows. They are demonstrated in [runnable samples hosted right in this repo](https://github.com/AzureAD/microsoft-authentication-library-for-python/tree/dev/sample).


1. MSAL proposes a clean separation between [public client applications, and confidential client applications](https://tools.ietf.org/html/rfc6749#section-2.1). Therefore, create either a `PublicClientApplication` or a `ConfidentialClientApplication` instance, and reuse it during the lifecycle of your app. The following example shows a `PublicClientApplication`:

   ```python
   from msal import PublicClientApplication
   app = PublicClientApplication(
       "your_client_id",
       authority="https://login.microsoftonline.com/Enter_the_Tenant_Name_Here")
   ```

   Later, each time you would want an access token, you start by:
   ```python
   result = None  # It is just an initial value. Please follow instructions below.
   ```

2. The API model in MSAL provides you explicit control on how to utilize token cache. This cache part is technically optional, but we highly recommend you to harness the power of MSAL cache. It will automatically handle the token refresh for you.

   ```python
   # We now check the cache to see
   # whether we already have some accounts that the end user already used to sign in before.
   accounts = app.get_accounts()
   if accounts:
       # If so, you could then somehow display these accounts and let end user choose
       print("Pick the account you want to use to proceed:")
       for a in accounts:
           print(a["username"])
       # Assuming the end user chose this one
       chosen = accounts[0]
       # Now let's try to find a token in cache for this account
       result = app.acquire_token_silent(["your_scope"], account=chosen)
   ```

3. Either there is no suitable token in the cache, or you chose to skip the previous step. Send a request to Azure AD to obtain a token. There are different methods based on your client type and scenario. Here we demonstrate a placeholder flow.

   ```python
   if not result:
       # So no suitable token exists in cache. Let's get a new one from AAD.
       result = app.acquire_token_by_one_of_the_actual_method(..., scopes=["User.Read"])
   if "access_token" in result:
       print(result["access_token"])  # Yay!
   else:
       print(result.get("error"))
       print(result.get("error_description"))
       print(result.get("correlation_id"))  # You may need this when reporting a bug
   ```

Refer to the [Wiki on GitHub](https://github.com/AzureAD/microsoft-authentication-library-for-python/wiki) for more details on the MSAL Python functionality and usage.

## Migrate from ADAL to MSAL

If your application is using ADAL Python, we recommend you update it to use MSAL Python. No new feature work will be done in ADAL Python.

See the [ADAL to MSAL migration](https://github.com/AzureAD/microsoft-authentication-library-for-python/wiki/Migrate-to-MSAL-Python) guide.

## Next Steps

- [Application types and authentication scenarios](https://docs.microsoft.com/azure/active-directory/develop/authentication-flows-app-scenarios): MSAL Python supports multiple application types and authentication scenarios.
- [Auth Scenarios](https://docs.microsoft.com/azure/active-directory/develop/authentication-scenarios) and [Auth protocols](https://docs.microsoft.com/azure/active-directory/develop/active-directory-v2-protocols): Get more information on authentication scenarios and protocols.
- [Sample applications](https://aka.ms/aaddevsamplesv2) and [documentation](https://aka.ms/aaddevv2): Get started with learning the Microsoft identity platform.
