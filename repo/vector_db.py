import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from helper.config import *
from helper.helper import load_json, format_plan


class VectorDBRepo:
    def __init__(self):
        # Initialize ChromaDB client
        self.chroma_client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
        self.subscription_plan_collection = self.chroma_client.get_or_create_collection(name="subscription_plans")
        self.subscription_plans_json = None
        self.embedding_model = None
        if self.subscription_plans_json is None:
            self.load_subscription_plans()
        if self.embedding_model is None:
            self.initialize_embedding_model()

    def load_subscription_plans(self):
        self.subscription_plans_json = load_json(SUBSCRIPTION_PLANS_PATH)

    def initialize_embedding_model(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    def store_plans(self):
        try:
            for plan in self.subscription_plans_json:
                text = format_plan(plan)
                self.subscription_plan_collection.add(documents=[text], metadatas=[{"plan_name": plan["name"]}], ids=[plan["name"]])
            print("✅ Subscription plans stored in ChromaDB!")
        except Exception as e:
            print(e)

    def retrieve_best_match(self,query):
        """Search the vector database for the best-matching subscription plan."""
        results = self.subscription_plan_collection.query(query_texts=[query], n_results=1)

        if results["documents"]:
            # Extract stored metadata
            retrieved_plan = results["documents"][0]
            metadata = results["metadatas"][0]

            return {
                "plan_name": metadata["plan_name"],
                "price": metadata.get("price", "N/A"),
                "features": metadata.get("features", []),
                "best_for": metadata.get("best_for", "General Use")
            }

        return None