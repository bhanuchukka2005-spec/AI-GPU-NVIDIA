# NVIDIA Internship 2026

This repository contains the daily learning activities, hands-on exercises, assignments, and projects completed during the NVIDIA Internship 2026.

The internship focuses on Kubernetes, cloud-native environments, Machine Learning, Deep Learning, and Image Classification using modern AI frameworks and real-world datasets.

## Internship Progress

### Day 1 - Kubernetes Setup and Image Prediction

* Learned Docker and Kubernetes fundamentals.
* Deployed Pods and Services using Kubernetes.
* Connected to the university head node using SSH.
* Launched Jupyter Lab inside a Kubernetes environment.
* Executed an image prediction application using a pre-trained deep learning model.

### Day 2 - Regression and Classification

* Learned Regression and Classification concepts with real-world examples.
* Implemented House Price Prediction using Linear Regression.
* Implemented Titanic Survival Prediction using Logistic Regression.
* Predicted student marks and classified students as Pass/Fail.
* Worked with the IBM Telco Customer Churn Dataset.
* Added visualizations using Matplotlib to improve result interpretation.

### Day 3 - Neural Networks and Deep Learning

* Learned Neural Network fundamentals.
* Understood Input, Hidden, and Output Layers.
* Explored activation functions and their role in learning.
* Implemented a Single Neuron (Perceptron) model.
* Solved the XOR problem using a Neural Network.
* Visualized Neural Network architecture.
* Built and trained a Deep Neural Network using TensorFlow and the Fashion-MNIST dataset.
* Received an image classification assignment using the Intel Image Classification Dataset.

### Day 4 - CNNs and Model Performance Evaluation

* Learned the fundamentals and architecture of Convolutional Neural Networks (CNNs).
* Explored different image classification architectures including CNN, MobileNetV2, ResNet50, and EfficientNetB0.
* Implemented an image classification model using Hugging Face and MobileNetV2.
* Trained and compared multiple models using the Intel Image Classification Dataset.
* Evaluated model performance using accuracy metrics.

#### Intel Image Classification Dataset Results

| Model          | Accuracy |
| -------------- | -------- |
| MobileNetV2    | 77.45%   |
| CNN            | 58.55%   |
| ResNet50       | 22.15%   |
| EfficientNetB0 | 10.80%   |

#### Flowers Dataset Results

| Model          | Accuracy |
| -------------- | -------- |
| MobileNetV2    | 90.19%   |
| CNN            | 66.76%   |
| ResNet50       | 35.69%   |
| EfficientNetB0 | 21.66%   |

* MobileNetV2 achieved the best performance on both datasets.

### Day 5 - Full Stack Development and AI-Assisted Web Development

* Learned the fundamentals of Full Stack Development and the complete software development lifecycle.
* Discussed the stages involved in building an application, including:

  * Requirement Gathering
  * Design and Development
  * Testing
  * Deployment
  * Maintenance
* Received an introduction to CI/CD (Continuous Integration and Continuous Deployment) concepts and their role in modern software development.
* Learned the basics of Prompt Engineering and how prompts can be used to effectively interact with AI-powered development tools.
* Explored the AI-assisted development tool **Antigravity IDE**.
* Built a simple portfolio website using natural language prompts in Antigravity IDE.
* Learned how AI can accelerate frontend development by generating code from user requirements.
* Installed and configured Node.js for running web applications locally.
* Executed and viewed the generated portfolio website using Node.js.
* Gained practical exposure to AI-assisted web development workflows and modern development tools.

### Day 6 - Transformers and Generative AI

- Learned the fundamentals of Transformer architecture.
- Explored Word Embeddings and Tokenization techniques.
- Understood how modern NLP models process text.
- Used Groq APIs for Text-to-Speech and Text-to-Image generation.
- Performed benchmarking on BERT and GPT models.
- Compared the performance of Groq and Gemini models across different tasks.
- Gained practical experience with Generative AI workflows and model evaluation.

### Day 7 - Hugging Face Transformers and LoRA Fine-Tuning

* Explored the Hugging Face Transformers ecosystem and worked with pretrained NLP models such as BERT and DistilGPT2.
* Learned tokenization, attention masks, embeddings, and text representation techniques.
* Implemented multiple NLP pipelines including text generation, sentiment analysis, translation, summarization, and feature extraction.
* Studied Parameter Efficient Fine-Tuning (PEFT) and Low-Rank Adaptation (LoRA) as efficient alternatives to full model fine-tuning.
* Built a complete LoRA fine-tuning workflow including dataset preparation, tokenization, training, adapter saving, and inference.
* Conducted benchmarking experiments across multiple LoRA configurations and analyzed training time, GPU memory usage, training loss, and model performance.
* Resolved practical GPU and environment issues related to PyTorch, CUDA, PEFT, and dependency compatibility.
* Gained hands-on experience with modern LLM adaptation techniques using Hugging Face, PEFT, and GPU-based training environments.

### Day 8 - Generative AI, GANs and Diffusion Models

* Learned the fundamentals of Generative AI and how it differs from traditional AI and machine learning approaches.
* Explored Generative Adversarial Networks (GANs), including the roles of the Generator and Discriminator and how they compete during training.
* Studied Diffusion Models and understood how images are generated by progressively removing noise from random inputs.
* Learned the architecture and workflow of Stable Diffusion for text-to-image generation.
* Explored how Stable Diffusion can be executed on NVIDIA H200 GPUs for accelerated image generation tasks.
* Understood the implementation workflow for training GANs and running Stable Diffusion models using Python.
* Compared GANs and Diffusion Models, including their strengths, limitations, and suitable use cases.
* Gained practical knowledge of modern image generation techniques used in Generative AI applications.

### Day 9 - Computer Vision with Roboflow

- Learned the fundamentals of Computer Vision workflows using Roboflow.
- Prepared and managed a Cats vs Dogs image dataset.
- Trained an image classification model on the Roboflow platform.
- Evaluated model performance using sample images.
- Performed image prediction and analyzed confidence scores.
- Integrated Roboflow models with Python using the Roboflow SDK.
- Retrieved prediction results through API-based inference workflows.
