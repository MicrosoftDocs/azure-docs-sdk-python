---
title: Azure Container Instances libraries for Python
description: Reference for Azure Container Instances libraries for Python
keywords: Azure, python, SDK, API, ACI, container, instances
author: mmacy
manager: jeconnoc

ms.date: 06/01/2018
ms.author: marsma
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: container-instances
---

# Azure Container Instances libraries for Python

Use the Microsoft Azure Container Instances libraries for Python to create and manage Azure container instances. Learn more by reading the [Azure Container Instances overview](/azure/container-instances/container-instances-overview).

## Management APIs

Use the management library to create and manage Azure container instances in Azure.

Install the management package via pip:

```bash
pip install azure-mgmt-containerinstance
```

## Example source

If you'd like to see the following code examples in context, you can find them in the following GitHub repository:

[Azure-Samples/aci-docs-sample-python](https://github.com/Azure-Samples/aci-docs-sample-python)

## Authentication

The example project uses file-based authentication to authenticate the Azure Container Instances and Resource Manager clients with Azure. File-based authentication queries the `AZURE_AUTH_LOCATION` environment variable for the path to a credentials file.

Create a credentials file with the [Azure CLI](/cli/azure) (or [Cloud Shell](https://shell.azure.com/)):

`az ad sp create-for-rbac --sdk-auth > my.azureauth`

Set the `AZURE_AUTH_LOCATION` environment variable to the full path of the generated credentials file. For example (in Bash):

```bash
export AZURE_AUTH_LOCATION=/home/yourusername/my.azureauth
```

With the credentials file created and the environment variable set, the [ResourceManagementClient][ResourceManagementClient] and [ContainerInstanceManagementClient][ContainerInstanceManagementClient] can be created.

<!-- SOURCE REPO: https://github.com/Azure-Samples/aci-docs-sample-python -->
[!code-python[authenticate](~/aci-docs-sample-python/src/aci_docs_sample.py#L44-L55 "Authenticate ACI and Resource Manager clients")]

For more details about authentication with the Python management libraries for Azure, see [Authenticate with the Azure Management Libraries for Python](/python/azure/python-sdk-azure-authenticate).

## Create container group - single container

This example creates a container group with a single container.

<!-- SOURCE REPO: https://github.com/Azure-Samples/aci-docs-sample-python -->
[!code-python[create_container_group](~/aci-docs-sample-python/src/aci_docs_sample.py#L77-L111 "Create single-container group")]

## Create container group - multiple containers

This example creates a container group with two containers: an application container and a sidecar container.

<!-- SOURCE REPO: https://github.com/Azure-Samples/aci-docs-sample-python -->
[!code-python[create_container_group_multi](~/aci-docs-sample-python/src/aci_docs_sample.py#L113-L153 "Create multi-container group")]

## Create task-based container group

This example creates a container group with a single task-based container. This example demonstrates several features:

* [Command line override](/azure/container-instances/container-instances-restart-policy#command-line-override) - A custom command line, different from that which is specified in the container's Dockerfile `CMD` line, is specified. Command line override allows you to specify a custom command line to execute at container startup, overriding the default command line baked-in to the container. Regarding executing multiple commands at container startup, the following applies:

   If you want to run a **single command** with several command-line arguments, for example `echo FOO BAR`, you must supply them as a string list to the `command` property of the [Container][Container]. For example:

   `command = ['echo', 'FOO', 'BAR']`

   If, however, you want to run **multiple commands** with (potentially) multiple arguments, you must execute a shell and pass the chained commands as an argument. For example, this executes both an `echo` and a `tail` command:

   `command = ['/bin/sh', '-c', 'echo FOO BAR && tail -f /dev/null']`
* [Environment variables](/azure/container-instances/container-instances-environment-variables) - Two environment variables are specified for the container in the container group. Use environment variables to modify script or application behavior at runtime, or otherwise pass dynamic information to an application running in the container
* [Restart policy](/azure/container-instances/container-instances-restart-policy) - The container is configured with a restart policy of "Never," useful for task-based containers that are executed as part of a batch job.
* Operation polling with [AzureOperationPoller][AzureOperationPoller] - After the create method is invoked, the operation is polled to determine when it has completed.

<!-- SOURCE REPO: https://github.com/Azure-Samples/aci-docs-sample-python -->
[!code-python[create_container_group_task](~/aci-docs-sample-python/src/aci_docs_sample.py#L155-L215 "Run a task-based container")]

## List container groups

This example lists the container groups in a resource group and then prints a few of their properties.

When you list container groups,the [instance_view][instance_view] of each returned group is `None`. To get the details of the containers within a container group, you must then [get][containergroupoperations_get] the container group, which returns the group with its `instance_view` property populated. See the next section, [Get an existing container group](#get-an-existing-container-group), for an example of iterating over a container group's containers with its `instance_view`.

<!-- SOURCE REPO: https://github.com/Azure-Samples/aci-docs-sample-python -->
[!code-python[list_container_groups](~/aci-docs-sample-python/src/aci_docs_sample.py#L217-L229 "List container groups")]

## Get an existing container group

This example gets a specific container group residing in a resource group, and then prints a few of its properties (including its containers) and their values.

The [get operation][containergroupoperations_get] returns a container group with its [instance_view][instance_view] populated, which allows you to iterate over each container in the group. Only the `get` operation populates the `instance_vew` property of the container group--listing the container groups in a subscription or resource group doesn't populate the instance view due to the potentially expensive nature of the operation (for example, when listing hundreds of container groups, each potentially containing multiple containers). As mentioned in previously in the [List container groups](#list-container-groups) section, after a `list`, you must subsequently `get` a specific container group to obtain its container instance details.

<!-- SOURCE REPO: https://github.com/Azure-Samples/aci-docs-sample-python -->
[!code-python[get_container_group](~/aci-docs-sample-python/src/aci_docs_sample.py#L231-L253 "Get container group")]

## Delete a container group

This example deletes several container groups from a resource group, as well as the resource group.

<!-- SOURCE REPO: https://github.com/Azure-Samples/aci-docs-sample-python -->
[!code-python[delete_container_group](~/aci-docs-sample-python/src/aci_docs_sample.py#L70-L75 "Delete container groups and resource group")]

## Next steps

* The source code for the preceding examples can be found on GitHub:

  [Azure-Samples/aci-docs-sample-python][aci-docs-sample-python]

* More Azure Container Instances code samples:

  [Azure Code Samples][samples-aci]

* Explore more [sample Python code][samples-python] you can use in your apps.

> [!div class="nextstepaction"]
> [Explore the management APIs](/python/api/overview/azure/containerinstance/management)

<!-- LINKS - External -->
[aci-docs-sample-python]: https://github.com/Azure-Samples/aci-docs-sample-python
[samples-aci]: https://azure.microsoft.com/resources/samples/?sort=0&term=ACI
[samples-python]: https://azure.microsoft.com/resources/samples/?platform=python

<!-- TYPES -->
[AzureOperationPoller]: /python/api/msrestazure.azure_operation.AzureOperationPoller?
[Container]: /python/api/azure.mgmt.containerinstance.models.container
[ContainerGroupInstanceView]: /python/api/azure.mgmt.containerinstance.models.containergrouppropertiesinstanceview
[containergroupoperations_get]: /python/api/azure.mgmt.containerinstance.operations.containergroupsoperations#get
[ContainerInstanceManagementClient]: /python/api/azure.mgmt.containerinstance.containerinstancemanagementclient
[instance_view]: /python/api/azure.mgmt.containerinstance.models.containergroup#variables
[ResourceManagementClient]: /python/api/azure.mgmt.resource.resources.resourcemanagementclient