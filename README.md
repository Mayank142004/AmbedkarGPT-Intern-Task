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

---

# 2) XML (structured, for tools or docs)
```xml
<?xml version="1.0" encoding="utf-8"?>
<installationGuide>
  <section id="install-python">
    <title>2. Install Python 3.8+</title>
    <verify>python --version</verify>
    <platforms>
      <windows>
        <instructions>Download from https://www.python.org/downloads/windows/ and install (choose "Add to PATH").</instructions>
      </windows>
      <linux>
        <instructions>sudo apt install python3 python3-pip</instructions>
      </linux>
      <macos>
        <instructions>brew install python</instructions>
      </macos>
    </platforms>
  </section>

  <section id="venv">
    <title>3. Create & Activate Virtual Environment</title>
    <windows>
      <command>python -m venv .venv</command>
      <command>.venv\Scripts\Activate.ps1</command>
    </windows>
    <linux_macos>
      <command>python3 -m venv .venv</command>
      <command>source .venv/bin/activate</command>
    </linux_macos>
    <note>You should now see the shell prompt prefixed with "(.venv)".</note>
  </section>

  <section id="install-deps">
    <title>4. Install Required Python Packages</title>
    <command>pip install -r requirements.txt</command>
    <installs>
      <package>langchain</package>
      <package>chromadb</package>
      <package>sentence-transformers</package>
      <package>torch</package>
      <package>ollama python binding</package>
      <package>utilities</package>
    </installs>
  </section>

  <section id="install-ollama">
    <title>5. Install Ollama (Local LLM Runtime)</title>
    <macos_linux>
      <command>curl -fsSL https://ollama.ai/install.sh | sh</command>
    </macos_linux>
    <windows>
      <instructions>Download installer from https://ollama.ai/download</instructions>
    </windows>
    <verify>ollama --version</verify>
  </section>

  <section id="mistral">
    <title>6. Download the Mistral 7B Model</title>
    <command>ollama pull mistral</command>
    <verify>ollama list</verify>
    <expectedOutput>mistral</expectedOutput>
  </section>

  <section id="speech-file">
    <title>7. Ensure speech.txt Is Present</title>
    <contents>
      <file>speech.txt</file>
      <file>main.py</file>
      <file>requirements.txt</file>
      <file>README.md</file>
    </contents>
  </section>

  <section id="clear-chromadb">
    <title>8. (Optional) Clear ChromaDB Cache</title>
    <command>rm -rf chroma_db</command>
    <note>Use this to force a rebuild of embeddings on next run.</note>
  </section>

  <section id="run-app">
    <title>9. Run the Application</title>
    <command>python main.py</command>
    <expectedOutput>AmbedkarGPT (local) — Ask questions based on the provided speech. Type 'exit' or 'quit' to stop.</expectedOutput>
  </section>

  <section id="test-questions">
    <title>10. Test With Questions</title>
    <examples>
      <example>What is the real remedy according to Ambedkar?</example>
      <example>Why does he criticize the shastras?</example>
      <example>Why does he say social reform is insufficient?</example>
    </examples>
  </section>

  <section id="usage">
    <title>Usage Instructions</title>
    <run>python main.py</run>
    <exitCommands>
      <cmd>exit</cmd>
      <cmd>quit</cmd>
    </exitCommands>
    <example>
      <question>What is the real enemy according to Ambedkar?</question>
      <answer>The belief in the sanctity of the shastras...</answer>
    </example>
  </section>

  <section id="troubleshooting">
    <title>Troubleshooting</title>
    <problem id="ollama-not-found">
      <symptom>ollama --version fails</symptom>
      <fix>Reinstall Ollama</fix>
    </problem>
    <problem id="mistral-missing">
      <symptom>Model not found</symptom>
      <fix>ollama pull mistral</fix>
    </problem>
    <problem id="chroma-errors">
      <symptom>Import/Module errors for chromadb</symptom>
      <fix>pip install chromadb --upgrade</fix>
    </problem>
    <problem id="embeddings-slow">
      <symptom>Embeddings slow on first run</symptom>
      <fix>Wait 1–2 minutes while HF model downloads and caches</fix>
    </problem>
    <problem id="low-memory">
      <symptom>OOM or slow performance</symptom>
      <fix>Close other apps, restart, use Linux/WSL; Mistral needs ~5GB RAM minimum</fix>
    </problem>
  </section>

  <section id="checklist">
    <title>Assignment Checklist</title>
    <functionalRequirements>
      <item>Read speech.txt</item>
      <item>Split text into chunks</item>
      <item>Generate embeddings (MiniLM-L6-v2)</item>
      <item>Store vectors in ChromaDB</item>
      <item>Retrieve relevant chunks</item>
      <item>Ollama + Mistral LLM answering</item>
      <item>Build RetrievalQA</item>
      <item>CLI interface</item>
    </functionalRequirements>
    <repoRequirements>
      <repoName>AmbedkarGPT-Intern-Task</repoName>
      <files>
        <file>main.py</file>
        <file>README.md</file>
        <file>requirements.txt</file>
        <file>speech.txt</file>
      </files>
    </repoRequirements>
  </section>

  <section id="files-included">
    <title>Files Included</title>
    <tree>
      <item>AmbedkarGPT-Intern-Task/</item>
      <item>main.py</item>
      <item>requirements.txt</item>
      <item>README.md</item>
      <item>speech.txt</item>
      <item>chroma_db/ (auto-created)</item>
    </tree>
  </section>
</installationGuide>
