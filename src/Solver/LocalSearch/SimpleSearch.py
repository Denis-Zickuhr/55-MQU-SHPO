import random
import sys
import time
import json
sys.path.extend(json.load(open('.vscode/settings.json'))['python.analysis.extraPaths'])
from loader import _LOAD
from solutioncalculation import *
from operators import *

def localSearch(ins, initial_construction):
        
    ins = ins
    solution  = initial_construction
    (vehicles, clients, vehicle_capacity, distances, client_demand) = _LOAD(ins)

    def search(solution, best_solution_value, distances):

        global fit
        global fit_value

        best_solution = solution
        not_improved = True
        
        solutions = []
        solutions.extend(swap(solution, client_demand, calcweigth(solution, client_demand, vehicle_capacity)))
        solutions.extend(route_robbing(best_solution, client_demand, calcweigth(best_solution, client_demand, vehicle_capacity)))
        solutions.extend(relocate(best_solution, client_demand, calcweigth(best_solution, client_demand, vehicle_capacity)))
        solutions.extend(shuffle(solution))
        
        solution_pool = []

        for solution_n in solutions:

            new_solution_value = calcdistance_nominal(solution_n, distances)

            if best_solution_value > new_solution_value:
                solution_pool.append([new_solution_value, solution_n])
                not_improved = False

        pool_size = len(solution_pool)
        solution_pool.sort()
        if pool_size > 0:
            rand = random.randint(0, pool_size-1)
            rand_elite = rand - random.randint(0, rand)
            best_solution = solution_pool[rand_elite][1]
            best_solution_value = calcdistance_nominal(best_solution, distances)

        if fit_value > best_solution_value:
            fit_value = best_solution_value
            fit = best_solution

        if not_improved:
            return best_solution, best_solution_value, not_improved

        return best_solution, best_solution_value, not_improved

    def init():

        global fit
        global fit_value

        fit = solution
        fit_value = calcdistance_nominal(solution, distances)

        def startSearch():
            best_solution = solution
            best_solution_value = fit_value
            while True:
                best_solution, best_solution_value, not_improved = search(best_solution, best_solution_value, distances)
                if not_improved:
                    break
            return best_solution, best_solution_value
        return startSearch()

    return init()
    