# Search Engine API Documentation

## Modules Overview
This documentation provides details on the functionality of each module in the search engine project.

### 1. `porterStemmer.py`
**Description:**
Implements the Porter Stemming algorithm to reduce words to their root forms.

**Methods:**
- `stem(word: str) -> str`: Returns the stemmed version of the input word.

### 2. `QueryGenerator.py`
**Description:**
Processes user queries by tokenizing, removing stop words, and stemming before passing them to the search algorithm.

**Methods:**
- `generate_query(query: str) -> list[str]`: Returns a list of processed tokens from the query.

### 3. `SearchInterface.py`
**Description:**
Provides a graphical user interface (GUI) for the search engine using Tkinter or another GUI library.

**Methods:**
- `setup_ui() -> None`: Initializes and displays the search engine interface.
- `handle_search(query: str) -> None`: Processes user input and displays results.

### 4. `SimilarityRanker.py`
**Description:**
Ranks search results based on similarity measures such as TF-IDF or cosine similarity.

**Methods:**
- `rank_documents(query_vector: list[float], doc_vectors: dict) -> list[tuple[str, float]]`: Returns ranked documents based on similarity scores.

### 5. `StopWordRemover.py`
**Description:**
Removes common stop words from input text.

**Methods:**
- `remove_stopwords(tokens: list[str]) -> list[str]`: Returns a list of tokens with stop words removed.

### 6. `TermDocMatrix.py`
**Description:**
Constructs a term-document matrix for indexing documents.

**Methods:**
- `build_matrix(docs: dict) -> dict`: Returns a term-document matrix for given documents.

### 7. `TokenGenerator.py`
**Description:**
Tokenizes input text into meaningful words.

**Methods:**
- `tokenize(text: str) -> list[str]`: Returns a list of tokens extracted from the input text.

### 8. `mainProgram.py`
**Description:**
Main entry point for the search engine, integrating all modules.

**Methods:**
- `run_search_engine() -> None`: Launches the search engine, initializes indexing, and starts the GUI.

## Usage Example
```python
from mainProgram import run_search_engine

import tkinter as tk
from SearchInterface import SearchApp
if __name__ == "__main__":
    root = tk.Tk()
    app = SearchApp(root)
    app.centerWindow(900, 500)
    root.mainloop()
```

This script initializes the search engine, processes user queries, and displays results through the GUI.

