from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

# ✅ Use the correct open-source model
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.3"

login(token="")

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype="auto", device_map="auto")

def generate_text(prompt):
    """Generates AI-based responses using Mistral-7B."""
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if model.device.type == "cuda" else "cpu")
    output = model.generate(**inputs, max_length=150)
    return tokenizer.decode(output[0], skip_special_tokens=True)
