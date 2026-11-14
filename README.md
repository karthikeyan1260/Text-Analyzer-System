# 🔍 Text Analyzer System Using Python

A Python-based text analysis application that combines **Word Search Engine** and **Longest Word Finder** into a single project using Object-Oriented Programming (OOP), File Handling, and text-processing techniques.

---

## 📌 Project Overview

The **Text Analyzer System** is designed to automate text-processing operations across individual text files and multiple documents.

This project consists of two main modules:

### Module 1 – Word Search Engine
- Searches for specific keywords across multiple text files.
- Uses an Inverted Index for efficient searching.
- Displays matching documents and relevant information.
- Supports Any Word Match and All Words Match.

### Module 2 – Longest Word Finder
- Identifies the longest word in a document.
- Finds multiple words with the same maximum length.
- Displays the top 5 longest unique words.

---

## 🚀 Run on Google Colab

Run the project directly in Google Colab without installing Python or Jupyter Notebook locally.

[![Open In Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-Sy5wKgGuSm_ZV2rSWIN-1dhEwm7sC0K?usp=sharing)

**How to Run:**
1. Click the Google Colab badge.
2. Open the notebook in Google Colab.
3. Upload or access the required project files.
4. Execute the notebook cells sequentially.
5. Explore both text-processing modules.

**Note:** Replace `YOUR_GOOGLE_COLAB_NOTEBOOK_LINK` with your actual Google Colab notebook URL.

---

## 🎯 Problem Statement

Manually searching for specific keywords and identifying the longest words in large text documents can be time-consuming.

The objective of this project is to develop an automated application that simplifies text searching, word extraction, and text analysis using Python.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Development Environment | Jupyter Notebook |
| Cloud Platform | Google Colab |
| Programming Concepts | Object-Oriented Programming |
| Text Processing | Regular Expressions (`re`) |
| File Handling | `os` |
| Data Serialization | `json` |
| Data Structures | Lists, Dictionaries, Sets |
| Collections | `collections.defaultdict` |
| Structured Data | `dataclasses` |

---

## ⚙️ Key Features

### 1. Word Search Engine

- Searches keywords across multiple text files.
- Supports Any Word Match and All Words Match.
- Builds an Inverted Index for efficient searching.
- Displays matching documents and line numbers.
- Calculates relevance scores based on word frequency.
- Highlights matching keywords.
- Saves and reloads search indexes using JSON.
- Supports searching documents from a specified folder.

### 2. Longest Word Finder

- Extracts words from text documents.
- Identifies the longest word.
- Handles multiple words with equal maximum length.
- Searches across multiple documents.
- Displays the top 5 longest unique words.
- Provides word-length-based analysis.

---

## 🔄 How It Works

### Module 1: Word Search Engine

1. Accepts individual text files or a folder containing multiple documents.
2. Reads and processes document contents.
3. Extracts words using Regular Expressions.
4. Removes predefined stop words.
5. Builds an Inverted Index that maps words to document locations.
6. Performs keyword searches using Any Word Match or All Words Match.
7. Calculates relevance scores based on matching word occurrences.
8. Displays matching documents, highlighted keywords, and line numbers.
9. Saves and reloads the search index using JSON.

### Module 2: Longest Word Finder

1. Reads text from individual files or multiple documents.
2. Extracts words using text-processing techniques.
3. Calculates the length of each word.
4. Identifies the longest word or multiple words with equal maximum length.
5. Compares results across multiple documents.
6. Displays the top 5 longest unique words.

---

## 📂 Project Structure

```text
Text-Analyzer-System/
│
├── Word Search Engine/
│   │
│   ├── word_search_engine.py
│   └── Longest Word Search.ipynb
│
├── Text Analyzer System.ipynb
│
├── Document/
│   │
│   └── Docs/
│       ├── Python.txt
│       ├── Java.txt
│       └── SQL.txt
│
└── README.md
```

### 📁 Folder Description

| File / Folder | Description |
|---|---|
| `Word Search Engine/` | Contains individual implementations of the two modules. |
| `word_search_engine.py` | Python implementation of the Word Search Engine. |
| `Longest Word Search.ipynb` | Notebook implementation of the Longest Word Finder. |
| `Text Analyzer System.ipynb` | Main notebook combining both modules. |
| `Document/` | Main folder for document storage. |
| `Docs/` | Contains sample text documents. |
| `Python.txt` | Python-related sample text data. |
| `Java.txt` | Java-related sample text data. |
| `SQL.txt` | SQL-related sample text data. |

---

## ▶️ How to Run the Project Locally

### Prerequisites

- Python 3.x
- Jupyter Notebook

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd Text-Analyzer-System
```

### Step 3: Open Jupyter Notebook

```bash
jupyter notebook
```

### Step 4: Run the Application

Open:

```text
Text Analyzer System.ipynb
```

Execute the notebook cells sequentially and follow the instructions displayed by the application.

**Note:** Maintain the provided folder structure so the application can access the sample documents correctly.

---

## 📚 My Learnings

Through this project, I gained practical experience in:

- Implementing Object-Oriented Programming concepts.
- Understanding Inverted Indexing.
- Working with Regular Expressions.
- Handling files and directories using Python.
- Using Dictionaries, Lists, Sets, and `defaultdict`.
- Implementing Generators and Iterators.
- Working with JSON Serialization and Deserialization.
- Developing modular and reusable Python applications.
- Combining multiple Python concepts into a practical project.

---

## 🌍 Real-World Applications

1. **Document Search Systems:** Searching specific keywords across multiple documents.
2. **Search Engines:** Building the foundation for keyword-based information retrieval.
3. **Resume Screening:** Identifying technical skills and keywords in resumes.
4. **Digital Libraries:** Searching through large collections of text documents.
5. **Content Analysis:** Extracting useful information from textual data.
6. **Text Processing Applications:** Identifying word patterns and analyzing document content.

---

## 🚀 Future Enhancements

- Add a graphical user interface (GUI).
- Support PDF and DOCX document formats.
- Implement advanced search algorithms.
- Add search history and filtering options.
- Improve search performance for large document collections.

---

## 👨‍💻 Author

**Karthikeyan**

Python Developer | Full Stack Development Enthusiast

---

## ⭐ Support

If you find this project interesting or useful, consider giving this repository a ⭐ Star on GitHub!

**Built with Python. Driven by Learning. Focused on Problem Solving.** 🚀

---

### 🏷️ Tags

`Python` `OOP` `File Handling` `Word Search Engine` `Inverted Index` `Text Processing` `Regular Expressions` `Jupyter Notebook` `Google Colab` `Python Projects`
