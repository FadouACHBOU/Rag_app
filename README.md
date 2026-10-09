# Rag Application
This is a minimal implementation of the RAG model for question answering.

## Requierments 
- Python 3.11 or later
## Install Python with Miniconda
1 - Download ananconda from [here](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh).

2 - Create a new environment using the following command:

```bash
conda create -n mini-rag python=3.8
conda activate mini-rag
```
## Setup you command line interface for better readability
### Optional

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
# Installation
## Install the required packages
```bash
$ pip install -r requirements.txt
```
## Setup the environment variables
```bash
$ cp .env.example .env
```
Set your environment variables in the .env file. Like OPENAI_API_KEY value.
## Run the FastAPI server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
## POSTMAN Collection
Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)