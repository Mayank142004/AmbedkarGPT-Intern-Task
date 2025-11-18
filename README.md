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

<!-- <details>
<summary><strong>1️ Clone the Repository</strong></summary> -->

```bash


# ambedkargpt_installation_guide: Complete Installation & Recovery Steps (YAML)
# Copy-paste this YAML if you want a machine-readable / structured checklist of ALL steps.
# Sections: clone, python, venv, deps, ollama, mistral, speech-file, chroma, run, tests, troubleshooting, git-cleanup, git-lfs, git-when-github-desktop


repo:
  name: AmbedkarGPT-Intern-Task
  url_template: "https://github.com/Mayank142004/AmbedkarGPT-Intern-Task.git"

steps:
  - id: 1_clone_repo
    title: Clone the repository
    commands:
      - "git clone https://github.com/Mayank142004/AmbedkarGPT-Intern-Task.git"
      - "cd AmbedkarGPT-Intern-Task"
    

  - id: 2_check_python
    title: Verify / install Python 3.8+
    verify_command: "python --version  # or python3 --version"
    windows:
      instructions: "Download from https://www.python.org/downloads/windows/ and install; check 'Add to PATH'."
    linux:
      commands:
        - "sudo apt update"
        - "sudo apt install python3 python3-pip -y"
    macos:
      commands:
        - "brew install python"
    notes: "Ensure Python >= 3.8."

  - id: 3_create_venv
    title: Create & activate virtual environment
    windows:
      commands:
        - "python -m venv .venv"
        - ".venv\\Scripts\\Activate.ps1  # PowerShell"
    linux_macos:
      commands:
        - "python3 -m venv .venv"
        - "source .venv/bin/activate"
    verify: "Your prompt should show '(.venv)'."

  - id: 4_install_deps
    title: Install Python dependencies
    command: "pip install -r requirements.txt"
    notes:
      - "requirements.txt should include langchain, chromadb, sentence-transformers, torch, ollama (python binding), tqdm, python-dotenv etc."
      - "If install fails, try upgrading pip: pip install --upgrade pip"

  - id: 5_install_ollama
    title: Install Ollama (local LLM runtime)
    macos_linux:
      commands:
        - "curl -fsSL https://ollama.ai/install.sh | sh"
    windows:
      instructions: "Download installer from https://ollama.ai/download and follow Windows installer steps."
    verify_command: "ollama --version"
    notes: "Ollama runs models locally — no API keys."

  - id: 6_pull_mistral
    title: Download / pull Mistral 7B model
    command: "ollama pull mistral"
    verify_command: "ollama list  # expect 'mistral' in output"
    notes:
      - "Mistral model download is several GB; ensure sufficient disk space & network."

  - id: 7_ensure_speech
    title: Ensure speech.txt is present
    required_files:
      - "speech.txt"
      - "main.py"
      - "requirements.txt"
      - "README.md"
    notes: "speech.txt should contain the provided Ambedkar excerpt."

  - id: 8_clear_chroma_optional
    title: Optional - Clear ChromaDB cache (rebuild embeddings)
    command: "rm -rf chroma_db"
    windows_note: "On Windows use: rmdir /s /q chroma_db"

  - id: 9_run_app
    title: Run the application (CLI)
    command: "python main.py"
    expected_output: |
      AmbedkarGPT (local) — Ask questions based on the provided speech.
      Type 'exit' or 'quit' to stop.
    usage_notes:
      - "Type questions and press Enter to get answers."
      - "Exit by typing 'exit' or 'quit'."

  - id: 10_test_queries
    title: Example test questions
    examples:
      - "What is the real remedy according to Ambedkar?"
      - "Why does he criticize the shastras?"
      - "Why does he say social reform is insufficient?"

troubleshooting:
  - id: t1_ollama_not_found
    symptom: "ollama command not found / Ollama not installed"
    fix:
      - "Re-run the Ollama install (see step 5)."
      - "Restart terminal or machine after install."
      - "Ensure Ollama's binary is in PATH."

  - id: t2_mistral_missing
    symptom: "model not found / mistral not in 'ollama list'"
    fix:
      - "Run: ollama pull mistral"
      - "Check disk space and network."

  - id: t3_chromadb_errors
    symptom: "ImportError: No module named chromadb"
    fix:
      - "pip install chromadb --upgrade"
      - "Verify virtual env is activated (see step 3)."

  - id: t4_embeddings_first_run_slow
    symptom: "Embedding creation slow, first run stalls"
    fix:
      - "First run downloads HF models; wait 1–3 minutes depending on network."
      - "Ensure the machine is connected to the internet for the first embedding build."

  - id: t5_memory_issues
    symptom: "OOM / very slow / process killed"
    fix:
      - "Mistral 7B needs ~5GB RAM (prefer 8GB+)."
      - "Close background apps, reboot, or use a larger machine/VM."
      - "Run on Linux/WSL for better memory management if on Windows."

