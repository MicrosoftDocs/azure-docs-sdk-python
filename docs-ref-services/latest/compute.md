---
title: Azure Compute SDK for Python
description: Reference for Azure Compute SDK for Python
ms.date: 07/08/2025
ms.topic: reference
ms.devlang: python
ms.service: compute
---
# Azure virtual machine libraries

## Overview

On-demand, scalable computing resources running Linux or Windows.

To get started with Azure Virtual Machines, see [Create a Linux virtual machine with the Azure portal](/azure/virtual-machines/linux/quick-create-portal).

## Management API

Create, configure, manage and scale Windows and Linux virtual machines in Azure from your code with the management API.

Install the library via pip.

```bash
pip install azure-mgmt-compute
```

### Example

Create a new Linux virtual machine in an existing Azure resource group with Managed Service Identity(MSI) authentication.

```python
VM_PARAMETERS={
        'location': 'LOCATION',
        'os_profile': {
            'computer_name': 'VM_NAME',
            'admin_username': 'USERNAME',
            'admin_password': 'PASSWORD'
        },
        'hardware_profile': {
            'vm_size': 'Standard_DS1_v2'
        },
        'storage_profile': {
            'image_reference': {
                'publisher': 'Canonical',
                'offer': 'UbuntuServer',
                'sku': '16.04.0-LTS',
                'version': 'latest'
            },
        },
        'network_profile': {
            'network_interfaces': [{
                'id': 'NIC_ID',
            }]
        },
    }

def create_vm()
    compute_client.virtual_machines.create_or_update(
        'RESOURCE_GROUP_NAME', 'VM_NAME', VM_PARAMETERS)
```

> [!div class="nextstepaction"]
> [Explore the Management APIs](/python/api/azure-mgmt-compute)

## Samples

* [Manage virtual machines][1]
* [Create a virtual machine with Managed Service Identity Extension][2]
* [Manage a load balancer][3]
* [Create and configure managed disks][4]
* [Monitor virtual machines][5]

View the [complete list](https://azure.microsoft.com/resources/samples/?platform=python&term=virtual-machines) of virtual machine samples.

[1]: https://github.com/Azure-Samples/virtual-machines-python-manage
[2]: https://github.com/Azure-Samples/compute-python-msi-vm
[3]: https://github.com/Azure-Samples/network-python-manage-loadbalancer
[4]: /azure/python/python-sdk-azure-samples-managed-disks
[5]: /azure/python/python-sdk-azure-samples-monitor-vms