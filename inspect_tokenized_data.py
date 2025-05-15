import os
from transformers import AutoTokenizer

# load tokenizer
tokenizer = AutoTokenizer.from_pretrained("models/tinyllama")

# path to transcripts file
transcript_dir = "data/transcripts"
transcript_files = sorted([f for f in os.listdir(transcript_dir) if f.endswith(".txt")])

# loop through each transcript
for filename in transcript_files:
    file_path = os.path.join(transcript_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    print(f"\n--- {filename} ---")
    print("Original Text:")
    print(text[:300] + ("..." if len(text) > 300 else ""))  # Preview first 300 chars

    # tokenize
    tokens = tokenizer.tokenize(text)
    input_ids = tokenizer.encode(text)

    print("\nTokenized Tokens:")
    print(tokens[:30], "...")  # we can change first 30 tokens

    print("\nToken IDs:")
    print(input_ids[:30], "...")  # we can change first 30 token IDs
