# main.py

import src.data_loader as data_loader
import src.visualization as visualization
import src.evaluation as evaluation
import src.submissions as submission
from src.model import simple_model

def main():
    # Load data
    data = data_loader.load_data({
        "training": "data/arc-agi_training_challenges.json",
        "training_solutions": "data/arc-agi_training_solutions.json",
        "test": "data/arc-agi_test_challenges.json"
    })

    # Visualize some training data
    task_id = list(data["training"].keys())[0]
    visualization.visualize_task(data["training"][task_id], data["training_solutions"][task_id])

    # Evaluate the model on test data
    predictions = evaluation.evaluate_model(simple_model, data["test"])

    # Save the predictions
    submission.save_submission(predictions)

if __name__ == "__main__":
    main()
