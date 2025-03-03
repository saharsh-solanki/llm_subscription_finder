from fastapi import FastAPI
from repo.vector_db import VectorDBRepo
from repo.llm_engine import generate_text

app = FastAPI()

db= VectorDBRepo()

@app.post("/ask/")
def ask_question(user_query: str):
    """Handles user queries and returns a formatted subscription plan."""
    retrieved_plan = db.retrieve_best_match(user_query)

    if retrieved_plan:
        # Pass the retrieved plan to the LLM for formatting
        formatted_prompt = (
            f"Format the following subscription plan into a professional and structured response:\n\n"
            f"Plan Name: {retrieved_plan['plan_name']}\n"
            f"Price: {retrieved_plan['price']}\n"
            f"Features: {', '.join(retrieved_plan['features'])}\n"
            f"Best For: {retrieved_plan['best_for']}"
        )
        response = generate_text(formatted_prompt)  # Let the LLM format it
    else:
        # If no match is found, generate a new AI-based suggestion
        ai_prompt = f"Suggest a subscription plan for: {user_query}"
        response = generate_text(ai_prompt)

    return {"response": response}
