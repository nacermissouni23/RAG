from llama_index import SimpleDirectoryReader
from src.retrievers.json_reader import PCJSONReader
import os

docs_directory = "data/retrieval_base/gt"

if __name__ == "__main__":
    print("Starting to load documents...")
    try:
        documents = SimpleDirectoryReader(docs_directory, file_extractor={".json": PCJSONReader()}, recursive=True, required_exts=[".json"]).load_data(num_workers=2)
        print(f"Successfully loaded {len(documents)} documents.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
