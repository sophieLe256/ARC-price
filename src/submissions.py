# src/submission.py

import json

def save_submission(predictions, filename="submission.json"):
    with open(filename, 'w') as file:
        json.dump(predictions, file)

if __name__ == "__main__":
    import evaluation
    import data_loader
    from model import simple_model

    data = data_loader.load_data({
        "test": "data/arc-agi_test_challenges.json"
    })
    
    predictions = evaluation.evaluate_model(simple_model, data["test"])
    save_submission(predictions)
