---
title: Azure Active Directory SDK for Python
description: Reference for Azure Active Directory SDK for Python
author: lmazuel
ms.author: lmazuel
ms.data: 12/16/2022
ms.topic: reference
ms.devlang: python
ms.service: activedirectory
---
# Microsoft Authentication Library (MSAL) for Python

Get started with the Microsoft Authentication Library for Python to sign in users or apps with Microsoft identities ([Azure AD](https://azure.microsoft.com/services/active-directory/), [Microsoft Accounts](https://account.microsoft.com) and [Azure AD B2C](https://azure.microsoft.com/services/active-directory-b2c/) accounts) and obtain tokens to call Microsoft APIs such as [Microsoft Graph](https://graph.microsoft.io/) or your own APIs registered with the [Microsoft identity platform](https://aka.ms/aaddevv2).

Follow steps to install the package and try out example code for basic tasks.

[Quickstart](/azure/active-directory/develop/quickstart-v2-python-webapp) | [API reference documentation](/python/api/msal/msal?view=azure-python) | [Samples](https://aka.ms/aaddevsamplesv2)


## Prerequisites

- An Azure account with an active subscription. [Create a free account][azure_sub].
- [Python 3.6+](https://www.python.org/downloads/).

## Install the package

Install the MSAL for Python package. You can find MSAL Python on [Pypi](https://pypi.org/project/msal/).
```Bash
pip install msal
```

## Setting up

Before using MSAL Python [register your application](/azure/active-directory/develop/quickstart-v2-register-an-app) with the Microsoft identity platform.

## Usage

Acquiring tokens with MSAL Python follows this 3-step pattern. This is the high level conceptual pattern. There will be some variations for different flows. They are demonstrated in the [runnable samples](https://github.com/AzureAD/microsoft-authentication-library-for-python/tree/dev/sample).

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

3. If there is no suitable token in the cache or you've chosen to skip the previous step, send a request to Azure AD to get a token. There are different methods based on your client type and scenario. Here we demonstrate a placeholder flow.

   ```python
   if not result:
       # So no suitable token exists in cache. Let's get a new one from Azure AD.
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

See the [ADAL to MSAL migration](/azure/active-directory/develop/migrate-python-adal-msal) guide.

## Next Steps

- [Handle errors and exceptions in MSAL Python](https://docs.microsoft.com/azure/active-directory/develop/msal-error-handling-python): Learn about the different types of errors and how to handle common sign-in errors.
- [Logging in MSAL Python](https://docs.microsoft.com/azure/active-directory/develop/msal-logging-python): Learn how to generate log messages that can help diagnose issues.

<!--Reference-style links -->
[azure_sub]: https://azure.microsoft.com/free/