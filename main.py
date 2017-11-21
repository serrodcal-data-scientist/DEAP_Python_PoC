import random
import math
from deap import base, creator, tools

"""
    genes = andalusia.keys()
    chromosome = random.shuffle(genes)
"""

def raffle(probability):
    return (random.random() < probability)

def euclidean_distance_2D(city_1, city_2, coordinates):
    city_1_coord = coordinates[city_1]
    city_2_coord = coordinates[city_2]
    return math.hypot(city_1_coord[0]-city_2_coord[0], city_1_coord[1]-city_2_coord[1])

def fitness(chromosome, coordinates):
    acc = 0
    for i in range(len(chromosome)-1):
        acc += euclidean_distance_2D(chromosome[i], chromosome[i+1], coordinates)
    return acc + euclidean_distance_2D(chromosome[-1], chromosome[0], coordinates)
    # return sum(euclidean_distance_2D(chromosome[i], chromosome[i+1], coordinates) for i in range(len(chromosome)-1)) + euclidean_distance_2D(chromosome[-1], chromosome[0], coordinates)

def evaluate(individual):
    coordinates = [(409.5,93), (63,57), (198,207), (309,127.5), (3,139.5), (295.5,192), (232.5,75), (90,135)]
    return fitness(individual, coordinates),

def deap():
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    IND_SIZE=8

    toolbox = base.Toolbox()
    toolbox.register("indices", random.sample, range(IND_SIZE), IND_SIZE) # Gen, in this case, a number which represents a city.
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices) # Define a route of cities. A chromosome.

    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluate)

    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    POP_SIZE = 50

    pop = toolbox.population(n=POP_SIZE)

    CXPB, MUTPB, NGEN = 0.5, 0.2, 40

    # Evaluate the entire population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(NGEN):
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = map(toolbox.clone, offspring)

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # The population is entirely replaced by the offspring
        pop[:] = offspring

    return pop

def simulated_annealing():
    pass

if __name__ == "__main__":
    andalusia = {
                    0: (409.5,93), # Almería
                    1: (63,57), # Cádiz
                    2: (198,207), # Córdoba
                    3: (309,127.5), # Granada
                    4: (3,139.5), # Huelva
                    5: (295.5,192), # Jaén
                    6: (232.5,75), # Málaga
                    7: (90,135) # Sevilla
                }

    # TODO: Implement simulated_annealing function.
    # TODO: Implement genetic algorithm usgin DEAP library.
    #
    print(deap())

"""def main():
    pop = toolbox.population(n=50)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40

    # Evaluate the entire population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(NGEN):
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = map(toolbox.clone, offspring)

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # The population is entirely replaced by the offspring
        pop[:] = offspring

    return pop"""
