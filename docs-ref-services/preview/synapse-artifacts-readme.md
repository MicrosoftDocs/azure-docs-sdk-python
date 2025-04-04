---
title: 
keywords: Azure, python, SDK, API, azure-synapse-artifacts, synapse-analytics
ms.date: 02/24/2025
ms.topic: reference
ms.devlang: python
ms.service: synapse-analytics
---
# Microsoft Azure SDK for Python

This is the Microsoft Azure Synapse Artifacts Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the [azure sdk python release](https://aka.ms/azsdk/python/all).

## _Disclaimer_

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to https://github.com/Azure/azure-sdk-for-python/issues/20691_

## Getting started

### Prerequisites

- Python 3.8+ is required to use this package.
- [Azure subscription](https://azure.microsoft.com/free/)

### Install the package

```bash
pip install azure-synapse-artifacts
pip install azure-identity
```

### Authentication

By default, [Azure Active Directory](https://aka.ms/awps/aad) token authentication depends on correct configure of following environment variables.

- `AZURE_CLIENT_ID` for Azure client ID.
- `AZURE_TENANT_ID` for Azure tenant ID.
- `AZURE_CLIENT_SECRET` for Azure client secret.

With above configuration, client can be authenticated by following code:

```python
import os
from azure.identity import DefaultAzureCredential
from azure.synapse.artifacts import ArtifactsClient

endpoint = os.environ["SYNAPSE_ARTIFACTS_ENDPOINT"]
client = ArtifactsClient(endpoint=endpoint, credential=DefaultAzureCredential())
```

## Examples

Code samples for this package can be found at:
- [Search Synapse Artifacts](/samples/browse/?languages=python&term=Getting%20started%20-%20Managing&terms=Getting%20started%20-%20Managing) on docs.microsoft.com


## Troubleshooting

## Next steps

## Provide Feedback

If you encounter any bugs or have suggestions, please file an issue in the
[Issues](https://github.com/Azure/azure-sdk-for-python/issues)
section of the project. 




