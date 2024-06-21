# src/visualization.py

import matplotlib.pyplot as plt

def visualize_grid(grid, title=""):
    plt.imshow(grid, cmap='viridis')
    plt.title(title)
    plt.show()

def visualize_task(task_data, task_solutions=None):
    for i, example in enumerate(task_data['train']):
        visualize_grid(example['input'], title=f"Train Input {i+1}")
        if task_solutions:
            visualize_grid(task_solutions['train'][i]['output'], title=f"Train Output {i+1}")

if __name__ == "__main__":
    import data_loader
    data = data_loader.load_data({
        "training": "data/arc-agi_training_challenges.json",
        "training_solutions": "data/arc-agi_training_solutions.json"
    })
    task_id = list(data["training"].keys())[0]
    visualize_task(data["training"][task_id], data["training_solutions"][task_id])
