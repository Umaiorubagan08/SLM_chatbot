# training/train_model.py

from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_from_disk

# Load dataset
dataset = load_from_disk("data/tokenized_dataset")

# Load pre-trained model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Training configuration
training_args = TrainingArguments(
    output_dir="models/tinyllama",
    per_device_train_batch_size=1,
    num_train_epochs=3,
    logging_dir="logs",
    logging_steps=10,
    save_strategy="epoch",
    save_total_limit=3  # Keeps only last 3 checkpoints
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Start training
trainer.train()

# Save final model and tokenizer
trainer.save_model("models/tinyllama")
tokenizer.save_pretrained("models/tinyllama")
