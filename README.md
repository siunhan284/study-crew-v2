# study-crew-v2

AI-powered study assistant built with CrewAI.  
Upload study materials (PDFs), and interact with an intelligent agent crew to generate summaries and structured notes.

---

## 🚀 Features

- 🧠 Extracts text from PDF study material  
- ✍️ Generates concise summaries and structured notes  
- 🤖 Modular CrewAI agent orchestration  
- ⚙️ Extensible tool setup and agent config via YAML  

---

## 📁 Project Structure

```
study_crew_v2/
├── pyproject.toml
├── poetry.lock
├── knowledge/             # Upload your PDF files here
├── src/
│   └── study_crew_v2/
│       ├── main.py        # Entrypoint to run the crew
│       ├── crew.py        # Crew and agent assembly
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── tools/
│           └── custom_tool.py
├── .env.example           # Example environment variables
```

---

## 🛠️ Installation

> This project uses [Poetry](https://python-poetry.org/) for dependency management.

### 1. Clone the repo

```bash
git clone https://github.com/YOUR-USERNAME/study-crew-v2.git
cd study-crew-v2
```

### 2. Install Poetry (if not already installed)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or via pipx:

```bash
pipx install poetry
```

### 3. Install dependencies

```bash
poetry install
```

### 4. Create `.env` file

Duplicate the `.env.example` file and fill in your API keys and configuration:

```bash
cp .env.example .env
```

Edit `.env` with your Azure OpenAI details.

---

## 🧪 Running the Project

### Upload study materials

Place all your `.pdf` files in the `knowledge/` directory.

### Start the AI Crew

```bash
poetry run run_crew
```

---

## 🔐 .env Configuration

Example `.env.example`:

```
model=azure/gpt-35-turbo
AZURE_OPENAI_API_KEY=your_azure_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-05-01-preview # API version for Azure OpenAI
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-35-turbo # Deployment name for Azure OpenAI

OPENAI_API_KEY=your_azure_api_key_here
```

> Both Azure OpenAI and OpenAI key fields are set for compatibility. Use Azure credentials for both.

---

## 🧩 Dependencies

- `crewai[tools]`
- `openai`, `langchain`, `langchain-openai`, `langchain-core`, `langchain-tools`
- `pymupdf` for PDF parsing

All handled via Poetry in `pyproject.toml`.

---

## ✍️ Author

**Harsh Vardhan Sharma**

[GitHub Profile](https://github.com/code-master-harsh)

---