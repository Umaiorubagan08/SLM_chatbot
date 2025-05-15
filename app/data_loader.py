import json
import pandas as pd

def load_data(json_path="data/structured_data.json"):
    with open(json_path, "r") as f:
        return json.load(f)
