---
title: Azure ML Package client library for Python
keywords: Azure, python, SDK, API, azure-ai-ml, ml
ms.date: 07/08/2025
ms.topic: reference
ms.devlang: python
ms.service: ml
---
# Azure ML Package client library for Python - version 1.28.1 


We are excited to introduce the GA of Azure Machine Learning Python SDK v2. The Python SDK v2 introduces new SDK capabilities like standalone local jobs, reusable components for pipelines and managed online/batch inferencing. Python SDK v2 allows you to move from simple to complex tasks easily and incrementally. This is enabled by using a common object model which brings concept reuse and consistency of actions across various tasks. The SDK v2 shares its foundation with the CLI v2 which is also GA.

[Source code][source_code]
| [Package (PyPI)][ml_pypi]
| [Package (Conda)][ml_conda]
| [API reference documentation][ml_ref_docs]
| [Product documentation][product_documentation]
| [Samples][ml_samples]


This package has been tested with Python 3.8, 3.9, 3.10, 3.11, 3.12 and 3.13.

For a more complete set of Azure libraries, see https://aka.ms/azsdk/python/all

## Getting started

### Prerequisites

- Python 3.7 or later is required to use this package.
- You must have an [Azure subscription][azure_subscription].
- An [Azure Machine Learning Workspace][workspace].

### Install the package

Install the Azure ML client library for Python with [pip][pip_link]:

```bash
pip install azure-ai-ml
pip install azure-identity
```

### Authenticate the client

```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)
```

## Key concepts

Refer the below high level sequence diagram illustrating the package's workflow:

![azure-ai-ml sequence diagram](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-ml_1.28.1/sdk/ml/azure-ai-ml/azure_ai_ml_seq_diagram.png?raw=true)

## SDK Architecture Components

The sequence diagram above illustrates the architecture and workflow of the Azure ML Python SDK v2. Here's an explanation of the key components:

- **User**: You, the developer using the SDK to interact with Azure ML.
- **Entity**: Python classes representing Azure ML resources like Jobs, Models, Components, etc.
- **Schema**: Validation classes that ensure entities conform to expected structures and requirements.
- **MLClient**: The main entry point for all operations, providing access to various services.
- **Operations**: Specialized classes handling specific resource types (jobs, models, endpoints, etc.).
- **Telemetry**: Internal component for monitoring and collecting usage data (opt-out available).
- **Serialization**: Converts between Python objects and REST API formats.
- **REST Client**: Manages HTTP communications with Azure ML services.
- **Authentication**: Handles identity and access tokens via Azure Identity libraries.
- **AzureML Service**: The backend Azure Machine Learning service.

## Workflow Description

The diagram depicts two main workflows:

1. **Entity Creation and Validation**:
   - Create entities directly using Python classes or load from YAML files
   - YAML files are validated against schemas to ensure correctness
   - Validation errors are reported immediately if found

2. **Operation Execution**:
   - Initialize MLClient with proper credentials
   - Request operations through the client (create, get, list, delete, etc.)
   - Operations are routed to specialized classes for handling
   - Entities are serialized into REST API format
   - Authenticated HTTP requests are sent to Azure ML services
   - Responses are deserialized back into entity objects
   - Results are returned to the user

Azure Machine Learning Python SDK v2 comes with many new features like standalone local jobs, reusable components for pipelines and managed online/batch inferencing. The SDK v2 brings consistency and ease of use across all assets of the platform. The Python SDK v2 offers the following capabilities:
* Run **Standalone Jobs** - run a discrete ML activity as Job. This job can be run locally or on the cloud. We currently support the following types of jobs:
  * Command - run a command (Python, R, Windows Command, Linux Shell etc.)
  * Sweep - run a hyperparameter sweep on your Command
* Run multiple jobs using our **improved Pipelines**
  * Run a series of commands stitched into a pipeline (**New**)
  * **Components** - run pipelines using reusable components (**New**)
* Use your models for **Managed Online inferencing** (**New**)
* Use your models for Managed **batch inferencing**
* Manage AML resources – workspace, compute, datastores
* Manage AML assets - Datasets, environments, models
* **AutoML** - run standalone AutoML training for various ml-tasks:
  - Classification (Tabular data)
  - Regression (Tabular data)
  - Time Series Forecasting (Tabular data)
  - Image Classification (Multi-class) (**New**)
  - Image Classification (Multi-label) (**New**)
  - Image Object Detection (**New**)
  - Image Instance Segmentation (**New**)
  - NLP Text Classification (Multi-class) (**New**)
  - NLP Text Classification (Multi-label) (**New**)
  - NLP Text Named Entity Recognition (NER) (**New**)

## Examples

- View our [samples][ml_samples].

## Troubleshooting

### General

Azure ML clients raise exceptions defined in [Azure Core][azure_core_readme].

```python
from azure.core.exceptions import HttpResponseError

try:
    ml_client.compute.get("cpu-cluster")
except HttpResponseError as error:
    print("Request failed: {}".format(error.message))
```

### Logging

This library uses the standard
[logging][python_logging] library for logging.
Basic information about HTTP sessions (URLs, headers, etc.) is logged at INFO
level.

Detailed DEBUG level logging, including request/response bodies and unredacted
headers, can be enabled on a client with the `logging_enable` argument.

See full SDK logging documentation with examples [here][sdk_logging_docs].

### Telemetry

The Azure ML Python SDK includes a telemetry feature that collects usage and failure data about the SDK and sends it to Microsoft when you use the SDK in a Jupyter Notebook only.
<u>Telemetry will **not** be collected for any use of the Python SDK outside of a Jupyter Notebook.</u>

Telemetry data helps the SDK team understand how the SDK is used so it can be improved and the information about failures helps the team resolve problems and fix bugs.
The SDK telemetry feature is enabled by default for Jupyter Notebook usage and cannot be enabled for non-Jupyter scenarios. To opt out of the telemetry feature in a Jupyter scenario, pass in `enable_telemetry=False` when constructing your MLClient object.

## Next steps

- View our [samples][ml_samples].

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit [cla.microsoft.com][cla].

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct][code_of_conduct]. For more information see the [Code of Conduct FAQ][coc_faq] or contact [opencode@microsoft.com][coc_contact] with any additional questions or comments.

<!-- LINKS -->

[source_code]: https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-ml_1.28.1/sdk/ml/azure-ai-ml
[ml_pypi]: https://pypi.org/project/azure-ai-ml/
[ml_conda]: https://anaconda.org/microsoft/azure-ai-ml/
[ml_ref_docs]: https://learn.microsoft.com/python/api/azure-ai-ml/?view=azure-python
[ml_samples]: https://github.com/Azure/azureml-examples/tree/main/sdk/python
[product_documentation]: https://learn.microsoft.com/azure/machine-learning/
[azure_subscription]: https://azure.microsoft.com/free/
[workspace]: https://learn.microsoft.com/azure/machine-learning/concept-workspace
[python_logging]: https://docs.python.org/3/library/logging.html
[sdk_logging_docs]: https://learn.microsoft.com/azure/developer/python/azure-sdk-logging
[azure_core_readme]: https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-ml_1.28.1/sdk/core/azure-core/README.md
[pip_link]: https://pypi.org/project/pip/
[azure_core_ref_docs]: https://aka.ms/azsdk-python-core-policies
[azure_core]: https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-ml_1.28.1/sdk/core/azure-core/README.md
[azure_identity]: https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-ml_1.28.1/sdk/identity/azure-identity
[cla]: https://cla.microsoft.com
[code_of_conduct]: https://opensource.microsoft.com/codeofconduct/
[coc_faq]: https://opensource.microsoft.com/codeofconduct/faq/
[coc_contact]: mailto:opencode@microsoft.com

