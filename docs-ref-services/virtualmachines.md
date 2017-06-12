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

Define, configure, and deploy new Windows and Linux virtual machines and virtual machine scale sets from your code with the Azure management libraries for Python. The libraries also let start and stop existing virtual machines and attach or detach disks to stopped VMs in your subscription.

## Import the libraries
```bash
pip install --pre azure-mgmt-compute 
```   

## Example

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

| || 
|---|---|
| [Manage virtual machines][1] | Create, modify, start, stop, and delete virtual machines. |
| [Manage a load balancer][2] | Manage a load balancer using the Azure Resource Manager APIs for python. |
| [Create and configure managed disks][3] | Create, resizing, updating a managed disk.|
| [List images][4] | Print all of the available images to use for creating virtual machines.| 
| [Monitor virtual machines][5] |Get metrics of a virtual machine's usage | 

[1]: https://azure.microsoft.com/resources/samples/virtual-machines-python-manage/
[2]: https://azure.microsoft.com/resources/samples/network-python-manage-loadbalancer
[3]: python-sdk-azure-samples-managed-disks.md
[4]: python-sdk-azure-samples-list-images.md
[5]: python-sdk-azure-samples-monitor-vms.md


Explore more [sample Python code](https://azure.microsoft.com/resources/samples/?platform=python) you can use in your apps.