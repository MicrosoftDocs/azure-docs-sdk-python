---
title: Service Bus libraries for Python 
description: Reference documentation for the Python client and management libraries for Service Bus
keywords: Azure, Python, SDK, API, messaging, pubsub, pub-sub, message broker
author: annatisch
ms.author: antisch
manager: mayurid
ms.date: 01/15/2019
ms.topic: article
ms.devlang: python
ms.service: service-bus
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
|    [azure-servicebus](https://pypi.org/project/azure-servicebus/)    |    [Reference](https://docs.microsoft.com/python/api/overview/azure/servicebus-readme?view=azure-python)    |    [Samples](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-servicebus/samples)   |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-servicebus)    |

### Version 0.50.x

The older verson allows you to send and receive messages from an Azure Service Bus queue, topic or subscription, but it lacks a lot of the new features and performance improvements available in the latest version of the same package.

The source code for the Azure Servicebus client libraries for Python is available on [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/servicebus_v0.50.3/sdk/servicebus/azure-servicebus/).

| Library | Reference | Samples | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    [azure-servicebus](https://pypi.org/project/azure-servicebus/0.50.3/)   |    [Reference](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-servicebus/0.50.3/index.html)    |    [Samples](https://github.com/Azure/azure-sdk-for-python/tree/servicebus_v0.50.3/sdk/servicebus/azure-servicebus/samples)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/servicebus_v0.50.3/sdk/servicebus/azure-servicebus/)    |

## Libraries for resource management

To manage your Azure Service Bus resources like namespaces, queues, topics, subscriptions and rules via the Azure Resource Manager, you would use the below package:

|    Library    |    Reference    |    Source    |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|    [azure-mgmt-servicebus](https://pypi.org/project/azure-mgmt-servicebus/)    |    [Reference](https://docs.microsoft.com/python/api/overview/azure/servicebus/management?view=azure-python)    |   [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-mgmt-servicebus)    |

## Next Steps

* [Service Bus documentation](https://docs.microsoft.com/azure/service-bus-messaging)
* [SDK source code](https://github.com/Azure/azure-sdk-for-python/tree/master/azure-servicebus)
* [SDK reference documentation](https://docs.microsoft.com/python/api/overview/azure/servicebus/client?view=azure-python)
* [Additional samples](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-servicebus/examples)
