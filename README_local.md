# News Research Tool 📈

A Streamlit-based application for researching news articles using LLM-powered question answering and source citation. The tool scrapes news articles from provided URLs, generates embeddings, stores them in a FAISS vector database, and allows users to ask questions about the content with cited sources.

## Features

- **Ingest News Articles:** Input URLs to fetch and process news articles automatically.
- **Text Embedding & Storage:** Uses OpenAI embeddings and FAISS for efficient semantic search.
- **LLM-Powered QA:** Ask questions about the ingested articles and get answers with cited sources using OpenAI's GPT-3.5.
- **Streamlit UI:** Simple, interactive web interface.

## Project Structure

```
LLM-Finance Research Tool/
├── main.py                # Main Streamlit app
├── chromdriver.py         # Selenium ChromeDriver setup script
├── faiss_store_openai.pkl # Pickled FAISS vector store (auto-generated)
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignores .env (API keys)
├── README.md              # Project documentation (this file)
└── LLM/                   # Python virtual environment (auto-generated)
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo-url>
cd "LLM-Finance Research Tool"
```

### 2. Create and Activate a Virtual Environment (Optional)

A virtual environment is already present (`LLM/`), but you can create your own:

```bash
python -m venv LLM
# On Windows:
LLM\Scripts\activate
# On Unix/Mac:
source LLM/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root with your OpenAI API key:

```
OPENAI_API_KEY=sk-...
```

### 5. Install ChromeDriver

- Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
- Update the path in `chromdriver.py` if you plan to use or test it.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
2. Enter one or more news article URLs in the sidebar and click **Process URLs**.
3. Once processed, ask questions about the articles in the main input box.
4. Answers and their sources will be displayed.

## Notes

- The `LLM/` folder is a Python virtual environment and not required for deployment.
- The `faiss_store_openai.pkl` file is auto-generated and stores the vector index for fast retrieval.
- The `.env` file is required for API keys and is not tracked by git.
- ChromeDriver must be installed and its path set correctly for Selenium to work.

## Dependencies

See `requirements.txt` for the full list. Key packages:

- streamlit
- langchain
- openai
- selenium
- faiss-cpu
- python-dotenv

## License

[MIT](LICENSE) (add a LICENSE file if needed)

---

_Developed for finance/news research using LLMs and modern NLP tools._
