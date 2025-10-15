import random
import copy

def tabu_search(distances, num_iterations, tabu_size, candidate_list_size):
    # Initialize the best solution with a random permutation of cities
    num_cities = len(distances)
    best_solution = list(range(num_cities))
    random.shuffle(best_solution)
    best_cost = calculate_cost(best_solution, distances)
    
    # Initialize the current solution to the best solution found so far
    current_solution = best_solution[:]
    current_cost = best_cost
    
    # Tabu list to store recently visited solutions
    tabu_list = []
    
    for _ in range(num_iterations):
        # Generate candidate solutions by swapping two cities in the current solution
        candidate_solutions = []
        for _ in range(candidate_list_size):
            candidate = current_solution[:]
            i, j = random.sample(range(num_cities), 2)
            candidate[i], candidate[j] = candidate[j], candidate[i]
            candidate_solutions.append(candidate)
        
        # Evaluate the candidate solutions and select the best one not in the tabu list
        best_candidate = None
        best_candidate_cost = float('inf')
        for candidate in candidate_solutions:
            candidate_cost = calculate_cost(candidate, distances)
            if candidate not in tabu_list and candidate_cost < best_candidate_cost:
                best_candidate = candidate
                best_candidate_cost = candidate_cost
        
        # Update the current solution to the best candidate found
        current_solution = best_candidate
        current_cost = best_candidate_cost
        
        # Update the tabu list with the current solution
        tabu_list.append(current_solution)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        
        # Update the best solution found so far if the current one is better
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
    
    return best_solution, best_cost

def calculate_cost(solution, distances):
    # Calculate the total distance of the path represented by the solution
    total_cost = 0
    for i in range(len(solution)):
        total_cost += distances[solution[i]][solution[(i + 1) % len(solution)]]
    return total_cost