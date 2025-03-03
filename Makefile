# Define Python environment
PYTHON = python3

# Generate embeddings using vector_db.py
generate-embeddings:
	$(PYTHON) -m scripts.generate_embedding

# Clean previous embeddings (if needed)
clean-embeddings:
	rm -rf embeddings/vector_db/*

create-emb-dir:
	mkdir -p embeddings/vector_db/

# Run the full embedding process
refresh-embeddings: clean-embeddings create-emb-dir generate-embeddings