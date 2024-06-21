# src/data_loader.py

import json
import os

def load_data(file_paths):
    data = {}
    for key, file_path in file_paths.items():
        with open(file_path, 'r') as file:
            data[key] = json.load(file)
    return data

def main():
    # Paths to your files
    files = {
        "evaluation": "data/arc-agi_evaluation_challenges.json",
        "test": "data/arc-agi_test_challenges.json",
        "training": "data/arc-agi_training_challenges.json",
        "training_solutions": "data/arc-agi_training_solutions.json",
        "sample_submission": "data/sample_submission.json"
    }

    data = load_data(files)
    
    for key in data:
        print(f"\nSample from {key}:")
        print(json.dumps(data[key], indent=2)[:500])  # Print a sample of 500 characters for brevity

if __name__ == "__main__":
    main()
