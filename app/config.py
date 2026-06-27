"""
Application configuration settings.
This file stores all constants and paths used throughout the project.
"""

from pathlib import Path

# ==========================
# Project Paths
# ==========================

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Knowledge base document
DATA_PATH = BASE_DIR / "data" / "support_docs.txt"

# Directory where ChromaDB stores vector embeddings
VECTOR_DB_PATH = BASE_DIR / "chroma_db"

# ==========================
# Embedding Model
# ==========================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================
# Text Splitting
# ==========================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 80

# ==========================
# Retrieval Settings
# ==========================

TOP_K_RESULTS = 3