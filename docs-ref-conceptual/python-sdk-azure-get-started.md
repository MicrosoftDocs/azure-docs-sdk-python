---
title: Get started with the Azure libraries for Python
description: Getting started with Aure libraries for Python
keywords: Azure, Python, SDK, API
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/05/2017
ms.topic: get-started
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: multiple
ms.assetid: 
---

# Get started with the Azure libraries for Python

This tutorial demonstrates the usage of several Azure libraries for Python.  You will set up authentication, create and use an Azure Storage account, create and use an Azure SQL Database, deploy some virtual machines, and deploy an Azure App Service Web App from GitHub.

## Prerequisites

- An Azure account. If you don't have one, [get a free trial](https://azure.microsoft.com/free/)
- [Azure CLI 2.0](https://docs.microsoft.com/cli/azure/install-az-cli2)
- [Python](https://www.python.org/downloads/)

## Set up authentication

The SDK is able to create a client using your CLI active subscription.

To define active credentials, use [az login](https://docs.microsoft.com/cli/azure/authenticate-azure-cli).
Default subscription ID is either the only one you have, or you can define it using 
[az account](https://docs.microsoft.com/cli/azure/manage-azure-subscriptions-azure-cli)

```python
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient

client = get_client_from_cli_profile(ComputeManagementClient)
```
## Create a virtual environment

> [!IMPORTANT]
> Create a virtual environment is optional, but we strongly suggest you to do it.

Create a virtual environment in Bash (Linux or [Bash for Windows](https://msdn.microsoft.com/commandline/wsl/about))
```bash
pip install virtualenv
virtualenv mytestenv
cd mytestenv
source ./bin/activate
```

Create a virtual environment in Powershell:
```powershell
pip install virtualenv
virtualenv mytestenv
cd mytestenv
.\Scripts\activate
```

> [!IMPORTANT]
> Note that if you use [VSCode](https://code.visualstudio.com/) and the [Python extension](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python),  you can start it using "code ." and get your environment configured.

## Create a Linux virtual machine
This code creates a new Linux VM with name `testLinuxVM` in a resource group `sampleResourceGroup` running in the US East Azure region.

```python
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.models import PublicIPAddress
from azure.mgmt.compute import ComputeManagementClient
from azure.common.client_factory import get_client_from_cli_profile

# Azure Datacenter
LOCATION = 'eastus'

# Resource Group
GROUP_NAME = 'sampleVmResourceGroup'

# Network
VNET_NAME = 'azure-sample-vnet'
SUBNET_NAME = 'azure-sample-subnet'

# VM
OS_DISK_NAME = 'azure-sample-osdisk'
STORAGE_ACCOUNT_NAME = 'azure-storage-account'

IP_CONFIG_NAME = 'azure-sample-ip-config'
NIC_NAME = 'azure-sample-nic'
VM_NAME = 'testLinuxVM'

USERNAME = 'userlogin'
PASSWORD = 'Pa$$w0rd91'

IP_ADDRESS_NAME='publicipaddress'

VM_REFERENCE = {
    'linux': {
        'publisher': 'Canonical',
        'offer': 'UbuntuServer',
        'sku': '16.04.0-LTS',
        'version': 'latest'
    },
    'windows': {
        'publisher': 'MicrosoftWindowsServerEssentials',
        'offer': 'WindowsServerEssentials',
        'sku': 'WindowsServerEssentials',
        'version': 'latest'
    }
}


def run_example():

    resource_client = get_client_from_cli_profile(ResourceManagementClient)
    compute_client = get_client_from_cli_profile(ComputeManagementClient)
    network_client = get_client_from_cli_profile(NetworkManagementClient)

    # Create Resource group
    print('\nCreate Resource Group')
    resource_client.resource_groups.create_or_update(GROUP_NAME, {'location': LOCATION})

    # Create a NIC
    nic = create_nic(network_client)

    # Create Linux VM
    print('\nCreating Linux Virtual Machine')
    vm_parameters = create_vm_parameters(nic.id, VM_REFERENCE['linux'])
    print(vm_parameters)
    async_vm_creation = compute_client.virtual_machines.create_or_update(
        GROUP_NAME, VM_NAME, vm_parameters)
    async_vm_creation.wait()

def create_nic(network_client):
    """Create a Network Interface for a VM.
    """
    # Create VNet
    print('\nCreate Vnet')
    async_vnet_creation = network_client.virtual_networks.create_or_update(
        GROUP_NAME,
        VNET_NAME,
        {
            'location': LOCATION,
            'address_space': {
                'address_prefixes': ['10.0.0.0/16']
            }
        }
    )
    async_vnet_creation.wait()

    # Create Subnet
    print('\nCreate Subnet')
    async_subnet_creation = network_client.subnets.create_or_update(
        GROUP_NAME,
        VNET_NAME,
        SUBNET_NAME,
        {'address_prefix': '10.0.0.0/24'}
    )
    subnet_info = async_subnet_creation.result()

    # Create public ip address
    print('\nCreate Public IP Address')
    async_public_ip_creation = network_client.public_ip_addresses.create_or_update(
        GROUP_NAME,
        IP_ADDRESS_NAME,
        PublicIPAddress(
            location=LOCATION,
            public_ip_allocation_method='Static'
        )

    )
    public_ip_info = async_public_ip_creation.result()

    # Create NIC
    print('\nCreate NIC')
    async_nic_creation = network_client.network_interfaces.create_or_update(
        GROUP_NAME,
        NIC_NAME,
        {
            'location': LOCATION,
            'ip_configurations': [{
                'name': IP_CONFIG_NAME,
                'subnet': {
                    'id': subnet_info.id
                },
                'public_ip_address':{
                    'id': public_ip_info.id
                }
            }]
        }
    )
    return async_nic_creation.result()


def create_vm_parameters(nic_id, vm_reference):
    """Create the VM parameters structure.
    """
    return {
        'location': LOCATION,
        'os_profile': {
            'computer_name': VM_NAME,
            'admin_username': USERNAME,
            'admin_password': PASSWORD
        },
        'hardware_profile': {
            'vm_size': 'Standard_DS1_v2'
        },
        'storage_profile': {
            'image_reference': {
                'publisher': vm_reference['publisher'],
                'offer': vm_reference['offer'],
                'sku': vm_reference['sku'],
                'version': vm_reference['version']
            },
        },
        'network_profile': {
            'network_interfaces': [{
                'id': nic_id,
            }]
        },
    }


if __name__ == "__main__":
    run_example()
```

When the program finishes, verify the virtual machine in your subscription with the Azure CLI 2.0:

```azurecli-interactive
az vm list --resource-group sampleVmResourceGroup
```

Once you've verified that the code worked, use the CLI to delete the VM and its resources.

```azurecli-interactive
az group delete --name sampleVmResourceGroup
```

## Deploy a web app from a GitHub repo
This code deploys a Flask web application from the `master` branch in a GitHub repo in to a new [Azure App Service Web App](https://docs.microsoft.com/azure/app-service-web/app-service-web-overview) running in the free tier. 

Before you begin: [Fork](https://help.github.com/articles/fork-a-repo/) https://github.com/Azure-Samples/python-docs-hello-world

```python
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.web.models import AppServicePlan, SkuDescription, Site, SiteSourceControl, SiteConfig
from azure.common.client_factory import get_client_from_cli_profile

RESOURCE_GROUP_NAME = 'sampleWebResourceGroup'
SERVICE_PLAN_NAME = 'sampleFreePlanName'
WEB_APP_NAME = 'YOUR_APP_NAME'

#log in
resource_client = get_client_from_cli_profile(ResourceManagementClient)
web_client = get_client_from_cli_profile(WebSiteManagementClient)

# create resource group
resource_group = resource_client.resource_groups.create_or_update(
    RESOURCE_GROUP_NAME,
    {
        'location':'eastus'
    }
)
print('Created resource group: ' + resource_group.name)

# create a free app service plan
service_plan_async_operation = web_client.app_service_plans.create_or_update(
    RESOURCE_GROUP_NAME,
    SERVICE_PLAN_NAME,
    AppServicePlan(
        location='eastus',
        sku=SkuDescription(
            name='F1',
            tier='Free',
        )
    )
)

service_plan = service_plan_async_operation.result()
print('created app service plan: ' + service_plan.name)
#
# create a web app
siteConfiguration = SiteConfig(
    python_version='3.4',
)
site_async_operation = web_client.web_apps.create_or_update(
    RESOURCE_GROUP_NAME,
    WEB_APP_NAME,
    Site(
        location='eastus',
        server_farm_id=service_plan.id,
        site_config=siteConfiguration
    ),
)


site = site_async_operation.result()
print('created webapp: ' + site.default_host_name)

# continuous deployment with GitHub
source_control_async_operation = web_client.web_apps.create_or_update_source_control(
    RESOURCE_GROUP_NAME,
    WEB_APP_NAME,
    SiteSourceControl(
        location='GitHub',
        repo_url='https://github.com/lisawong19/python-docs-hello-world',
        branch='master'
    )
)

source_control = source_control_async_operation.result()
print("added source control to: " + source_control.name + "azurewebsites.net")
```

Open a browser pointed to the application using the CLI:
```azcli
az appservice web browse --resource-group sampleWebResourceGroup --name YOUR_APP_NAME
```

Remove the web app and plan from your subscription once you've verified the deployment. 
```azcli
az group delete --name sampleWebResourceGroup
```


## Connect to a SQL database
This code creates a new SQL database with a firewall rule allowing remote access, and then connected to it using the Microsoft ODBC driver. Pyodbc uses the Microsoft ODBC Driver on Linux to connect to SQL Databases. 
```python
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.sql import SqlManagementClient
from azure.common.client_factory import get_client_from_cli_profile
import pyodbc

LOCATION = 'eastus'
GROUP_NAME = 'azure-sample-group'
SERVER_NAME = 'samplesqlserver123'
DATABASE_NAME = 'sample-db'
USER_NAME ='mysecretname'
PASSWORD='HusH_Sec4et'

# authenticate
resource_client = get_client_from_cli_profile(ResourceManagementClient)
sql_client = get_client_from_cli_profile(SqlManagementClient)

# You MIGHT need to add SQL as a valid provider for these credentials
# If so, this operation has to be done only once for each credentials
resource_client.providers.register('Microsoft.Sql')


def run_example():

    # You MIGHT need to add SQL as a valid provider for these credentials
    # If so, this operation has to be done only once for each credentials
    resource_client.providers.register('Microsoft.Sql')

    # Create Resource group
    print('Create Resource Group')
    resource_client.resource_groups.create_or_update(GROUP_NAME, {'location': LOCATION})

    # Create a SQL server
    print('Create a SQL server')
    server = sql_client.servers.create_or_update(
        GROUP_NAME,
        SERVER_NAME,
        {
            'location': LOCATION,
            'version': '12.0', # Required for create
            'administrator_login': USER_NAME, # Required for create
            'administrator_login_password': PASSWORD # Required for create
        }
    )
    print(server)
    print('\n\n')

    # Open access to this server for IPs
    print("Add firewall rule")
    firewall_rule = sql_client.firewall_rules.create_or_update(
        GROUP_NAME,
        SERVER_NAME,
        "firewall_rule_name_123.123.123.123",
        "123.123.123.123", # Start ip range
        "167.220.0.235"  # End ip range
    )
    print(firewall_rule)

    # Create a database
    print('Create SQL database')
    async_db_create = sql_client.databases.create_or_update(
        GROUP_NAME,
        SERVER_NAME,
        DATABASE_NAME,
        {
            'location': LOCATION
        }
    )
    database = async_db_create.result() # Wait for completion and return created object
    print(database)
    print("\n\n")

    # Get SQL database
    print('Get SQL database')
    database = sql_client.databases.get(
        GROUP_NAME,
        SERVER_NAME,
        DATABASE_NAME
    )
    print(database)
    print("\n\n")


def create_and_insert():
    server = SERVER_NAME+'.database.windows.net'
    database = DATABASE_NAME
    username = USER_NAME
    password = PASSWORD
    driver = '{ODBC Driver 13 for SQL Server}'
    cnxn = pyodbc.connect(
        'DRIVER=' + driver + ';PORT=1433;SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    tsql = "CREATE TABLE CLOUD (name varchar(255), code int);"
    tsqlInsert = "INSERT INTO CLOUD (name, code) VALUES ('Azure', 1); "
    selectValues = "SELECT * FROM CLOUD"
    with cursor.execute(tsql):
        print('Successfully created table!')
    with cursor.execute(tsqlInsert):
        print('Successfully inserted data into table')
    cursor.execute(selectValues)
    row = cursor.fetchone()
    while row:
        print(str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()
    cnxn.commit()

if __name__ == "__main__":
    run_example()
    create_and_insert()
```

## Write a blob into a new storage account

This code creates an [Azure storage account](https://docs.microsoft.com/azure/storage/storage-introduction) and then uses the Azure Storage libraries for Python to create a new html file in the cloud. 
```python
from azure.storage import CloudStorageAccount
from azure.storage.blob import PublicAccess
from azure.storage.blob.models import ContentSettings
from azure.mgmt.storage.models import (
    StorageAccountCreateParameters,
    StorageAccountUpdateParameters,
    Sku,
    SkuName,
    Kind
)
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

# log in
resource_client = get_client_from_cli_profile(ResourceManagementClient)
storage_client = get_client_from_cli_profile(StorageManagementClient)

# You MIGHT need to add Storage as a valid provider for these credentials
# If so, this operation has to be done only once for each credentials
 resource_client.providers.register('Microsoft.Storage')

# create a new resource group
resource_client.resource_groups.create_or_update(
    'sampleStorageResourceGroup',
    {
        'location':'eastus'
    }
)

# create a new storage account
async_create = storage_client.storage_accounts.create(
    'sampleStorageResourceGroup',
    'sampleStorageAccountName',
    StorageAccountCreateParameters(
        sku=Sku(SkuName.standard_ragrs),
        kind=Kind.storage,
        location='eastus'
    )
)
async_create.wait()

# create a public storage container to hold the file
storage_keys = storage_client.storage_accounts.list_keys('sampleStorageResourceGroup', 'sampleStorageAccountName')
storage_keys = {v.key_name: v.value for v in storage_keys.keys}

storage_client = CloudStorageAccount('sampleStorageAccountName', storage_keys['key1'])
blob_service = storage_client.create_block_blob_service()

blob_service.create_container('sampleContainerName',public_access=PublicAccess.Container)


blob_service.create_blob_from_bytes(
    'sampleContainerName',
    'helloworld.html',
    b'<center><h1>Hello World!</h1></center>',
    content_settings=ContentSettings('text/html')
)

print(blob_service.make_blob_url('sampleContainerName', 'helloworld.html'))
```
To verify content successfully uploaded, navigate to the url printed. 

Clean up the storage account using the CLI:
```azcli
az group delete --name sampleStorageResourceGroup
```

## Explore more samples

To learn more about how to use the Azure management libraries for Python to manage resources and automate tasks, see our sample code for [virtual machines](python-sdk-azure-web-apps-samples.md), [web apps](python-sdk-azure-web-apps-samples.md) and [SQL database](python-sdk-azure-sql-database-samples.md).


## Reference

A [reference](http://docs.microsoft.com/python/api) is available for all packages.