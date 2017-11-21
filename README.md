# DEAP_Python_PoC

[![Build Status](https://travis-ci.org/serrodcal/DEAP_Python_PoC.svg?branch=master)](https://travis-ci.org/serrodcal/DEAP_Python_PoC)
[![Coverage Status](https://coveralls.io/repos/github/serrodcal/DEAP_Python_PoC/badge.svg?branch=master)](https://coveralls.io/github/serrodcal/DEAP_Python_PoC?branch=master)
[![Code Health](https://landscape.io/github/serrodcal/DEAP_Python_PoC/master/landscape.svg?style=flat)](https://landscape.io/github/serrodcal/DEAP_Python_PoC/master)

This project is a proof of concept about [DEAP](http://deap.readthedocs.io/en/master/overview.html) in Python
developed by Fernando Jiménez and Sergio Rodríguez.

# Goals

* Learn [DEAP](http://deap.readthedocs.io/en/master/overview.html) library.
* Learn Artificial Intelligence techniques.
* Learn genetic algorithm.
* And the most important, *have fun*.

# The problem

A company needs to solve the [Travelling salesman problem or TSP](https://en.wikipedia.org/wiki/Travelling_salesman_problem).
It needs to know the shortest route to deliver orders daily. This problem is NP-hard, so the company wants us to solve this problem
using some artificial intelligence technique.

Its headquarter is located in [Seville](https://en.wikipedia.org/wiki/Seville), and they deliver orders
for [Andalusia](https://en.wikipedia.org/wiki/Andalusia). Simplify, is able to go from any point to any other point using
the Euclidean distance, and

Note, that this problem is focused as [local search or optimization problem](https://en.wikipedia.org/wiki/Local_search_(optimization)).
And, it is not necessary to start deliveries from the company's headquarter.

First, a dictionary with the provinces and their coordinates is provided:

```
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
```

And, `euclidean_distance_2D`, `raffle` and `fitness` functions are provided:

```
import math
import random

def raffle(probability):
    return (random.random() < probability)

def euclidean_distance_2D(city_1, city_2, coordinates):
    city_1_coord = coordinates[city_1]
    city_2_coord = coordinates[city_2]
    return math.hypot(city_1_coord[0]-city_2_coord[0], city_1_coord[1]-city_2_coord[1])

def fitness(chromosome, coordinates):
    return sum(euclidean_distance_2D(chromosome[i], chromosome[i+1], coordinates) for i in range(len(chromosome)-1)) + euclidean_distance_2D(chromosome[-1], chromosome[0], coordinates)
```

It is important to specify what the genes and the chromosome will be.

Please, use any CI technology with coverage and code quality, and complete more section in `README.md` like
solution section and how to execute the solution.

# The solution

Two ways of solving this problem are proposed:

1. Using DEAP to implement a classic [Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm).
2. Using proprietary implementation of the [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing) algorithm.

# How to execute it?

## Technologies

_In progress_.

## Prerequisites

_In progress_.

## Run by console

_In progress_.

## Do you prefer docker?

_In progress_.
