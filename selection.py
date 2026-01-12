
# selection.py

import random

# For all the functions here, it's strongly recommended to
# review the documentation for Python's random module:
# https://docs.python.org/3/library/random.html

# Parent selection functions---------------------------------------------------
def uniform_random_selection(population, n, **kwargs):
    # TODO: select n individuals uniform randomly
    # Select n individuals uniform randomly with replacement
    selected_individuals = [random.choice(population) for _ in range(n)]
    return selected_individuals
    pass


def k_tournament_with_replacement(population, n, k, **kwargs):
    # TODO: perform n k-tournaments with replacement to select n individuals
    selected_individuals = []
    for _ in range(n):
        # Sample k individuals without replacement for the tournament
        tournament_contestants = random.sample(population, k)
        # Select the most fit individual from the tournament
        winner = max(tournament_contestants, key=lambda individual: individual.fitness)
        # Add the winner to the selected individuals
        selected_individuals.append(winner)
    return selected_individuals
    pass


def fitness_proportionate_selection(population, n, **kwargs):
    # TODO: select n individuals using fitness proportionate selection
    # Extract fitness values from the population
    fitness_values = [individual.fitness for individual in population]
    
    # Check if there are any negative fitness values
    min_fitness = min(fitness_values)
    if min_fitness < 0:
        # Calculate selection weights by subtracting the minimum fitness from all fitness values
        selection_weights = [fitness - min_fitness for fitness in fitness_values]
    else:
        # Use fitness values directly as selection weights
        selection_weights = fitness_values
    
    # Handle the edge case where all fitnesses are negative and equal
    if all(weight == 0 for weight in selection_weights):
        # In this case, selection probabilities are uniform
        selection_weights = [1] * len(population)
    
    # Select n individuals with replacement based on selection weights
    selected_individuals = random.choices(population, weights=selection_weights, k=n)
    
    return selected_individuals
    pass



# Survival selection functions-------------------------------------------------
def truncation(population, n, **kwargs):
    # TODO: perform truncation selection to select n individuals
    # Perform truncation selection to select n individuals
    # Sort the population based on fitness in descending order
    sorted_population = sorted(population, key=lambda individual: individual.fitness, reverse=True)
    # Select the top n individuals
    selected_individuals = sorted_population[:n]
    return selected_individuals
    pass


def k_tournament_without_replacement(population, n, k, **kwargs):
    # TODO: perform n k-tournaments without replacement to select n individuals
    # Note: an individual should never be cloned from surviving twice!
    # Also note: be careful if using list.remove(), list.pop(), etc.
    # since this can be EXTREMELY slow on large populations if not handled properly
    # A better alternative to my_list.pop(i) is the following:
    # my_list[i] = my_list[-1]
    # my_list.pop()
    # Perform n k-tournaments without replacement to select n individuals
    selected_individuals = []
    population_copy = population[:]
    
    for _ in range(n):
        # Sample k individuals without replacement for the tournament
        tournament_contestants = random.sample(population_copy, k)
        # Select the most fit individual from the tournament
        winner = max(tournament_contestants, key=lambda individual: individual.fitness)
        # Add the winner to the selected individuals
        selected_individuals.append(winner)
        # Remove the winner from the population copy to avoid replacement
        population_copy.remove(winner)
    
    return selected_individuals
    pass



# Yellow deliverable parent selection function---------------------------------
def stochastic_universal_sampling(population, n, **kwargs):
    # Recall that yellow deliverables are required for students in the grad
    # section but bonus for those in the undergrad section.
    # TODO: select n individuals using stochastic universal sampling
    pass