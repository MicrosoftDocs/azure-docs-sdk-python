---
title: Face API 
author: PatrickFarley
ms.author: pafarley
ms.date: 06/21/2021
ms.topic: article
ms.prod: azure
ms.technology: azure
ms.devlang: python
ms.service: face-api
---

# Azure Face API

> [!IMPORTANT]
> Face service access is limited based on eligibility and usage criteria in order to support our Responsible AI principles. Face service is only available to Microsoft managed customers and partners. Use the [Face Recognition intake form](https://aka.ms/facerecognition) to apply for access.

> [!IMPORTANT]
> The following Face attributes have been categorized as **sensitive attributes**: `age`, `gender`, `emotion`, `smile`, `hair`, `facial hair`, `makeup`. New Face customers won't be able to use these attributes unless they get approved for a corresponding scenario through the [Face Recognition Limited Access Review](https://aka.ms/facerecognition) form. Existing customers will have access to **sensitive attributes** until June 21 2023, after which they must also request access.

The Azure Face service provides AI algorithms that detect, recognize, and analyze human faces in images.

## Install the library

After installing Python, you can install the client library with:

```console
pip install --upgrade azure-cognitiveservices-vision-face
```

## Next Steps

Go to the Face service [Overview](https://docs.microsoft.com/azure/cognitive-services/face/overview) or follow a [quickstart](https://docs.microsoft.com/azure/cognitive-services/face/quickstarts/client-libraries) to get started.
