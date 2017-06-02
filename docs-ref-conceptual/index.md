Azure libraries for Python
==========================

The Azure libraries for Python let you use Azure services and manage Azure resources from your application code. The libraries are available in [PyPI](python-sdk-azure-install.md) for use in your python projects.

Manage Azure resources
----------------------

Create and manage Azure resources from Python applications using the Azure SDK for Python.

For example, create a resource group on Azure:

```python
    from azure.mgmt.resource import ResourceManagementClient

    resource_client = ResourceManagementClient(credentials, subscription_id)
    resource_client.resource_groups.create_or_update(
        'my_resource_group',
        {
            'location':'westus'
        }
    )
```

Read the [get started article](python-sdk-azure-get-started) to set up your authentication and run sample code against your own Azure subscription.

Connect to Azure services
-------------------------

In addition to using Python libraries to create and manage resources within Azure, you can also use Python libraries to connect and use those resources in your apps. For example, you might update a table SQL Database or store files in Azure Storage. Select the library you need for a particular service from the complete list of libraries and visit the Python developer center for tutorials and sample code for help using them in your apps.

For example, to upload a simple HTML page on a blob and get the Url:

```python
storage_client = CloudStorageAccount(storage_account_name, storage_key)
blob_service = storage_client.create_block_blob_service()

blob_service.create_container(
    'mycontainername',
    public_access=PublicAccess.Blob
)

blob_service.create_blob_from_bytes(
    'mycontainername',
    'myblobname',
    b'<center><h1>Hello World!</h1></center>',
    content_settings=ContentSettings('text/html')
)

print(blob_service.make_blob_url('mycontainername', 'myblobname'))
```

Get help and give feedback
--------------------------

Post questions to the community on [Stack Overflow](http://stackoverflow.com/questions/tagged/azure-sdk-python) and open issues against the SDK on the [project GitHub](https://github.com/Azure/azure-sdk-for-python).