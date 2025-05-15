from datasets import Dataset
from transformers import AutoTokenizer
import os

transcript_dir = "data/transcripts"
files = [os.path.join(transcript_dir, f) for f in os.listdir(transcript_dir) if f.endswith(".txt")]

texts = []
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        texts.append(f.read())

dataset = Dataset.from_dict({"text": texts})

tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

def tokenize_function(example):
    result = tokenizer(example["text"], truncation=True, padding="max_length", max_length=512)
    result["labels"] = result["input_ids"].copy()
    return result

tokenized_dataset = dataset.map(tokenize_function, batched=True)
tokenized_dataset.save_to_disk("data/tokenized_dataset")
