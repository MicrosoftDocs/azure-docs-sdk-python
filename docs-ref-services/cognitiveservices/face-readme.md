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
> Access to Face recognition features is limited and requires approval for responsible use in line with Microsoft's principles for face recognition. Use the [Face Recognition Limited Access Review](https://aka.ms/facerecognition) form to get access.

> [!IMPORTANT]
> The following Face attributes have been categorized as **sensitive attributes**: `age`, `gender`, `emotion`, `smile`, `hair`, `facial hair`, `makeup`. New Face customers won't be able to use these attributes unless they get approved for a corresponding scenario through the [Face Recognition Limited Access Review](https://aka.ms/facerecognition) form. Existing customers will have access to **sensitive attributes** until November 2022, after which they must also request access.

The Azure Face service provides AI algorithms that detect, recognize, and analyze human faces in images.

## Install the library

After installing Python, you can install the client library with:

```console
pip install --upgrade azure-cognitiveservices-vision-face
```

## Next Steps

Go to the Face service [Overview](https://docs.microsoft.com/azure/cognitive-services/face/overview) or follow a [quickstart](https://docs.microsoft.com/azure/cognitive-services/face/quickstarts/client-libraries) to get started.
