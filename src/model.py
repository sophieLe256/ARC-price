# src/model.py

def simple_model(input_grid):
    # A very simple model that just duplicates the input grid horizontally
    output_grid = [row * 2 for row in input_grid]
    return output_grid

if __name__ == "__main__":
    import data_loader
    import visualization

    data = data_loader.load_data({
        "test": "data/arc-agi_test_challenges.json"
    })
    
    task_id = list(data["test"].keys())[0]
    test_input = data["test"][task_id]['test'][0]['input']
    
    predicted_output = simple_model(test_input)
    
    visualization.visualize_grid(test_input, title="Test Input")
    visualization.visualize_grid(predicted_output, title="Predicted Output")
