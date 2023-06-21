import random

class Individual:
    def __init__(self, genotype):
        self.genotype = genotype
        self.fitness = 0

def generate_random_individual(num_items):
    genotype = [random.randint(0, 1) for _ in range(num_items)]
    return Individual(genotype)

def evaluate_fitness(individual, weights, values, capacity):
    total_weight = sum(individual.genotype[i] * weights[i] for i in range(len(individual.genotype)))
    total_value = sum(individual.genotype[i] * values[i] for i in range(len(individual.genotype)))

    if total_weight > capacity:
        individual.fitness = 0
    else:
        individual.fitness = total_value

def perform_crossover(parent1, parent2):
    offspring_genotype = []
    for i in range(len(parent1.genotype)):
        if random.random() < 0.5:
            offspring_genotype.append(parent1.genotype[i])
        else:
            offspring_genotype.append(parent2.genotype[i])
    return Individual(offspring_genotype)

def perform_mutation(individual, mutation_rate):
    for i in range(len(individual.genotype)):
        if random.random() < mutation_rate:
            individual.genotype[i] = 1 - individual.genotype[i]

def select_parents(population):
    tournament_size = 3
    selected_parents = []
    for _ in range(2):
        tournament = random.sample(population, tournament_size)
        selected_parents.append(max(tournament, key=lambda ind: ind.fitness))
    return selected_parents

def genetic_algorithm_knapsack(weights, values, capacity, population_size, num_generations, crossover_rate, mutation_rate):
    population = []
    num_items = len(weights)

    # Generate initial population
    for _ in range(population_size):
        individual = generate_random_individual(num_items)
        evaluate_fitness(individual, weights, values, capacity)
        population.append(individual)

    best_solution = max(population, key=lambda ind: ind.fitness)

    for generation in range(num_generations):
        new_population = []

        while len(new_population) < population_size:
            # Selection
            parents = select_parents(population)

            # Crossover
            if random.random() < crossover_rate:
                offspring = perform_crossover(parents[0], parents[1])
            else:
                offspring = parents[0]  # No crossover, copy parent

            # Mutation
            perform_mutation(offspring, mutation_rate)

            # Evaluate fitness
            evaluate_fitness(offspring, weights, values, capacity)
            new_population.append(offspring)

        population = new_population

        # Update best solution
        current_best = max(population, key=lambda ind: ind.fitness)
        if current_best.fitness > best_solution.fitness:
            best_solution = current_best

    return best_solution.genotype, best_solution.fitness

# Predefined problem instance
values = [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367,
          853655, 1826027, 65731, 901489, 577243, 466257, 369261]
weights = [382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111,
           323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684]
capacity = 6404180

population_size = 50
num_generations = 100
crossover_rate = 0.8
mutation_rate = 0.1

best_genotype, best_fitness = genetic_algorithm_knapsack(weights, values, capacity, population_size, num_generations, crossover_rate, mutation_rate)

# Print the optimal solution in 0-1 format
print("Best solution:")
for i in range(len(best_genotype)):
    print(best_genotype[i], end=" ")
print()

# Calculate quality percentage
quality_percentage = (best_fitness / sum(values)) * 100
print("Quality Percentage:", quality_percentage)
