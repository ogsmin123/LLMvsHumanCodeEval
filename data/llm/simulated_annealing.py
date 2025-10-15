import math
import random

def simulated_annealing(objective_function, initial_solution, temperature, cooling_rate, iteration_limit):
    """
    Perform simulated annealing to find a solution that minimizes the objective function.

    :param objective_function: A function to minimize.
    :param initial_solution: Initial guess for the solution.
    :param temperature: Initial temperature for the annealing process.
    :param cooling_rate: Rate at which the temperature decreases.
    :param iteration_limit: Maximum number of iterations to perform.
    :return: A solution that approximately minimizes the objective function.
    """
    # Start with the initial solution
    current_solution = initial_solution
    current_value = objective_function(current_solution)
    
    # Best solution found
    best_solution = current_solution
    best_value = current_value

    # Iterate until the temperature is effectively zero or we hit the iteration limit
    iteration = 0
    while temperature > 1e-10 and iteration < iteration_limit:
        # Generate a new candidate solution by making a small random change to the current solution
        candidate_solution = current_solution + random.uniform(-1, 1)
        candidate_value = objective_function(candidate_solution)

        # Calculate the change in the objective function
        delta_value = candidate_value - current_value

        # Decide whether to accept the new solution
        if delta_value < 0 or random.random() < math.exp(-delta_value / temperature):
            current_solution = candidate_solution
            current_value = candidate_value

            # Update the best solution found
            if candidate_value < best_value:
                best_solution = candidate_solution
                best_value = candidate_value

        # Cool down the temperature
        temperature *= cooling_rate
        iteration += 1

    return best_solution

# Example usage:
# Define an objective function to minimize
def objective_function(x):
    return x**2 + 4*math.sin(5*x) + 0.1*x**4

# Parameters for simulated annealing
initial_solution = 0.0
temperature = 10.0
cooling_rate = 0.99
iteration_limit = 1000

# Find the solution
solution = simulated_annealing(objective_function, initial_solution, temperature, cooling_rate, iteration_limit)
print("Found solution:", solution)
print("Objective function value:", objective_function(solution))