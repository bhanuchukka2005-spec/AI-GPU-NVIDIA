# Day 9 - Computer Vision with Roboflow

## Overview

The ninth day of the internship focused on Computer Vision and model training using the Roboflow platform. The session introduced dataset management, model training, and image prediction workflows using Roboflow's cloud-based machine learning tools.

## Learning Objectives

* Understand the fundamentals of Computer Vision.
* Learn how to manage datasets using Roboflow.
* Train image classification models on custom datasets.
* Perform image prediction using trained models.
* Integrate Roboflow models with Python applications.

---

## Topics Covered

### 1. Introduction to Roboflow

The session began with an introduction to Roboflow and its role in simplifying computer vision workflows.

Features explored:

* Dataset management
* Image annotation
* Dataset preprocessing
* Model training
* Model deployment
* Inference APIs

---

### 2. Dataset Preparation

A Cats vs Dogs dataset was used for training.

Activities performed:

* Uploaded images to Roboflow.
* Organized images into classes.
* Prepared the dataset for training.
* Generated dataset versions for model training.

---

### 3. Model Training

A computer vision model was trained using the prepared dataset.

Training workflow:

1. Dataset upload
2. Dataset preprocessing
3. Model training
4. Model evaluation
5. Deployment

The model learned to distinguish between cat and dog images based on the provided training data.

---

### 4. Image Prediction

After training, a sample image was provided to the model for inference.

The model:

* Processed the input image.
* Predicted the class label.
* Returned confidence scores for the prediction.

---

### 5. Python Integration with Roboflow

The trained model was accessed using the Roboflow Python SDK.

#### Libraries Used

```python
from inference_sdk import InferenceHTTPClient
from roboflow import Roboflow
```

#### Workflow

* Connected to Roboflow using an API key.
* Accessed the workspace.
* Opened the project.
* Loaded the trained model version.
* Performed prediction on a sample image.
* Retrieved prediction results in JSON format.

Example workflow:

```python
rf = Roboflow(api_key="YOUR_API_KEY")

workspace = rf.workspace("workspace_name")

project = workspace.project("project_name")

model = project.version(1).model

result = model.predict("sample_image.jpg").json()

print(result)
```

---

## Key Learnings

* Fundamentals of Computer Vision workflows.
* Dataset preparation and management.
* Training image classification models.
* Using Roboflow for rapid model development.
* Running inference on trained models.
* Accessing deployed models through Python SDKs.
* Understanding prediction outputs and confidence scores.

---

## Outcome

Successfully trained an image classification model using a Cats vs Dogs dataset on Roboflow and performed image prediction using a sample image. Gained hands-on experience with cloud-based computer vision workflows and model deployment through the Roboflow platform.
