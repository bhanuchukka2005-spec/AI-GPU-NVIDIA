# Summer Internship 2026

## About
This repository contains the work, learning outcomes, and hands-on activities completed during my Summer Internship. The internship focuses on Kubernetes, cloud-native environments, Jupyter-based AI workloads, and machine learning applications.

---

# Day 1 – Kubernetes Setup and Image Prediction

## Objective
Understand the basics of Docker and Kubernetes and deploy a Jupyter Notebook environment on a Kubernetes cluster.

## What I Learned
- Difference between Docker and Kubernetes.
- How Kubernetes manages containerized applications.
- Basic Kubernetes resources such as Pods and Services.
- Accessing remote computing infrastructure using SSH.
- Running Jupyter Notebook inside a Kubernetes Pod.

## Hands-on Activities

### Step 1: Accessing the Cluster
- Connected to the university head node using SSH credentials provided by the internship mentors.
- Explored the Kubernetes environment and available resources.

### Step 2: Pod Deployment
- Created a Kubernetes configuration file named `pod.yaml`.
- Deployed the pod using:

```bash
kubectl apply -f pod.yaml
```

- Verified successful deployment.

### Step 3: Service Deployment
- Created a new configuration file named `pod-services.yaml`.
- Removed the previous deployment.
- Applied the new configuration to expose the service.

```bash
kubectl apply -f pod-services.yaml
```

### Step 4: Verification
- Checked deployed resources using:

```bash
kubectl get pods
kubectl get services
```

- Obtained the required port information.

### Step 5: Accessing the Running Container
- Opened an interactive terminal inside the container.

```bash
kubectl exec -it <pod-name> -- bash
```

### Step 6: Launching Jupyter Lab
- Started a Jupyter Lab server inside the pod.

```bash
jupyter lab --NotebookApp.token='password'
```

- Accessed the Jupyter interface through the URL provided by the mentors.

### Step 7: Image Prediction Exercise
- Executed an image prediction notebook.
- Provided multiple images as input.
- The pre-trained model successfully classified the images and produced accurate predictions.

## Technologies Used
- Docker
- Kubernetes
- kubectl
- SSH
- Jupyter Lab
- Python
- PyTorch

## Day 1 Outcome
Successfully deployed and managed Kubernetes resources, launched a Jupyter environment inside a container, and executed an image classification application using a pre-trained deep learning model.

---

### Daily Progress
- [x] Kubernetes introduction
- [x] Pod deployment
- [x] Service deployment
- [x] Jupyter Lab setup
- [x] Image prediction execution