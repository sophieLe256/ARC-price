# src/evaluation.py

def evaluate_model(model, test_data):
    predictions = {}
    for task_id, task in test_data.items():
        predictions[task_id] = []
        for test_case in task['test']:
            input_grid = test_case['input']
            predicted_output = model(input_grid)
            predictions[task_id].append({"attempt_1": predicted_output, "attempt_2": predicted_output})
    return predictions

if __name__ == "__main__":
    import data_loader
    from model import simple_model

    data = data_loader.load_data({
        "test": "data/arc-agi_test_challenges.json"
    })
    
    predictions = evaluate_model(simple_model, data["test"])
    print(predictions)
