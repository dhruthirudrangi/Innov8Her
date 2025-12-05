# Innov8Her
Overnight_Hackathon_RVCE
Intelligent Candidate Discovery and Matching Platform 

#  AI-Powered Intelligent Candidate Discovery & Matching Platform

An end-to-end **AI recruitment engine** that automatically reads job descriptions (JD), discovers candidates across the web, analyzes their GitHub profiles, and ranks them using deep semantic intelligence.

This platform combines **NLP, vector embeddings, web search APIs, GitHub analysis, and robust document parsing** into a single, automated hiring pipeline.

---

## Key Features

### 1.  Job Description Analyzer
A powerful document processor that extracts all critical requirements from a JD (PDF, DOCX, or even scanned PDFs via **OCR**).

| Extracted Data | Example |
| :--- | :--- |
| **Tech Stack & Skills** | Python, AWS, MiniLM |
| **Semantic Vector** | Semantic Embedding (1x384 dimension) |
| **Metadata** | Seniority Level, Domain, Location |

### 2.  Multi-Source Candidate Discovery

We utilize smart, legal search methods to find and parse public candidate data.

* **Google Resume Finder:** Uses the **Serper API** with targeted queries (e.g., `"Software Engineer" resume filetype:pdf`) to discover and download public resumes for parsing.
* **LinkedIn SERP Search:** Finds public profile URLs and snippets legally without scraping: `site:linkedin.com/in "python developer" "bangalore"`.

### 3.  GitHub Profile Analyzer: Technical Validation

This module goes beyond vanity metrics to assess actual coding ability. Using the GitHub REST API, the system extracts and computes:

* **Code Quality:** Analyzes language distribution, commit frequency, and technical debt indicators.
* **Repo Score:** Based on stars, forks, and project activity.
* **Technical Strength Indicator:** A final metric quantifying hands-on coding skill.

---

##  Intelligent AI Matching Engine

Our ranking system uses a weighted, three-dimensional scoring model for accuracy:

$$
\text{Final Score} = (0.55 \times \text{Skill Score}) + (0.30 \times \text{Embedding Score}) + (0.15 \times \text{Responsibility Score})
$$

###  Scoring Breakdown

| Component | Weight | Description |
| :--- | :--- | :--- |
| **Skill Score** | **55%** | Precision and recall on exact keyword skill overlap. |
| **Embedding Score** | **30%** | **Semantic similarity** using **MiniLM embeddings**. Measures conceptual fit (e.g., "Deep Learning" matches "Neural Networks"). |
| **Responsibility Score** | **15%** | Compares candidate experience/responsibilities against JD expectations. |

---

##  Tech Stack & Dependencies

| Category | Tools & Libraries | Purpose |
| :--- | :--- | :--- |
| **AI & NLP** | `SentenceTransformer` (MiniLM-L3-v2), `spaCy`, `YAKE`, `NumPy` | Semantic embedding generation, keyphrase extraction, and similarity calculation. |
| **Parsing** | `pdfplumber`, `pytesseract` (OCR), `pdf2image`, `python-docx` | Robustly handle various resume file formats, including scanned documents. |
| **Search & APIs** | `Serper Google Search API`, `GitHub REST API`, `requests` | External data collection and profile analysis. |
| **Frontend** | `Streamlit` | Interactive, rapid prototyping user interface. |

---

##  Installation & Setup

### 1️ Clone the project

1)clone the repo ,go to the codes folder,install requirements.txt
2)Install Python dependencies
 Install Tesseract OCR (External Dependency)
Note: Tesseract must be installed on your system to process scanned PDFs. Please follow platform-specific instructions online.

 set Environment Variables
Create a file named .env in the project root:
SERPER_API_KEY=your_serper_api_key
GITHUB_TOKEN=your_github_token_with_repo_scope

# AI-powered HR Policy Assistant
built using Python, LangChain, Gradio, and the free Gemini 1.5 Flash API. It loads company policy PDFs, splits them into text chunks, embeds them using MiniLM embeddings, and stores them in a Chroma vector database for fast semantic search. When a user asks a question, the system performs Retrieval-Augmented Generation (RAG) by retrieving relevant policy chunks and passing them along with the user query to the Gemini 2.5 Flash model, ensuring grounded and document-accurate answers. The interface is provided through a simple Gradio chat UI, making it easy for employees to ask questions about leaves, WFH rules, benefits, compliance, and other HR topics.
# certificate verification
This feature is an automated certificate verification pipeline that extracts and validates information directly from uploaded certificate images. Using OCR and lightweight text parsing, the system reads the candidate’s name, course title, score, ID/roll number, and session details, then compares them against the details claimed by the candidate to detect mismatches or potential fraud. It also interprets the course session (for example, a month–month–year range) to estimate the course end date, compute a configurable validity period, and determine whether the certificate is currently valid. The output is an “employer view” that presents all extracted fields, verification checks, and validity status in a clean, human‑readable format, making it easy for recruiters or institutions to quickly trust—or question—the authenticity of a certificate.
