---
title: Installation
description: How to install the Azure python SDK
keywords: Azure, Python, SDK, API
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/05/2017
ms.topic: install
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
---

# Installation

## Installation with pip

You can install each Azure service's library individually:

```bash
pip install azure-batch          # Install the latest Batch runtime library
pip install azure-mgmt-scheduler # Install the latest Storage management library
```

Preview packages can be installed using the `--pre` flag:

```bash
pip install --pre azure-mgmt-compute # will install only the latest Compute Management library
```

You can also install a set of Azure libraries in a single line using the
`azure` meta-package.

```bash
pip install azure
```

We publish a preview version of this package, which you can access using
the --pre flag:

```bash
pip install --pre azure
```

## Install from GitHub

If you want to install `azure` from source:

    git clone git://github.com/Azure/azure-sdk-for-python.git
    cd azure-sdk-for-python
    python setup.py install
