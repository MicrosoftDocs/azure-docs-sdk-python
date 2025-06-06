---
title: Azure Communication Messages Package client library for Python
keywords: Azure, python, SDK, API, azure-communication-messages, communication
ms.date: 02/11/2025
ms.topic: reference
ms.devlang: python
ms.service: communication
---
# Azure Communication Messages Package client library for Python - version 1.2.0b1 


This package contains a Python SDK for Azure Communication Services for Messages(Advanced Messaging).
Read more about Azure Communication Services [here][product_docs]

[Source code][source] | [Package (Pypi)][pypi] | [Product documentation][product_docs]

## _Disclaimer_

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to https://github.com/Azure/azure-sdk-for-python/issues/20691_

## Getting started

### Prequisites

- Python 3.8 or later is required to use this package.
- You need an [Azure subscription][azure_sub] to use this package.
- An existing Communication Messages instance.

## Key concepts

Azure Communication Services enables you to send and receive WhatsApp messages using the Azure Communication Services Messages SDK. It can be used to send out messages like appointment reminders, shipping updates, two-factor authentication, and other notification scenarios.

### Installating the package

```bash
python -m pip install azure-communication-messages
```

### Create with an Azure Active Directory Credential

To use an [Azure Active Directory (AAD) token credential][authenticate_with_token],
provide an instance of the desired credential type obtained from the
[azure-identity][azure_identity_credentials] library.

To authenticate with AAD, you must first [pip][pip] install [`azure-identity`][azure_identity_pip]

After setup, you can choose which type of [credential][azure_identity_credentials] from azure.identity to use.
As an example, [DefaultAzureCredential][default_azure_credential] can be used to authenticate the client:

Set the values of the client ID, tenant ID, and client secret of the AAD application as environment variables:
`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET`

Use the returned token credential to authenticate the client:

```python
>>> from azure.communication.messages import NotificationMessagesClient
>>> from azure.identity import DefaultAzureCredential
>>> client = NotificationMessagesClient(endpoint='<endpoint>', credential=DefaultAzureCredential())
```

### Examples

Send Text WhatsApp message using AdvancedMessages python SDK.
```python
import os
import sys

sys.path.append("..")

class SendWhatsAppMessageSample(object):

    connection_string = os.getenv("COMMUNICATION_SAMPLES_CONNECTION_STRING")
    phone_number = os.getenv("RECIPIENT_PHONE_NUMBER")
    channel_id = os.getenv("WHATSAPP_CHANNEL_ID")

    def send_text_send_message(self):

        from azure.communication.messages import NotificationMessagesClient
        from azure.communication.messages.models import TextNotificationContent
        from azure.identity import DefaultAzureCredential

        messaging_client = NotificationMessagesClient(
            endpoint=self.endpoint_string, credential=DefaultAzureCredential()
        )
        text_options = TextNotificationContent(
            channel_registration_id=self.channel_id,
            to=[self.phone_number],
            content="Hello World via Notification Messaging SDK.",
        )

        # calling send() with whatsapp message details
        message_responses = messaging_client.send(text_options)
        response = message_responses.receipts[0]
        print("Message with message id {} was successful sent to {}".format(response.message_id, response.to))


if __name__ == "__main__":
    sample = SendWhatsAppMessageSample()
    sample.send_text_send_message()

```

## Troubleshooting

Running into issues? This section should contain details as to what to do there.

## Next steps

- [Read more about Azure Communication Services Messages][nextsteps]

## Contributing

This project welcomes contributions and suggestions. Most contributions require
you to agree to a Contributor License Agreement (CLA) declaring that you have
the right to, and actually do, grant us the rights to use your contribution.
For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether
you need to provide a CLA and decorate the PR appropriately (e.g., label,
comment). Simply follow the instructions provided by the bot. You will only
need to do this once across all repos using our CLA.

This project has adopted the
[Microsoft Open Source Code of Conduct][code_of_conduct]. For more information,
see the Code of Conduct FAQ or contact opencode@microsoft.com with any
additional questions or comments.

<!-- LINKS -->
[code_of_conduct]: https://opensource.microsoft.com/codeofconduct/
[authenticate_with_token]: https://learn.microsoft.com/azure/cognitive-services/authentication?tabs=powershell#authenticate-with-an-authentication-token
[azure_identity_credentials]: https://github.com/Azure/azure-sdk-for-python/tree/azure-communication-messages_1.2.0b1/sdk/identity/azure-identity#credentials
[azure_identity_pip]: https://pypi.org/project/azure-identity/
[default_azure_credential]: https://github.com/Azure/azure-sdk-for-python/tree/azure-communication-messages_1.2.0b1/sdk/identity/azure-identity#defaultazurecredential
[pip]: https://pypi.org/project/pip/
[azure_sub]: https://azure.microsoft.com

[source]: https://github.com/Azure/azure-sdk-for-python/blob/azure-communication-messages_1.2.0b1/sdk/communication/azure-communication-messages
[product_docs]: https://learn.microsoft.com/azure/communication-services/overview
[pypi]: https://pypi.org
[nextsteps]: https://learn.microsoft.com/azure/communication-services/quickstarts/advanced-messaging/whatsapp/get-started

