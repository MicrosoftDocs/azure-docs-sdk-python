---
title: Service Bus libraries for Python 
description: Reference documentation for the Python client and management libraries for Service Bus
keywords: Azure, Python, SDK, API, messaging, pubsub, pub-sub, message broker
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/26/2017
ms.topic: article
ms.devlang: python
ms.service: service-bus
---

# Service Bus libraries for Python

## Overview

Microsoft Azure Service Bus supports a set of cloud-based, message-oriented middleware technologies including reliable message queuing and durable publish/subscribe messaging. 

## Install the libraries
```bash
pip install azure-mgmt-servicebus
```

## Example
Send messages to a queue.

```python
from azure.servicebus import Message

msg1 = Message('Hello World!')
msg2 = Message('Hello World again!')
sbs.send_queue_message_batch('taskqueue', [msg1, msg2])
# dequeue the message
msg = sbs.receive_queue_message('taskqueue')
```
> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/overview/azure/servicebus/managementlibrary)

