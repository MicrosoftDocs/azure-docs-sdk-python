---
title: Get started with the Azure libraries for Python
description: Getting started with Aure libraries for Python
keywords: Azure, Python, SDK, API
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/05/2017
ms.topic: get-started
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
ms.assetid: 
---

# Get started with the Azure libraries for Python

This tutorial demonstrates the usage of several Azure libraries for Python.  You will set up authentication, create and use an Azure Storage account, create and use an Azure SQL Database, deploy some virtual machines, and deploy an Azure App Service Web App from GitHub.

## Prerequisites

- An Azure account. If you don't have one, [get a free trial](https://azure.microsoft.com/free/)
- [Azure CLI 2.0](https://docs.microsoft.com/cli/azure/install-az-cli2)
- Python!

## Which Python and which version to use
There are several flavors of Python interpreters available - examples include:

* CPython - the standard and most commonly used Python interpreter
* PyPy - fast, compliant alternative implementation to CPython
* IronPython - Python interpreter that runs on .Net/CLR
* Jython - Python interpreter that runs on the Java Virtual Machine

**CPython** v2.7 or v3.3+ and PyPy 5.4.0 are tested and supported for the Azure SDK for Python.

## Where to get Python?
There are several ways to get CPython:

* Directly from [www.python.org](www.python.org)
* From a reputable distro such as [www.continuum.io](www.continuum.io),[www.enthought.com](www.enthought.com) or [www.activestate.com](www.activestate.com)
* Build from source!

Unless you have a specific need, we recommend the first two options.

## Set up authentication

FIXME
- CLI link for creation
- Link to authentication page 
- Use CLI to login

## Create a virtual environment

> [!IMPORTANT]
> Create a virtual environment is optional, but we strongly suggest you to do it.

Create a virtual environment in Bash (Linux or [Bash for Windows](https://msdn.microsoft.com/commandline/wsl/about)
```bash
pip install virtualenv
virtualenv mytestenv
cd mytestenv
source ./bin/activate
```

Create a virtual environment in Powershell:
```powershell
pip install virtualenv
virtualenv mytestenv
cd mytestenv
.\Scripts\activate
```

> [!IMPORTANT]
> Note that if you use [VSCode](https://code.visualstudio.com/) and the [Python extension](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python),  you can start it using "code ." and get your environment configured.

## Create a XXXXXXXXXX

FIXME


## Reference

A [reference](http://docs.microsoft.com/python/api) is available for all packages.