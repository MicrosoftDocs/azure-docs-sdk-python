---
title: Azure Virtual Machine libraries for Python
description: 
keywords: Azure, Python, SDK, API, Compute , Virtual Machines
author: lisawong19
ms.author: liwong
manager: douge
ms.date: 06/09/2017
ms.topic: article
ms.prod: azure
ms.technology: azure
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

[!div class="nextstepaction"]
[Explore the Management APIs](/python/api/azure.mgmt.compute.compute)

### Example

Create a new Linux virtual machine in an existing Azure resource group.

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

## Samples

* [Manage virtual machines][1]
* [Manage a load balancer][2]
* [Create and configure managed disks][3]
* [List images][4] 
* [Monitor virtual machines][5]

View the [complete list](https://azure.microsoft.com/resources/samples/?platform=python&term=virtual-machines) of virtual machine samples.

[1]: https://azure.microsoft.com/resources/samples/virtual-machines-python-manage/
[2]: https://azure.microsoft.com/resources/samples/network-python-manage-loadbalancer
[3]: ../docs-ref-conceptual/python-sdk-azure-samples-managed-disks.md
[4]: ../docs-ref-conceptual/python-sdk-azure-samples-list-images.md
[5]: ../docs-ref-conceptual/python-sdk-azure-samples-monitor-vms.md