# Day 1 - Kubernetes Setup and Image Prediction

## Overview

The first day of the internship focused on understanding containerization and container orchestration concepts using Docker and Kubernetes. The session included both theoretical discussions and hands-on activities involving Kubernetes deployments, remote cluster access, and running machine learning workloads through Jupyter Lab.

## Learning Objectives

* Understand the fundamentals of Docker and Kubernetes.
* Learn the differences between containerization and container orchestration.
* Deploy applications using Kubernetes Pods and Services.
* Access and manage resources in a Kubernetes cluster.
* Run Jupyter Lab inside a Kubernetes environment.
* Execute a machine learning application for image prediction.

## Activities Performed

### 1. Introduction to Docker and Kubernetes

The session began with an introduction to Docker and Kubernetes. The concepts of containers, container images, and orchestration were discussed along with the key differences between Docker and Kubernetes.

### 2. Accessing the Kubernetes Cluster

SSH credentials were provided to connect to the university head node. After successfully logging in, the Kubernetes environment was explored to understand how workloads are deployed and managed.

### 3. Pod Deployment

A Kubernetes configuration file named `pod.yaml` was created and deployed using:

```bash
kubectl apply -f pod.yaml
```

The deployment was verified to ensure that the pod was running successfully.

### 4. Service Configuration

A new configuration file named `pod-services.yaml` was created to expose the application through a Kubernetes Service. The previous deployment was removed and the new configuration was applied.

```bash
kubectl apply -f pod-services.yaml
```

### 5. Resource Verification

The deployed resources were verified using:

```bash
kubectl get pods
kubectl get services
```

These commands were used to check the status of the deployments and obtain the required service port information.

### 6. Accessing the Running Container

An interactive shell session was started inside the running container using:

```bash
kubectl exec -it <pod-name> -- bash
```

This allowed direct interaction with the container environment.

### 7. Launching Jupyter Lab

Inside the container, a Jupyter Lab server was started using:

```bash
jupyter lab --NotebookApp.token='password'
```

The generated URL was opened in a web browser to access the Jupyter Lab interface.

### 8. Image Prediction Demonstration

A machine learning notebook for image prediction was executed in Jupyter Lab. Multiple images were provided as input to a pre-trained deep learning model. The model successfully identified and classified the images, producing accurate predictions.

## Key Learnings

* Basics of Docker and Kubernetes.
* Creating and deploying Kubernetes Pods.
* Exposing applications using Kubernetes Services.
* Managing Kubernetes resources using `kubectl`.
* Accessing containers through interactive shell sessions.
* Running Jupyter Lab in a Kubernetes environment.
* Executing machine learning workloads on a remote cluster.
* Understanding image classification using pre-trained models.

## Outcome

Successfully connected to a Kubernetes cluster, deployed and managed resources, launched Jupyter Lab inside a containerized environment, and executed an image prediction application using a pre-trained machine learning model.
