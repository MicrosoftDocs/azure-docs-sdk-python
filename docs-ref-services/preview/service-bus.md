---
title: Azure Service Bus SDK for Python
description: Reference for Azure Service Bus SDK for Python
ms.date: 07/24/2024
ms.topic: reference
ms.devlang: python
ms.service: service-bus-messaging
keywords: Azure, Python, SDK, API, messaging, pubsub, pub-sub, message broker
manager: mayurid
---
# Service Bus libraries for Python

Microsoft Azure Service Bus supports a set of cloud-based, message-oriented middleware technologies including reliable message queuing and durable publish/subscribe messaging.

* [SDK source code](https://github.com/Azure/azure-sdk-for-python/tree/master/azure-servicebus)
* [SDK reference documentation](https://docs.microsoft.com/python/api/overview/azure/servicebus/client?view=azure-python)

## What's new in v0.50.0?

As of version 0.50.0 a new AMQP-based API is available for sending and receiving messages. This update involves **breaking changes**.

Please read [Migration from v0.21.1 to v0.50.0](#migration-from-v0211-to-v0500) to determine if upgrading is
right for you at this time.

The new AMQP-based API offers improved message passing reliability, performance and expanded feature support going forward.
The new API also offers support for asynchronous operations (based on asyncio) for sending, receiving and handling messages.

For documentation on the legacy HTTP-based operations please see [Using HTTP-based operations of the legacy API](#using-http-based-operations-of-the-legacy-api).

## Prerequisites

* Azure subscription - [Create a free account](https://azure.microsoft.com/free/)
* Azure [Service Bus namespace and management credentials](https://docs.microsoft.com/azure/service-bus-messaging/service-bus-create-namespace-portal)
* [Python 2.7-3.7](https://www.python.org/downloads/)

## Installation

```bash
pip install azure-servicebus
```

## Connect to Azure Service Bus

### Get credentials

Use the Azure CLI snippet below to populate an environment variable with the Service Bus connection string (you can also find this value in the Azure portal). The snippet is formatted for the Bash shell.

```Bash
RES_GROUP=<resource-group-name>
NAMESPACE=<servicebus-namespace>

export SB_CONN_STR=$(az servicebus namespace authorization-rule keys list \
 --resource-group $RES_GROUP \
 --namespace-name $NAMESPACE \
 --name RootManageSharedAccessKey \
 --query primaryConnectionString \
 --output tsv)
```

### Create client

Once you've populated the `SB_CONN_STR` environment variable, you can create the ServiceBusClient.

```python
import os
from azure.servicebus import ServiceBusClient

connection_str = os.environ['SB_CONN_STR']

sb_client = ServiceBusClient.from_connection_string(connection_str)
```

If you wish to use asynchronous operations, please use the `azure.servicebus.aio` namespace.

```python
import os
from azure.servicebus.aio import ServiceBusClient

connection_str = os.environ['SB_CONN_STR']

sb_client = ServiceBusClient.from_connection_string(connection_str)
```

For more examples of asynchronous operations, please explore [Service Bus samples](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/servicebus/azure-servicebus/samples/async_samples) at the azure-sdk-for-python repository.

## Service Bus queues

Service Bus queues are an alternative to Storage queues that might be useful in scenarios where more advanced messaging features are needed (larger message sizes, message ordering, single-operation destructive reads, scheduled delivery) using push-style delivery (using long polling).

### Create queue

This creates a new queue within the Service Bus namespace. If a queue of the same name already exists within the namespace an error will be raised.

```python
sb_client.create_queue("MyQueue")
```

Optional parameters to configure the queue behavior can also be specified.

```python
sb_client.create_queue(
    "MySessionQueue",
    requires_session=True, # Create a sessionful queue
    max_delivery_count=5   # Max delivery attempts per message
)
```

### Get a queue client

A QueueClient can be used to send and receive messages from the queue, along with other operations.

```python
queue_client = sb_client.get_queue("MyQueue")
```

### Sending messages

The queue client can send one or more messages at a time:

```python
from azure.servicebus import Message

message = Message("Hello World")
queue_client.send(message)

message_one = Message("First")
message_two = Message("Second")
queue_client.send([message_one, message_two])
```

Each call to QueueClient.send will create a new service connection. To reuse the same connection for multiple send calls, you can open a sender:

```python
message_one = Message("First")
message_two = Message("Second")

with queue_client.get_sender() as sender:
    sender.send(message_one)
    sender.send(message_two)
```

If you are using an asynchronous client, the above operations will use async syntax:

```python
from azure.servicebus.aio import Message

message = Message("Hello World")
await queue_client.send(message)

message_one = Message("First")
message_two = Message("Second")
async with queue_client.get_sender() as sender:
    await sender.send(message_one)
    await sender.send(message_two)
```

### Receiving messages

Messages can be received from a queue as a continuous iterator. The default mode for message receiving is [PeekLock](https://docs.microsoft.com/rest/api/servicebus/peek-lock-message-non-destructive-read), which requires each message to be explicitly completed in order that it be removed from the queue.

```python
messages = queue_client.get_receiver()
for message in messages:
    print(message)
    message.complete()
```

The service connection will remain open for the entirety of the iterator. If you find yourself only partially iterating the message stream, you should run the receiver in a `with` statement to ensure the connection is closed:

```python
with queue_client.get_receiver() as messages:
    for message in messages:
        print(message)
        message.complete()
        break
```
If you are using an asynchronous client, the above operations will use async syntax:

```python
async with queue_client.get_receiver() as messages:
    async for message in messages:
        print(message)
        await message.complete()
        break
```

## Service Bus topics and subscriptions

Service Bus topics and subscriptions are an abstraction on top of Service Bus queues that provide a one-to-many form of communication, in a publish/subscribe pattern. Messages are sent to a topic and delivered to one or more associated subscriptions, which is useful for scaling to large numbers of recipients.

### Create topic

This creates a new topic within the Service Bus namespace. If a topic of the same name already exists an error will be raised.

```python
sb_client.create_topic("MyTopic")
```

### Get a topic client

A TopicClient can be used to send messages to the topic, along with other operations.

```python
topic_client = sb_client.get_topic("MyTopic")
```

### Create subscription

This creates a new subscription for the specified topic within the Service Bus namespace.

```python
sb_client.create_subscription("MyTopic", "MySubscription")
```

### Get a subscription client

A SubscriptionClient can be used to receive messages from the topic, along with other operations.

```python
topic_client = sb_client.get_subscription("MyTopic", "MySubscription")
```

## Migration from v0.21.1 to v0.50.0

Major breaking changes were introduced in version 0.50.0. The original HTTP-based API is still available in v0.50.0 - however it now exists under a new namesapce: `azure.servicebus.control_client`.

### Should I upgrade?

The new package (v0.50.0) offers no improvements in HTTP-based operations over v0.21.1. The HTTP-based API is identical except that it now exists under a new namespace. For this reason if you only wish to use HTTP-based operations (`create_queue`, `delete_queue` etc) - there will be no additional benefit in upgrading at this time.

### How do I migrate my code to the new version?

Code written against v0.21.0 can be ported to version 0.50.0 by simply changing the import namespace:

```python
# from azure.servicebus import ServiceBusService  <- This will now raise an ImportError
from azure.servicebus.control_client import ServiceBusService

key_name = 'RootManageSharedAccessKey' # SharedAccessKeyName from Azure portal
key_value = '' # SharedAccessKey from Azure portal
sbs = ServiceBusService(service_namespace,
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value)
```

## Using HTTP-based operations of the legacy API

The following documentation describes the legacy API and should be used for those wishing to port existing code to v0.50.0 without making any additional changes. This reference can also be used as guidance by those using v0.21.1.
For those writing new code, we recommend using the new API described above.

### Service Bus queues

#### Shared Access Signature (SAS) authentication

To use Shared Access Signature authentication, create the service bus
service with:

```python
from azure.servicebus.control_client import ServiceBusService

key_name = 'RootManageSharedAccessKey' # SharedAccessKeyName from Azure portal
key_value = '' # SharedAccessKey from Azure portal
sbs = ServiceBusService(service_namespace,
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value)
```

#### Access Control Service (ACS) authentication

ACS is not supported on new Service Bus namespaces. We recommend [migrating applications to SAS authentication](https://docs.microsoft.com/azure/service-bus-messaging/service-bus-migrate-acs-sas). To use ACS authentication within an older Service Bus namesapce, create the ServiceBusService with:

```python
from azure.servicebus.control_client import ServiceBusService

account_key = '' # DEFAULT KEY from Azure portal
issuer = 'owner' # DEFAULT ISSUER from Azure portal
sbs = ServiceBusService(service_namespace,
                        account_key=account_key,
                        issuer=issuer)
```

#### Sending and receiving messages

The **create\_queue** method can be used to ensure a queue exists:

```python
sbs.create_queue('taskqueue')
```

The **send\_queue\_message** method can then be called to insert the message into the queue:

```python
from azure.servicebus.control_client import Message

msg = Message('Hello World!')
sbs.send_queue_message('taskqueue', msg)
```

The **send\_queue\_message_batch** method can then be called to  send several messages at once:

```python
from azure.servicebus.control_client import Message

msg1 = Message('Hello World!')
msg2 = Message('Hello World again!')
sbs.send_queue_message_batch('taskqueue', [msg1, msg2])
```

It is then possible to call the **receive\_queue\_message** method to dequeue the message.

```python
msg = sbs.receive_queue_message('taskqueue')
```

### Service Bus topics

The **create\_topic** method can be used to create a server-side topic:

```python
sbs.create_topic('taskdiscussion')
```

The **send\_topic\_message** method can be used to send a message to a topic:

```python
from azure.servicebus.control_client import Message

msg = Message(b'Hello World!')
sbs.send_topic_message('taskdiscussion', msg)
```

The **send\_topic\_message_batch** method can be used to send  several messages at once:

```python
from azure.servicebus.control_client import Message

msg1 = Message(b'Hello World!')
msg2 = Message(b'Hello World again!')
sbs.send_topic_message_batch('taskdiscussion', [msg1, msg2])
```

Please consider that in Python 3 a str message will be utf-8 encoded and you should have to manage your encoding yourself in Python 2.

A client can then create a subscription and start consuming messages by calling the **create\_subscription** method followed by the **receive\_subscription\_message** method. Please note that any messages sent before the subscription is created will not be received.

```python
from azure.servicebus.control_client import Message

sbs.create_subscription('taskdiscussion', 'client1')
msg = Message('Hello World!')
sbs.send_topic_message('taskdiscussion', msg)
msg = sbs.receive_subscription_message('taskdiscussion', 'client1')
```

### Event Hub

Event Hubs enable the collection of event streams at high throughput, from a diverse set of devices and services.

The **create\_event\_hub** method can be used to create an event hub:

```python
sbs.create_event_hub('myhub')
```

To send an event:

```python
sbs.send_event('myhub', '{ "DeviceId":"dev-01", "Temperature":"37.0" }')
```

The event content is the event message or JSON-encoded string that contains multiple messages.

### Advanced features

#### Broker properties and user properties

This section describes how to use Broker and User properties defined [here](https://docs.microsoft.com/rest/api/servicebus/message-headers-and-properties):

```python
sent_msg = Message(b'This is the third message',
                   broker_properties={'Label': 'M3'},
                   custom_properties={'Priority': 'Medium',
                                      'Customer': 'ABC'}
            )
```

You can use datetime, int, float or boolean

```python
props = {'hello': 'world',
         'number': 42,
         'active': True,
         'deceased': False,
         'large': 8555111000,
         'floating': 3.14,
         'dob': datetime(2011, 12, 14),
         'double_quote_message': 'This "should" work fine',
         'quote_message': "This 'should' work fine"}
sent_msg = Message(b'message with properties', custom_properties=props)
```

For compatibility reason with old version of this library,  `broker_properties` could also be defined as a JSON string.
If this situation, you're responsible to write a valid JSON string, no check will be made by Python before sending to the RestAPI.

```python
broker_properties = '{"ForcePersistence": false, "Label": "My label"}'
sent_msg = Message(b'receive message',
                   broker_properties = broker_properties
)
```

## Next Steps

* [Service Bus documentation](https://docs.microsoft.com/azure/service-bus-messaging)
* [SDK source code](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/servicebus)
* [SDK reference documentation](/python/api/overview/azure/servicebus-readme)
* [Additional samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/servicebus/azure-servicebus/samples)