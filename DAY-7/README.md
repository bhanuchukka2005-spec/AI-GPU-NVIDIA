# Day 7 - Hugging Face Transformers, LoRA & PEFT Fine-Tuning

## Overview

Today focused on understanding and implementing Transformer-based NLP workflows using the Hugging Face ecosystem. The session covered tokenization, embeddings, text generation, sentiment analysis, model fine-tuning using LoRA (Low-Rank Adaptation), PEFT (Parameter Efficient Fine-Tuning), and benchmarking different LoRA configurations on GPU.

---

## Topics Covered

### 1. Hugging Face Transformers

* Introduction to the Transformers library
* Loading pretrained models and tokenizers
* Understanding model architectures
* Working with DistilGPT2 and BERT models

### 2. Tokenization

* Text preprocessing using tokenizers
* Converting text into model-understandable tokens
* Token IDs and attention masks
* Comparing GPT and BERT tokenization

### 3. Embeddings

* Generating contextual embeddings using BERT
* Understanding hidden states
* Sentence embedding extraction
* Embedding dimensions and representation learning

### 4. NLP Pipelines

Implemented multiple Hugging Face pipelines:

* Text Generation
* Sentiment Analysis
* Translation
* Summarization
* Feature Extraction

---

## LoRA (Low-Rank Adaptation)

### Concepts Learned

* Why full fine-tuning is expensive
* Parameter-efficient fine-tuning
* Low-rank matrix decomposition
* Trainable adapters

### LoRA Configuration Parameters

* Rank (r)
* Alpha
* Dropout
* Target modules

### Benefits

* Reduced GPU memory consumption
* Faster training
* Smaller checkpoint sizes
* Efficient deployment

---

## PEFT (Parameter Efficient Fine-Tuning)

### Concepts Learned

* Adapter-based training
* Freezing pretrained weights
* Training only lightweight layers
* Saving and loading adapter checkpoints

### Workflow

1. Load pretrained model
2. Configure LoRA
3. Apply PEFT adapters
4. Fine-tune on custom dataset
5. Save adapter weights
6. Reload adapters for inference

---

## Hands-On Implementation

### Fine-Tuning Pipeline

Built a complete LoRA training workflow:

* Dataset creation
* Tokenization
* Data collation
* Trainer API usage
* Model training
* Adapter saving
* Adapter loading
* Text generation

---

## Benchmarking Experiments

Conducted benchmarking on multiple LoRA configurations:

| Rank | Alpha |
| ---- | ----- |
| 4    | 8     |
| 8    | 16    |
| 16   | 32    |
| 32   | 64    |

### Metrics Measured

* Training Time
* GPU Memory Usage
* Final Training Loss
* Trainable Parameters
* Generated Output Quality

### Observations

* Higher rank increases trainable parameters.
* Training time increases with rank.
* GPU memory consumption grows gradually.
* Larger ranks provide higher adaptation capacity.

---

## GPU & Environment Troubleshooting

### Issues Encountered

* Torch and TorchVision version incompatibility
* CUDA dependency conflicts
* NCCL symbol errors
* Device mismatch (CPU vs GPU)
* PEFT dependency issues
* TorchAO compatibility problems

### Solutions Applied

* Migrated workflow to Google Colab
* Reinstalled compatible PyTorch versions
* Corrected CUDA setup
* Fixed device placement issues
* Disabled unnecessary logging services

---

## Tools & Libraries Used

* Python
* PyTorch
* Hugging Face Transformers
* PEFT
* Datasets
* Pandas
* Google Colab
* CUDA
* NVIDIA Tesla T4 GPU

---

## Key Learnings

* Transformer architecture workflow
* Tokenization and embeddings
* Pretrained model usage
* LoRA fine-tuning strategy
* PEFT framework fundamentals
* GPU-based model training
* Benchmarking methodologies
* Troubleshooting ML environments

---

## Outcome

Successfully built and executed a complete parameter-efficient fine-tuning workflow using LoRA and PEFT, benchmarked multiple configurations, and gained hands-on experience with modern LLM adaptation techniques on GPU infrastructure.
