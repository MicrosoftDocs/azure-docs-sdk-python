---
title: Azure Service Bus SDK for Python
description: Reference for Azure Service Bus SDK for Python
ms.date: 07/22/2024
ms.topic: reference
ms.devlang: python
ms.service: service-bus-messaging
---
# Azure Service Bus libraries for Python

Microsoft Azure Service Bus supports a set of cloud-based, message-oriented middleware technologies including reliable message queuing and durable publish/subscribe messaging.

## Libraries for data access

The latest version of the Azure Service Bus library is version 7.x.x. We highly recommend using version 7.x.x for new applications.

To update existing applications to version 7.x.x, please follow the [migration guide](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/servicebus/azure-servicebus/migration_guide.md).

### Version 7.x.x

To send and receive messages from an Azure Service Bus queue, topic or subscription, you would use the latest version of the `azure-servicebus`. This also allows to manage your Azure Service Bus resources like queues, topics, subscriptions and rules, but not the namespace itself.

| Library | Reference | Samples | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    [azure-servicebus v7](https://pypi.org/project/azure-servicebus/)    |    [API Reference for azure-servicebus v7](https://docs.microsoft.com/python/api/overview/azure/servicebus-readme?view=azure-python)    |    [Samples for azure-servicebus v7](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-servicebus/samples)   |    [Source code for azure-servicebus v7](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-servicebus)    |

### Version 0.50.x

The older verson allows you to send and receive messages from an Azure Service Bus queue, topic or subscription, but it lacks a lot of the new features and performance improvements available in the latest version of the same package.

| Library | Reference | Samples | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    [azure-servicebus v0.50](https://pypi.org/project/azure-servicebus/0.50.3/)   |    [API Reference for azure-servicebus 0.50](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-servicebus/0.50.3/index.html)    |    [Samples for azure-servicebus 0.50](https://github.com/Azure/azure-sdk-for-python/tree/servicebus_v0.50.3/sdk/servicebus/azure-servicebus/samples)    |    [Source code for azure-servicebus 0.50](https://github.com/Azure/azure-sdk-for-python/tree/servicebus_v0.50.3/sdk/servicebus/azure-servicebus/)    |

## Libraries for resource management

To manage your Azure Service Bus resources like namespaces, queues, topics, subscriptions and rules via the Azure Resource Manager, you would use the below package:

|    Library    |    Reference    |    Source    |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|    [azure-mgmt-servicebus](https://pypi.org/project/azure-mgmt-servicebus/)    |    [API Reference for azure-mgmt-servicebus](/python/api/overview/azure/mgmt-servicebus-readme)    |   [Source code for azure-mgmt-servicebus](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-mgmt-servicebus)    |

## Next Steps

* [Service Bus documentation](https://docs.microsoft.com/azure/service-bus-messaging)
* [SDK source code](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/servicebus)
* [SDK reference documentation](/python/api/overview/azure/servicebus-readme)
* [Additional samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/servicebus/azure-servicebus/samples)