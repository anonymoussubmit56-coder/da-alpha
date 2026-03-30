## DAα: Controllable Vocabulary Modulation for LLMs

This repository contains the experimental framework and evaluation pipeline for **DAα**, a lightweight inference-time approach for controlling both domain fidelity and audience-aware vocabulary adaptation in large language model (LLM) generation.

The method combines:
- **Retrieval gating** (via a threshold parameter τ) to control domain and topic relevance, and  
- A continuous parameter **α** to modulate vocabulary sophistication from novice to expert levels.

### Key Features
- 🎯 **Controllable generation** without fine-tuning  
- 🧠 **Semantic consistency preservation** across different levels of vocabulary adaptation  
- 🔁 **Dynamic vocabulary modulation** using a single parameter (α)  
- 📊 Integrated evaluation with automatic metrics (BERTScore, ROUGE-L, TTR, entropy) and human studies  

### What this repository includes
- Experimental setup and evaluation scripts  
- Data processing and benchmarking utilities  
- Reproducibility tools for reported results  

> ⚠️ Note: The core implementation of the DAα framework is not included in this repository.

### Motivation
Adapting language to different audiences (e.g., novice vs. expert) is essential in many applications, yet most LLM approaches lack fine-grained control over how information is expressed.  
DAα addresses this by enabling controlled variation in vocabulary while preserving the underlying meaning of responses.

### Applications
- Technical documentation  
- Educational content generation  
- Compliance and policy communication  
- Multi-audience explanation systems  

### Status
This repository accompanies a research paper currently under submission.
This project implements a steering vector approach for language models, using `sentence-transformers` and `transformers` to semantically guide text generation. The system selects relevant context based on semantic similarity with a given prompt, computes a steering vector, and generates text using a pretrained model (e.g., `phi-2`).

There are two test configurations: **NDC** (e.g., Natural Dialogue Context) and **Programming**, each using different input files (`context.txt` and `questions.txt`), but sharing the same core code.

---

## 📂 Project Structure
```text
.
├── src/                   # Main source code
│   └── main.py
├── ndc/                   # Files for the NDC test
│   ├── context.txt
│   └── questions.txt
├── programming/           # Files for the Programming test
│   ├── context.txt
│   └── questions.txt
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Docker Compose services
└── README.md              # This file

```



---

## ⚙️ Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/) (included with Docker Desktop)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/anonymoussubmit56-coder/da-alpha
cd da-alpha

docker-compose up ndc
docker-compose up programming 

```

### 2. 🛠️ Technologies Used
- Python 3.10
- HuggingFace Transformers
- SentenceTransformers
- PyTorch
- Docker

### 3. 📄 Code Overview (main.py)
- Loads context from context.txt.
- Loads prompts from questions.txt.
- Finds the most semantically relevant context using embeddings.
- Computes a steering vector based on the relevant embeddings.
- Projects the vector to the model’s embedding space.
- Modifies the prompt embeddings using the steering vector (ALPHA as strength).
- Generates output using microsoft/phi-2.

### 4. ⚙️ Configuration Variables
- SIMILARITY_THRESHOLD: Minimum similarity for context to be considered relevant.
- ALPHA: Controls the strength of the steering vector during embedding manipulation.

### 5. 🧪 Optional: Local Setup Without Docker
If you prefer to run locally:
```bash 
pip install -r requirements.txt
python src/main.py

```
Make sure to place the context.txt and questions.txt files at the project root or update the paths in the code.

