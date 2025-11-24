# Research Help Agent

A minimal end-to-end system designed to assist researchers by automatically finding, downloading, analyzing, and answering questions about scientific papers.

## Features

* **Automated Research Fetching**: Downloads research PDFs from online sources.
* **Text Extraction**: Converts PDFs into plain text for processing.
* **Document Ingestion**: Generates embeddings and stores them in a vector database (FAISS).
* **Question Answering**: Answers research and technical questions by retrieving relevant document sections.
* **CrewAI Workflow**: Manages agents that automate tasks such as downloading, extracting, and indexing documents.
* **FastAPI API**: Provides endpoints for ingestion and question answering.
* **Airflow Automation**: Automates scheduled scraping and ingestion tasks.
* **MLOps Support**: Includes Docker, Kubernetes deployment, and CI/CD pipeline via GitHub Actions.

## Technology Stack

* **Python**: Core language for all modules.
* **FastAPI**: REST API to interact with the system.
* **Requests**: For downloading PDFs.
* **pdfminer.six**: Extracts text from PDFs.
* **Sentence-Transformers**: Generates embeddings for semantic search.
* **FAISS**: Efficient similarity search in high-dimensional vector spaces.
* **CrewAI**: Multi-agent orchestration for automating research workflows.
* **Apache Airflow**: Task scheduling and workflow automation.
* **Docker & Docker Compose**: Containerization.
* **Kubernetes**: Deployment and scalability.
* **GitHub Actions**: Continuous integration and testing.
* **Python-dotenv**: Environment variable management.
* **Pytest**: Testing framework.

## Project Structure

```
research-agent-minimal/
├── README.md
├── requirements.txt
├── .github/
│   └── workflows/ci.yml
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   └── deployment.yaml
├── airflow/
│   └── dags/
│       └── scrape_dag.py
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   ├── scraper.py       # download PDFs
│   ├── extractor.py     # PDF → text
│   ├── ingest.py        # embeddings + FAISS
│   ├── crew_agent.py    # minimal CrewAI flow
│   └── qa.py            # retrieval
└── scripts/
    └── start.sh
```

This repository is minimal and easily extendable for building lightweight research automation tools.

