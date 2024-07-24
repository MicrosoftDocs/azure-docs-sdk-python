---
title: Azure Event Grid SDK for Python
description: Reference for Azure Event Grid SDK for Python
ms.date: 07/24/2024
ms.topic: reference
ms.devlang: python
ms.service: event-grid
---
# Event Grid libraries for Python


Azure Event Grid is a fully-managed intelligent event routing service that allows for uniform event consumption using a publish-subscribe model.

## Libraries for data access

The latest version of the Azure Event Grid library is version 4.x.x. We highly recommend using version 4.x.x for new applications.

To update existing applications to version 4.x.x, please follow the [migration guide](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/eventgrid/azure-eventgrid/migration_guide.md).

### Version 4.x.x

To publish a CloudEvent, an EventGridEvent or a Custom schema event to Azure Event Grid, you would use the latest version of the `azure-eventgrid`. This version also has async support.

| Library | Reference | Samples | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    [azure-eventgrid v4](https://pypi.org/project/azure-eventgrid/)    |    [API Reference for azure-eventgrid v4](https://docs.microsoft.com/python/api/overview/azure/event-grid?view=azure-python)    |    [Samples for azure-eventgrid v4](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventgrid/azure-eventgrid/samples)   |    [Source code for azure-eventgrid v4](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventgrid/azure-eventgrid)    |

### Version 1.x.x

The older version allows you to send events to Azure Event Grid, but it lacks a lot of the new features and performance improvements available in the latest version of the same package.

| Library | Reference | Samples | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    [azure-eventgrid v1](https://pypi.org/project/azure-eventgrid/1.3.0/)    |    [API Reference for azure-eventgrid v1](https://docs.microsoft.com/python/api/overview/azure/event-grid?view=azure-python)    |    [Samples for azure-eventgrid v1](https://github.com/Azure-Samples/event-grid-python-public-consume-events)   |    [Source code for azure-eventgrid v1](https://github.com/Azure/azure-sdk-for-python/tree/release/eventgrid-v1/sdk/eventgrid/azure-eventgrid)    |

## Libraries for resource management

To manage your Azure Event Grid resources like topics and domains via the Azure Resource Manager, you would use the below package:

|    Library    |    Reference    |    Source    |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|    [azure-mgmt-eventgrid](https://pypi.org/project/azure-mgmt-eventgrid/)    |    [API Reference for azure-mgmt-eventgrid](https://docs.microsoft.com/python/api/overview/azure/eventgrid/management?view=azure-python)    |   [Source code for azure-mgmt-eventgrid](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventgrid/azure-mgmt-eventgrid)    |

## Next Steps

* [Event Grid documentation](https://docs.microsoft.com/azure/event-grid/)
* [SDK source code](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventgrid/)
* [SDK reference documentation](https://docs.microsoft.com/python/api/overview/azure/event-grid?view=azure-python)