---
title: Azure Cognitive Services SDK for Python
description: Reference for Azure Cognitive Services SDK for Python
ms.date: 07/24/2024
ms.topic: reference
ms.devlang: python
ms.service: cognitiveservices
---
# Azure Cognitive Services modules for Python

Add image and face recognition, language analysis, and search to your Python apps, websites, and tools using the Azure Cognitive Services modules for Python.

## Vision modules

### Computer Vision 

Returns information about visual content found in an image:

- Use tagging, descriptions, and domain-specific models to identify content and label it with confidence.
- Apply adult/racy settings to enable automated restriction of adult content.
- Identify image types and color schemes in pictures.

[Try Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) for free in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-vision-computervision
```

[Learn more](/azure/cognitive-services/computer-vision/home) about the Computer Vision API and get started with the [Computer Vision API Python quickstart](/azure/cognitive-services/computer-vision/quickstarts/python).

### Content Moderator

Machine-assisted moderation of text, video and images, augmented with human review tools.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-vision-contentmoderator
```

[Learn more](/azure/cognitive-services/content-moderator/overview) about the Content Moderator service.

### Custom Vision Service

Upload images to train and customize a computer vision model for your specific use case. Once the model is trained, you can use the API to tag images using the model and evaluate the results to improve your classifier.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-vision-customvision
```

[Learn more](/azure/cognitive-services/Custom-Vision-Service/home) about the Custom Vision service and get started with the [Custom Vision Python tutorial](/azure/cognitive-services/Custom-Vision-Service/python-tutorial)

### Face API

Detect, identify, analyze, organize, and tag faces in photos. 

[Try the Face API](https://azure.microsoft.com/en-us/services/cognitive-services/face/) in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install cognitive-face
```

[Learn more](/azure/cognitive-services/face/overview) about the Face API and get started with the [Face API Python quickstart](/azure/cognitive-services/Face/Tutorials/FaceAPIinPythonTutorial).

## Search modules

### Web search

Retrieve web documents indexed by the Bing Web Search API and narrow down the results by result type, freshness and more. 

[Try the Web Search API](https://azure.microsoft.com/en-us/services/cognitive-services/bing-web-search-api/) in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-search-websearch
```

[Learn more](/azure/cognitive-services/bing-web-search/overview) about the Bing Web Search API and get started with the [Web Search API Python quickstart](/azure/cognitive-services/bing-web-search/quickstarts/python).

### Image search

Search for images and get thumbnails, full image URLs, image metadata and more in your results.

[Try the Image Search API](https://azure.microsoft.com/en-us/services/cognitive-services/bing-image-search-api/) in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-search-imagesearch
```

[Learn more](/azure/cognitive-services/bing-image-search/overview) about the Bing Image Search API and get started with the [Image Search API Python quickstart](/azure/cognitive-services/bing-image-search/quickstarts/python).


### Entity search

Search for the most relevant entity (place, person, or thing) for a given search term or location.

[Try the Entity Search API](https://azure.microsoft.com/services/cognitive-services/bing-entity-search-api/) in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-search-entitysearch
```

[Learn more](/azure/cognitive-services/bing-entities-search/search-the-web) about the Bing Entity Search API and get started with the [Entity Search API Python quickstart](/azure/cognitive-services/bing-entities-search/quickstarts/python).

### Custom search

Build and a custom web search that meets your specific search domain.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-search-customsearch
```

[Learn more](/azure/cognitive-services/bing-custom-search/) about the Bing Custom Search service and get started with querying your custom search from Python with the [Custom Search API Python quickstart](/azure/cognitive-services/bing-custom-search/call-endpoint-python).

### Video search

Find videos across the web and get results with creator, encoding, length, and view count metadata.

[Try the Video Search API](https://azure.microsoft.com/services/cognitive-services/bing-video-search-api/) in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-search-videosearch
```

[Learn more](/azure/cognitive-services/bing-video-search/search-the-web) about the Bing Video Search service and get started with the [Video Search API Python quickstart](/azure/cognitive-services/bing-video-search/python).


### News search

Search the web for news articles and work with article, related news, images, and provider info metadata.

[Try the News Search API](https://azure.microsoft.com/services/cognitive-services/bing-news-search-api/) in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-search-newssearch
```

[Learn more](/azure/cognitive-services/bing-news-search/search-the-web) about the Bing News Search service and get started with the [News Search API Python quickstart](/azure/cognitive-services/bing-news-search/python).


## Language modules

### Text Analytics 

The Text Analytics API is a cloud-based service that provides  natural language processing over raw text. The API includes three main functions:

- Sentiment analysis
- Key phrase extraction
- Language detection

[Try the Text Analytics API](https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/) in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-language-textanalytics
```

[Learn more](/azure/cognitive-services/text-analytics/overview) about the Text Analytics API and get started with the [Text Analytics API Python quickstart](/azure/cognitive-services/text-analytics/quickstarts/python).

### Language Understanding

The LUIS API provides you with natural language understanding capabilties like intent recognition and relevant entity extraction from user utterances.

[Try LUIS API](https://westus.dev.cognitive.microsoft.com/docs/services/5890b47c39e2bb17b84a55ff/operations/5890b47c39e2bb052c5b9c2f) in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-language-luis
```

[Learn more](/azure/cognitive-services/luis/what-is-luis) about the LUIS and get started with the [LUIS SDK quickstart](/azure/cognitive-services/luis/client-libraries-rest-api).


### Spell Check

Perform contextual grammar and spell checking with the Bing Spell Check API.

[Try the Spell Check API](https://azure.microsoft.com/en-us/services/cognitive-services/spell-check/) in your browser.

Get the Python module with [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
pip install azure-cognitiveservices-language-spellcheck
```

[Learn more](/azure/cognitive-services/bing-spell-check/proof-text) about the Spell Check API and get started with the [Spell Check API Python quickstart](/azure/cognitive-services/bing-spell-check/quickstarts/python).