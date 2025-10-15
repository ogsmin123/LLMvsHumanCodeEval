# Hill Climbing Algorithm Implementation

def hill_climbing(objective_function, initial_state, neighbors_function, max_iterations=1000):
    """
    Perform the hill climbing algorithm to find a local maximum of the objective function.

    :param objective_function: A function that takes a state and returns a numeric value representing
                               the "height" or "value" of that state.
    :param initial_state: The starting point for the hill climbing algorithm.
    :param neighbors_function: A function that takes a state and returns a list of neighboring states.
    :param max_iterations: The maximum number of iterations to perform (default is 1000).
    :return: A tuple containing the best state found and its corresponding value.
    """
    current_state = initial_state
    current_value = objective_function(current_state)

    for iteration in range(max_iterations):
        # Generate neighbors of the current state
        neighbors = neighbors_function(current_state)
        
        # Evaluate the neighbors to find the best one
        next_state = current_state
        next_value = current_value
        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)
            # If a better neighbor is found, update the next state and value
            if neighbor_value > next_value:
                next_state = neighbor
                next_value = neighbor_value

        # If no better neighbor is found, we have reached a local maximum
        if next_value <= current_value:
            break

        # Move to the best neighbor
        current_state = next_state
        current_value = next_value

    return current_state, current_value

# Example usage:
# Define an example objective function and neighbors function
def example_objective_function(state):
    # A simple quadratic function with a maximum at x = 3
    return -(state - 3) ** 2 + 9

def example_neighbors_function(state):
    # Generate neighbors by incrementing or decrementing the state
    return [state - 1, state + 1]

# Run the hill climbing algorithm
best_state, best_value = hill_climbing(example_objective_function, initial_state=0, neighbors_function=example_neighbors_function)
print(f"Best state: {best_state}, Best value: {best_value}")