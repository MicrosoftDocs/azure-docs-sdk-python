---
title: Azure Storage Queues client library for Python
keywords: Azure, Python, SDK, API, storage, azure-storage-queue
author: maggiepint
ms.author: magpint
ms.date: 04/16/2020
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: Python
ms.service: storage
---
 # Azure Storage Queues client library for Python - Version 12.1.1 


Azure Queue storage is a service for storing large numbers of messages that can be accessed from anywhere in the world via authenticated calls using HTTP or HTTPS. A single queue message can be up to 64 KiB in size, and a queue can contain millions of messages, up to the total capacity limit of a storage account.

Common uses of Queue storage include:

* Creating a backlog of work to process asynchronously
* Passing messages between different parts of a distributed application

[Source code](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/azure/storage/queue) | [Package (PyPI)](https://pypi.org/project/azure-storage-queue/) | [API reference documentation](https://aka.ms/azsdk-python-storage-queue-ref) | [Product documentation](https://docs.microsoft.com/azure/storage/) | [Samples](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples)

## Getting started

## 1: Set up your local development environment
 
If you haven't already, follow all the instructions on [Configure your local Python dev environment for Azure](https://docs.microsoft.com/azure/developer/python/configure-local-development-environment?tabs=bash).
 
Be sure to create a service principal for local development, and create and activate a virtual environment for this project.

## 2. Create a storage account

[Create a storage account](https://docs.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)

## 3. Install the package

```bash
pip install azure-storage-queue
```


## 4. Create the client
The Azure Storage Queues client library for Python allows you to interact with three types of resources: the storage
account itself, queues, and messages. Interaction with these resources starts with an instance of a [client](#clients).
To create a client object, you will need the storage account's queue service endpoint URL and a credential that allows
you to access the storage account:

```python
from azure.storage.queue import QueueServiceClient

service = QueueServiceClient(account_url="https://<my-storage-account-name>.queue.core.windows.net/", credential=new DefaultAzureCredential())
```

*Notes:* If you have created a service principal following the [configure your local environment documentation](https://docs.microsoft.com/azure/developer/python/configure-local-development-environment?tabs=bash), `Default Azure Credential` works without additional parameters. For additional configuration options see [Authorizing access to data in Azure Storage](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth?toc=/azure/storage/queues/toc.json).

You can find the storage account's queue service URL using the [Azure Portal](https://docs.microsoft.com/azure/storage/common/storage-account-overview#storage-account-endpoints).


## Examples

The following sections provide several code snippets covering some of the most common Storage Queue tasks, including:

* [Creating a queue](#creating-a-queue "Creating a queue")
* [Sending messages](#sending-messages "Sending messages")
* [Receiving messages](#receiving-messages "Receiving messages")

### Creating a queue
Create a queue in your storage account

```python
from azure.storage.queue import QueueClient

queue = QueueClient.from_connection_string(conn_str="<connection_string>", queue_name="my_queue")
queue.create_queue()
```

Use the async client to create a queue
```python
from azure.storage.queue.aio import QueueClient

queue = QueueClient.from_connection_string(conn_str="<connection_string>", queue_name="my_queue")
await queue.create_queue()
```

### Sending messages
Send messages to your queue

```python
from azure.storage.queue import QueueClient

queue = QueueClient.from_connection_string(conn_str="<connection_string>", queue_name="my_queue")
queue.send_message("I'm using queues!")
queue.send_message("This is my second message")
```

Send messages asynchronously

```python
import asyncio
from azure.storage.queue.aio import QueueClient

queue = QueueClient.from_connection_string(conn_str="<connection_string>", queue_name="my_queue")
await asyncio.gather(
    queue.send_message("I'm using queues!"),
    queue.send_message("This is my second message")
)
```

### Receiving messages
Receive and process messages from your queue

```python
from azure.storage.queue import QueueClient

queue = QueueClient.from_connection_string(conn_str="<connection_string>", queue_name="my_queue")
response = queue.receive_messages()

for message in response:
    print(message.content)
    queue.delete_message(message)

# Printed messages from the front of the queue:
# >> I'm using queues!
# >> This is my second message
```

Receive and process messages in batches

```python
from azure.storage.queue import QueueClient

queue = QueueClient.from_connection_string(conn_str="<connection_string>", queue_name="my_queue")
response = queue.receive_messages(messages_per_page=10)

for message_batch in response.by_page():
    for message in message_batch:
        print(message.content)
        queue.delete_message(message)
```

Receive and process messages asynchronously

```python
from azure.storage.queue.aio import QueueClient

queue = QueueClient.from_connection_string(conn_str="<connection_string>", queue_name="my_queue")
response = queue.receive_messages()

async for message in response:
    print(message.content)
    await queue.delete_message(message)
```


## Understanding the Examples
The following components make up the Azure Queue Service:
* The storage account itself
* A queue within the storage account, which contains a set of messages
* A message within a queue, in any format, of up to 64 KiB

The Azure Storage Queues client library for Python - Version 12.1.1 
 allows you to interact with each of these components through the
use of a dedicated client object.

### Clients
Two different clients are provided to to interact with the various components of the Queue Service:
1. [QueueServiceClient](https://aka.ms/azsdk-python-storage-queue-queueserviceclient) -
    this client represents interaction with the Azure storage account itself, and allows you to acquire preconfigured
    client instances to access the queues within. It provides operations to retrieve and configure the account
    properties as well as list, create, and delete queues within the account. To perform operations on a specific queue,
    retrieve a client using the `get_queue_client` method.
2. [QueueClient](https://aka.ms/azsdk-python-storage-queue-queueclient) -
    this client represents interaction with a specific queue (which need not exist yet). It provides operations to
    create, delete, or configure a queue and includes operations to send, receive, peek, delete, and update messages
    within it.

### Messages
* **Send** - Adds a message to the queue and optionally sets a visibility timeout for the message.
* **Receive** - Retrieves a message from the queue and makes it invisible to other consumers.
* **Peek** - Retrieves a message from the front of the queue, without changing the message visibility.
* **Update** - Updates the visibility timeout of a message and/or the message contents.
* **Delete** - Deletes a specified message from the queue.
* **Clear** - Clears all messages from the queue.

## Optional Configuration

Optional keyword arguments that can be passed in at the client and per-operation level. 

### Retry Policy configuration

Use the following keyword arguments when instantiating a client to configure the retry policy:

* __retry_total__ (int): Total number of retries to allow. Takes precedence over other counts.
Pass in `retry_total=0` if you do not want to retry on requests. Defaults to 10.
* __retry_connect__ (int): How many connection-related errors to retry on. Defaults to 3.
* __retry_read__ (int): How many times to retry on read errors. Defaults to 3.
* __retry_status__ (int): How many times to retry on bad status codes. Defaults to 3.
* __retry_to_secondary__ (bool): Whether the request should be retried to secondary, if able.
This should only be enabled of RA-GRS accounts are used and potentially stale data can be handled.
Defaults to `False`.

### Other client / per-operation configuration

Other optional configuration keyword arguments that can be specified on the client or per-operation.

**Client keyword arguments:**

* __connection_timeout__ (int): Optionally sets the connect and read timeout value, in seconds.
* __transport__ (Any): User-provided transport to send the HTTP request.

**Per-operation keyword arguments:**

* __raw_response_hook__ (callable): The given callback uses the response returned from the service.
* __raw_request_hook__ (callable): The given callback uses the request before being sent to service.
* __client_request_id__ (str): Optional user specified identification of the request.
* __user_agent__ (str): Appends the custom value to the user-agent header to be sent with the request.
* __logging_enable__ (bool): Enables logging at the DEBUG level. Defaults to False. Can also be passed in at
the client level to enable it for all requests.
* __headers__ (dict): Pass in custom headers as key, value pairs. E.g. `headers={'CustomValue': value}`


## Troubleshooting
### General
Storage Queue clients raise exceptions defined in [Azure Core](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/core/azure-core/README.md).
All Queue service operations will throw a `StorageErrorException` on failure with helpful [error codes](https://docs.microsoft.com/rest/api/storageservices/queue-service-error-codes).

### Logging
This library uses the standard
[logging](https://docs.python.org/3/library/logging.html) library for logging.
Basic information about HTTP sessions (URLs, headers, etc.) is logged at INFO
level.

Detailed DEBUG level logging, including request/response bodies and unredacted
headers, can be enabled on a client with the `logging_enable` argument:
```python
import sys
import logging
from azure.storage.queue import QueueServiceClient

# Create a logger for the 'azure.storage.queue' SDK
logger = logging.getLogger('azure.storage.queue')
logger.setLevel(logging.DEBUG)

# Configure a console output
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

# This client will log detailed information about its HTTP sessions, at DEBUG level
service_client = QueueServiceClient.from_connection_string("your_connection_string", logging_enable=True)
```

Similarly, `logging_enable` can enable detailed logging for a single operation,
even when it isn't enabled for the client:
```py
service_client.get_service_stats(logging_enable=True)
```

## Next steps
### More sample code

Get started with our [Queue samples](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples).

Several Storage Queues Python SDK samples are available to you in the SDK's GitHub repository. These samples provide example code for additional scenarios commonly encountered while working with Storage Queues:

* [queue_samples_hello_world.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples/queue_samples_hello_world.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples/queue_samples_hello_world_async.py)) - Examples found in this article:
    * Client creation
    * Create a queue
    * Send messages
    * Receive messages

* [queue_samples_authentication.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples/queue_samples_authentication.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples/queue_samples_authentication_async.py)) - Examples for authenticating and creating the client:
    * From a connection string
    * From a shared access key
    * From a shared access signature token
    * From Azure Active Directory

* [queue_samples_service.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples/queue_samples_service.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples/queue_samples_service_async.py)) - Examples for interacting with the queue service:
    * Get and set service properties
    * List queues in a storage account
    * Create and delete a queue from the service
    * Get the QueueClient

* [queue_samples_message.py](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples/queue_samples_message.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue/samples/queue_samples_message_async.py)) - Examples for working with queues and messages:
    * Set an access policy
    * Get and set queue metadata
    * Send and receive messages
    * Delete specified messages and clear all messages
    * Peek and update messages
    
### Additional documentation
For more extensive documentation on Azure Queue storage, see the [Azure Queue storage documentation](https://docs.microsoft.com/azure/storage/queues/) on docs.microsoft.com.

## Contributing
This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
