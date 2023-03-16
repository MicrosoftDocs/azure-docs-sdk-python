---
title: Azure Communication Phone Numbers Package client library for Python
keywords: Azure, python, SDK, API, azure-communication-phonenumbers, communication
description: Purchase Numbers for direct offer or direct routing. Configure number calling capabilities. Configure direct routing in order to connect customer-provided telephony infrastructure to Azure Communication Resources
author: ramya-rao-a
ms.author: nostojic
ms.date: 03/16/2023
ms.topic: reference
ms.prod: azure
ms.devlang: python
ms.service: communication
---

# Azure Communication Phone Numbers Package client library for Python - version 1.2.0


The phone numbers library provides capabilities for phone number administration.

Purchased phone numbers can come with many capabilities, depending on the country, number type and assignment type. Examples of capabilities are SMS inbound and outbound usage, PSTN inbound and outbound usage. Phone numbers can also be assigned to a bot via a webhook URL.

## Getting started

### Prerequisites

- Python 2.7, or 3.6 or later is required to use this package.
- You must have an [Azure subscription](https://azure.microsoft.com/free/)
- A deployed Communication Services resource. You can use the [Azure Portal](https://docs.microsoft.com/azure/communication-services/quickstarts/create-communication-resource?tabs=windows&pivots=platform-azp) or the [Azure PowerShell](https://docs.microsoft.com/powershell/module/az.communication/new-azcommunicationservice) to set it up.

### Installing

Install the Azure Communication Phone Numbers client library for Python with [pip](https://pypi.org/project/pip/):

```bash
pip install azure-communication-phonenumbers
```

## Key concepts

This SDK provides functionality to easily manage `direct offer` and `direct routing` numbers.

The `direct offer` numbers come in two types: Geographic and Toll-Free. Geographic phone plans are phone plans associated with a location, whose phone numbers' area codes are associated with the area code of a geographic location. Toll-Free phone plans are phone plans not associated location. For example, in the US, toll-free numbers can come with area codes such as 800 or 888. They are managed using the PhoneNumbersClient

The `direct routing` feature enables connecting your existing telephony infrastructure to ACS. The configuration is managed using the SipRoutingClient. Client provides methods for setting up SIP trunks and voice routing rules, in order to properly handle calls for your telephony subnet.

## Phone number client

### Phone number types

Phone numbers come in two types; Geographic and Toll-Free. Geographic phone numbers are phone numbers associated with a location, whose area codes are associated with the area code of a geographic location. Toll-Free phone numbers are not associated with a location. For example, in the US, toll-free numbers can come with area codes such as 800 or 888.

All geographic phone numbers within the same country are grouped into a phone plan group with a Geographic phone number type. All Toll-Free phone numbers within the same country are grouped into a phone plan group.

### Searching and acquiring numbers

Phone numbers can be searched through the search creation API by providing a phone number type (geographic or toll-free), assignment type (person or application), calling and sms capabilities, an area code and quantity of phone numbers. The provided quantity of phone numbers will be reserved for 15 minutes. This search of phone numbers can either be canceled or purchased. If the search is canceled, then the phone numbers become available to others. If the search is purchased, then the phone numbers are acquired for the Azure resource.

### Configuring phone numbers

Phone numbers can have a combination of capabilities. They can be configured to support inbound and/or outbound calling, or neither if you won't use the phone number for calling. The same applies to sms capabilities.

It is important to consider the assignment type of your phone number. Some capabilities are restricted to a particular assignment type.

## Sip routing client

Direct routing feature allows connecting customer-provided telephony infrastructure to Azure Communication Resources. In order to set up routing configuration properly, customer needs to supply the SIP trunk configuration and SIP routing rules for calls. SIP routing client provides the necessary interface for setting this configuration.

When call is made, system tries to match the destination number with regex number patterns of defined routes. The first route to match the number will be selected. The order of regex matching is the same as the order of routes in configuration, therefore the order of routes matters. Once a route is matched, the call is routed to the first trunk in the route's trunks list. If the trunk is not available, next trunk in the list is selected.

## Examples

## Authentication

To create a client object to access the Communication Services API, you need a `connection string` or the `endpoint` of your Communication Services resource and a `credential`. The Phone Numbers client can use either Azure Active Directory credentials or an API key credential to authenticate.

You can get a key and/or connection string from your Communication Services resource in the [Azure portal][azure_portal]. You can also find the endpoint for your Communication Services resource in the [Azure portal][azure_portal].

Once you have a key, you can authenticate the `PhoneNumbersClient` with any of the following methods:

### Using a connection string

```python
# You can find your connection string from your resource in the Azure Portal
import os
from azure.communication.phonenumbers import PhoneNumbersClient

connection_str = "endpoint=ENDPOINT;accessKey=KEY"
phone_numbers_client = PhoneNumbersClient.from_connection_string(connection_str)
```

```python
# You can find your connection string from your resource in the Azure Portal
import os
from azure.communication.siprouting import SipRoutingClient

connection_str = "endpoint=ENDPOINT;accessKey=KEY"
sip_routing_client = SipRoutingClient.from_connection_string(connection_str)
```

### Using an Azure Active Directory Credential

Connection string authentication is used in most of the examples, but you can also authenticate with Azure Active Directory using the [Azure Identity library][azure_identity]. To use the [DefaultAzureCredential][defaultazurecredential] provider shown below, or other credential providers provided with the Azure SDK install the [`azure-identity`][azure_identity] package:

```bash
pip install azure-identity
```

```python
# You can find your connection string from your resource in the Azure Portal
import os
from azure.communication.phonenumbers import PhoneNumbersClient
from azure.identity import DefaultAzureCredential

endpoint = "https://<RESOURCE_NAME>.communication.azure.com"
# To use Azure Active Directory Authentication (DefaultAzureCredential) make sure to have your
# AZURE_TENANT_ID, AZURE_CLIENT_ID and AZURE_CLIENT_SECRET as env variables.
phone_numbers_client = PhoneNumbersClient(endpoint, DefaultAzureCredential())
```

```python
# You can find your connection string from your resource in the Azure Portal
import os
from azure.communication.siprouting import SipRoutingClient
from azure.identity import DefaultAzureCredential

endpoint = "https://<RESOURCE_NAME>.communication.azure.com"
# To use Azure Active Directory Authentication (DefaultAzureCredential) make sure to have your
# AZURE_TENANT_ID, AZURE_CLIENT_ID and AZURE_CLIENT_SECRET as env variables.
sip_routing_client = SipRoutingClient(endpoint, DefaultAzureCredential())
```

## Usage

The following sections provide code snippets that cover some of the common tasks using the Azure Communication Services Phone Numbers client. The scenarios that are covered here consist of:

PhoneNumbersClient

- [Search for available phone numbers](#search-for-available-phone-numbers)
- [Purchase phone numbers from a search](#purchase-phone-numbers-from-a-search)
- [Release a purchased phone number](#release-a-purchased-phone-number)
- [Update phone number capabilities](#update-phone-number-capabilities)
- [Get a purchased phone number](#get-a-purchased-phone-number)
- [List purchased phone numbers](#list-purchased-phone-numbers)

SipRoutingClient

- [Retrieve SIP trunks and routes](#retrieve-sip-trunks-and-routes)
- [Replace SIP trunks and routes](#replace-sip-trunks-and-routes)
- [Retrieve single trunk](#retrieve-single-trunk)
- [Set single trunk](#set-single-trunk)
- [Delete single trunk](#delete-single-trunk)

## PhoneNumbersClient

### Search for available phone numbers

You can search for available phone numbers by providing the capabilities of the phone you want to acquire, the phone number type, the assignment type, and the country code. It's worth mentioning that for the toll-free phone number type, proving the area code is optional.
The result of the search can then be used to purchase the number in the corresponding API.

```python
capabilities = PhoneNumberCapabilities(
        calling = PhoneNumberCapabilityType.INBOUND,
        sms = PhoneNumberCapabilityType.INBOUND_OUTBOUND
    )
poller = phone_numbers_client.begin_search_available_phone_numbers(
    "US",
    PhoneNumberType.TOLL_FREE,
    PhoneNumberAssignmentType.APPLICATION,
    capabilities,
    area_code ="833", # Area code is optional for toll-free numbers
    quantity = 2, # Quantity is optional. If not set, default is 1
    polling = True
)
search_result = poller.result()
```

### Purchase phone numbers from a search

The result of your search can be used to purchase the specified phone numbers. This can be done by passing the `search_id` from the search response to the purchase phone number API.

```python
purchase_poller = phone_numbers_client.begin_purchase_phone_numbers(
    search_result.search_id, 
    polling=True
)
```

### Release a purchased phone number

Releases an acquired phone number.

```python
poller = self.phone_number_client.begin_release_phone_number(
    "<phone number>", 
    polling = True
)
```

### Update phone number capabilities

Updates the specified phone number capabilities for Calling and SMS to one of: 

- `PhoneNumberCapabilityType.NONE`
- `PhoneNumberCapabilityType.INBOUND`
- `PhoneNumberCapabilityType.OUTBOUND`
- `PhoneNumberCapabilityType.INBOUND_OUTBOUND`

```python
poller = self.phone_number_client.begin_update_phone_number_capabilities(
    "<phone number>",
    PhoneNumberCapabilityType.OUTBOUND,
    PhoneNumberCapabilityType.INBOUND_OUTBOUND,
    polling = True
)
```

### Get a purchased phone number

Gets the information from the specified phone number

```python
result = phone_numbers_client.get_purchased_phone_number("<phone number>")
print(result.country_code)
print(result.phone_number)
```


### List Purchased Phone Numbers

Lists all of your purchased phone numbers

```python
purchased_phone_numbers = phone_numbers_client.list_purchased_phone_numbers()
for acquired_phone_number in purchased_phone_numbers:
    print(acquired_phone_number.phone_number)
```

## SipRoutingClient

### Retrieve SIP trunks and routes

List currently configured trunks or routes.

```python
trunks = sip_routing_client.list_trunks()
for trunk in trunks:
    print(trunk.fqdn)
    print(trunk.sip_signaling_port)
routes = sip_routing_client.list_routes()
for route in routes:
    print(route.name)
    print(route.description)
    print(route.number_pattern)
    for trunk_fqdn in route.trunks:
        print(trunk_fqdn)
```

### Replace SIP trunks and routes

Replace the list of currently configured trunks or routes with new values.

```python
new_trunks = [SipTrunk(fqdn="sbs1.contoso.com", sip_signaling_port=1122), SipTrunk(fqdn="sbs2.contoso.com", sip_signaling_port=1123)]
new_routes = [SipTrunkRoute(name="First rule", description="Handle numbers starting with '+123'", number_pattern="\+123[0-9]+", trunks=["sbs1.sipconfigtest.com"])]
sip_routing_client.set_trunks(new_trunks)
sip_routing_client.set_routes(new_routes)
```

### Retrieve single trunk

```python
trunk = sip_routing_client.get_trunk("sbs1.contoso.com")
```

### Set single trunk

```python
# Set function will either modify existing item or add new item to the collection.
# The trunk is matched based on it's FQDN.
new_trunk = SipTrunk(fqdn="sbs3.contoso.com", sip_signaling_port=5555)
sip_routing_client.set_trunk(new_trunk)
```

### Delete single trunk

```python
sip_routing_client.delete_trunk("sbs1.contoso.com")
```

## Troubleshooting

The Phone Numbers Administration client will raise exceptions defined in [Azure Core][azure_core].

## Next steps

## More sample code

Please take a look at the [samples](https://github.com/Azure/azure-sdk-for-python/tree/azure-communication-phonenumbers_1.0.1/sdk/communication/azure-communication-phonenumbers/samples) directory for detailed examples of how to use this library.

## Provide Feedback

If you encounter any bugs or have suggestions, please file an issue in the [Issues](https://github.com/Azure/azure-sdk-for-python/issues) section of the project

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the
PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Related projects

- [Microsoft Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)

<!-- LINKS -->
[azure_core]: https://github.com/Azure/azure-sdk-for-python/blob/azure-communication-phonenumbers_1.0.1/sdk/core/azure-core/README.md
[azure_portal]: https://portal.azure.com
[defaultazurecredential]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#defaultazurecredential
[azure_identity]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#identity
