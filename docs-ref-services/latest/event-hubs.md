---
title: Azure Event Hubs SDK for Python
description: Reference for Azure Event Hubs SDK for Python
ms.date: 07/24/2024
ms.topic: reference
ms.devlang: python
ms.service: event-hubs
---
# Azure Event Hubs libraries for Python

Azure Event Hubs is a highly scalable publish-subscribe service that can ingest millions of events per second and stream them to multiple consumers. This lets you process and analyze the massive amounts of data produced by your connected devices and applications. Once Event Hubs has collected the data, you can retrieve, transform, and store it by using any real-time analytics provider or with batching/storage adapters. If you would like to know more about Azure Event Hubs, you may wish to review: [What is Event Hubs](https://docs.microsoft.com/azure/event-hubs/event-hubs-about).

## Libraries for data access

The latest version of the Azure Evnet Hub library is version 5.x.x. We highly recommend using version 5.x.x for new applications.

To update existing applications to version 5.x.x, please follow the [migration guide](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/eventhub/azure-eventhub/migration_guide.md).

### Version 5.x.x

To send and receive events from an Azure Event Hub instance, you would use the below packages.

| Library | Reference | Samples | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    [azure-eventhub v5](https://pypi.org/project/azure-eventhub/)    |    [API Reference for azure-eventhub v5](https://docs.microsoft.com/python/api/overview/azure/eventhub-readme?view=azure-python)    |    [Samples for azure-eventhub v5](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub/samples)   |    [Source code for azure-eventhub v5](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub)    |
|    [azure-eventhub-checkpointstoreblob](https://pypi.org/project/azure-eventhub-checkpointstoreblob/)    |    [API Reference](https://docs.microsoft.com/python/api/overview/azure/eventhub-checkpointstoreblob-readme?view=azure-python)    |    [Samples](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub-checkpointstoreblob/samples)   |    [Source code](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub-checkpointstoreblob)    |
|    [azure-eventhub-checkpointstoreblob-aio](https://pypi.org/project/azure-eventhub-checkpointstoreblob-aio/)    |    [API Reference](https://docs.microsoft.com/python/api/overview/azure/eventhub-checkpointstoreblob-aio-readme?view=azure-python)    |    [Samples](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub-checkpointstoreblob-aio/samples)   |    [Source code](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub-checkpointstoreblob-aio)    |

### Version 1.x.x

The older verson allows you to send and receive events from an Azure Event Hub instance, but it lacks a lot of the new features and improvements on development experience in the latest version of the same package.

| Library | Reference | Samples | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    [azure-eventhub v1](https://pypi.org/project/azure-eventhub/1.3.3/)    |    [API Reference for azure-eventhub v1](https://docs.microsoft.com/python/api/azure-eventhub/?view=azure-python-previous)    |    [Samples for azure-eventhub v1](https://github.com/Azure/azure-sdk-for-python/tree/release/eventhub-v1/sdk/eventhub/azure-eventhubs/examples)   |    [Source code for azure-eventhub v1](https://github.com/Azure/azure-sdk-for-python/tree/release/eventhub-v1/sdk/eventhub/azure-eventhubs)    |

## Libraries for resource management

Use the following library to work with the Azure Event Huns resource provider:

|    Library    |    Reference    |    Source    |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|    [azure-mgmt-eventhub](https://pypi.org/project/azure-mgmt-eventhub/)    |    [API Reference](https://docs.microsoft.com/python/api/overview/azure/eventhubs/management?view=azure-python)    |   [Source code for azure-mgmt-eventhub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-mgmt-eventhub)    |