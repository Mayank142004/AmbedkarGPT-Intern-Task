# AmbedkarGPT-Intern-Task

#  AmbedkarGPT – RAG-based Q&A System 

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Ollama](https://img.shields.io/badge/LLM-Ollama%20Mistral%207B-red)

A completely **local**, **offline**, and **cost-free** Retrieval-Augmented Generation (RAG) system built using:

- **LangChain**
- **ChromaDB**
- **HuggingFace Embeddings** (`all-MiniLM-L6-v2`)
- **Ollama (Mistral 7B)**

This CLI tool answers questions about the provided excerpt from  
📘 *Dr. B. R. Ambedkar’s — Annihilation of Caste*.

---

# 📚 Table of Contents
- [📁 Project Overview](#-project-overview)
- [🏗 Architecture](#-architecture)
- [⚙️ Installation Guide](#️-installation-guide)
- [▶️ Usage Instructions](#️-usage-instructions)
- [🛠 Troubleshooting](#-troubleshooting)
- [📋 Assignment Checklist](#-assignment-checklist)
- [📎 Files Included](#-files-included)

---

# 📁 Project Overview
This project demonstrates a functional RAG pipeline that:

1. Loads the **speech.txt** file  
2. Splits text into chunks  
3. Creates embeddings using **HuggingFace MiniLM-L6-v2**  
4. Stores vectors locally using **ChromaDB**  
5. Retrieves relevant chunks based on user questions  
6. Uses **Ollama Mistral 7B** to generate answers  
7. Allows user interaction through a **command-line interface**

---

# 🏗 Architecture

               ┌──────────────────┐
               │   speech.txt      │
               └─────────┬────────┘
                         │ Load text
                         ▼
               ┌──────────────────┐
               │  Text Splitter   │
               │ (Chunks 500/50)  │
               └─────────┬────────┘
                         │ Create documents
                         ▼
               ┌────────────────────────┐
               │ HF Embeddings          │
               │ (all-MiniLM-L6-v2)     │
               └─────────┬──────────────┘
                         │ Store vectors
                         ▼
               ┌──────────────────┐
               │   ChromaDB       │
               │ Local Vectorstore│
               └─────────┬────────┘
                         │ Retrieve top-k chunks
                         ▼
               ┌──────────────────┐
               │   RetrievalQA     │
               │  (LangChain)      │
               └─────────┬────────┘
                         │ Send context
                         ▼
               ┌──────────────────┐
               │   Ollama LLM     │
               │  (Mistral 7B)    │
               └─────────┬────────┘
                         ▼
               ┌──────────────────┐
               │  Final Answer     │
               └──────────────────┘

---

# ⚙️ Installation Guide

<details>
<summary><strong>1️⃣ Clone the Repository</strong></summary>

```bash
git clone https://github.com/<your-username>/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task
</details>


<details> <summary><strong>2️⃣ Create & Activate Virtual Environment</strong></summary>
