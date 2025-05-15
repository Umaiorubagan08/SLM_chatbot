from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from app.data_loader import load_data

model_dir = "models/tinyllama"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForCausalLM.from_pretrained(model_dir)
structured_data = load_data()

def search_structured_data(prompt):
    prompt_lower = prompt.lower()
    for item in structured_data:
        if (
            item['property_type'] in prompt_lower and
            item['location'].lower() in prompt_lower and
            (item['budget'] and item['budget'].split()[0] in prompt_lower)
        ):
            return f"Yes, there is a {item['property_type']} available in {item['location']} within your budget."
    return None

def generate_response(prompt, chat_history=[]):
    # First, try to match with structured data using later i will try to feed in SLM
    data_response = search_structured_data(prompt)
    if data_response:
        return data_response

    # SLM model
    input_text = "\n".join(chat_history + [prompt])
    inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(inputs, max_length=512, pad_token_id=tokenizer.eos_token_id)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reply.split(prompt)[-1].strip()
