# Subscription Finder

An intelligent recommendation system for subscription services using LangChain, ChromaDB, and local transformer models.

## Features

- Vector-based search for subscription recommendations
- Semantic understanding of user preferences using sentence-transformers
- Local LLM inference with Hugging Face models - no API keys required!
- Filtering by price, category, and other attributes
- FastAPI web interface for easy interaction

## Requirements

- Python 3.8+
- 8GB+ RAM recommended (for running the LLM)
- Disk space for model downloads (~1-2GB)

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application:

```bash
python app.py
```

This starts the FastAPI server at http://localhost:8000

Alternatively, you can run with uvicorn directly:

```bash
uvicorn app:app --reload
```

## How It Works

1. **Sentence Embeddings**: The application uses the `all-MiniLM-L6-v2` model to convert subscription descriptions into vector embeddings.

2. **Vector Database**: ChromaDB stores these embeddings along with metadata about each subscription.

3. **Local LLM**: A TinyLlama model runs completely locally to generate natural language recommendations.

4. **Retrieval-Augmented Generation (RAG)**: When a user submits preferences, the system:
   - Converts the query to an embedding
   - Finds similar subscriptions in ChromaDB
   - Passes context about relevant subscriptions to the LLM
   - Formats a personalized recommendation response

## Project Structure

- `subscription_finder.py`: Core recommendation engine
- `app.py`: FastAPI web application
- `templates/`: HTML templates
- `chroma_db/`: Vector database storage (created on first run)

## Adding Your Own Data

To add your own subscription data, modify the `create_sample_data()` function in `subscription_finder.py`. The system will automatically create embeddings for your new data.

## Performance Considerations

- For better performance, consider using a more powerful LLM model and enabling GPU acceleration by changing `device_map="auto"` in the model configuration.
- The first run will download models which may take some time depending on your internet connection.