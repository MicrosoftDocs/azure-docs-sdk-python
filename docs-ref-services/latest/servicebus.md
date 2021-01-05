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

# Service Bus libraries for Python

Microsoft Azure Service Bus supports a set of cloud-based, message-oriented middleware technologies including reliable message queuing and durable publish/subscribe messaging.

## Libraries for data access

The latest version of the Azure Servicebus libraries is version 7.x.x. We highly recommend using version 7.x.x for new applications.

To update existing applications to version 7.x.x, please follow the [migration guide](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/servicebus/azure-servicebus/migration_guide.md)

### Version 7.x.x

The version 7.x.x client libraries for Python are part of the Azure SDK for Python. The source code for the Azure ServiceBus client libraries for Python is available on [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus).

Use the following version 7.x.x libraries to manage your Azure Service Bus resources like namespaces, queues, topics, subscriptions and rules via the Azure Resource Manager, you would use the below package:

| Library | Reference | Package | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    azure-servicebus   |    [Reference](https://docs.microsoft.com/python/api/overview/azure/servicebus-readme?view=azure-python)    |    [PyPI](https://pypi.org/project/azure-servicebus/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-servicebus)    |

### Version 0.50.x

The older verson allows you to send and receive messages from an Azure Service Bus queue, topic or subscription, but it lacks a lot of the new features and performance improvements available in the latest version of the same package.

The source code for the Azure Servicebus client libraries for Python is available on [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/servicebus_v0.50.3/sdk/servicebus/azure-servicebus/).

| Library | Reference | Package | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    azure-servicebus   |    [Reference](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-servicebus/0.50.3/index.html)    |    [PyPI](https://pypi.org/project/azure-servicebus/0.50.3/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/servicebus_v0.50.3/sdk/servicebus/azure-servicebus/)    |

## Libraries for resource management

Use the following library to work with the Azure Servicebus resource provider:

|    Library    |    Reference    |    Package    |    Source    |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|    azure-mgmt-servicebus    |    [Reference](https://docs.microsoft.com/python/api/overview/azure/servicebus/management?view=azure-python)    |    [PyPI](https://pypi.org/project/azure-mgmt-servicebus/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-mgmt-servicebus)    |

## Next Steps

* [Service Bus documentation](https://docs.microsoft.com/azure/service-bus-messaging)
* [SDK source code](https://github.com/Azure/azure-sdk-for-python/tree/master/azure-servicebus)
* [SDK reference documentation](https://docs.microsoft.com/python/api/overview/azure/servicebus/client?view=azure-python)
* [Additional samples](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-servicebus/examples)
