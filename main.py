import random
import math

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
    return sum(euclidean_distance_2D(chromosome[i], chromosome[i+1], coordinates) for i in range(len(chromosome)-1)) + euclidean_distance_2D(chromosome[-1], chromosome[0], coordinates)

if __name__ == "__main__":
    andalusia = {
                    "Almeria": (409.5,93),
                    "Cadiz": (63,57),
                    "Cordoba": (198,207),
                    "Granada": (309,127.5),
                    "Huelva": (3,139.5),
                    "Jaen": (295.5,192),
                    "Malaga": (232.5,75),
                    "Seville": (90,135)
                }

    # TODO: Implement simulated_annealing function.
    # TODO: Implement genetic algorithm usgin DEAP library.
