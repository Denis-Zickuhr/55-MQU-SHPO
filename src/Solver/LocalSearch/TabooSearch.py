import random
import sys
import time
import json
sys.path.extend(json.load(open('.vscode/settings.json'))['python.analysis.extraPaths'])
from loader import _LOAD
from solutioncalculation import *
from operators import *

def localSearch(ins, ts, tx, initial_construction):
        
    ins = ins
    solution  = initial_construction
    (vehicles, clients, vehicle_capacity, distances, client_demand) = _LOAD(ins)

    def search(solution, best_solution_value, distances, local_optima, optima_index, looseness):

        global fit
        global fit_value
        global optima_max

        best_solution = solution
        not_improved = True

        weigth = calcweigth(solution, client_demand, vehicle_capacity)
        
        solutions = []
        solutions.extend(relocate(solution, client_demand, weigth))
        solutions.extend(swap(solution, client_demand, weigth))
        solutions.extend(route_robbing(best_solution, client_demand, weigth))
        solutions.extend(shuffle(solution))
        
        for solution_n in solutions:

            new_solution_value = calcdistance_nominal(solution_n, distances)

            if best_solution_value > new_solution_value and solution_n not in local_optima:
                best_solution = solution_n
                best_solution_value = new_solution_value 
                not_improved = False
                looseness = 0

        if fit_value > best_solution_value:
            fit_value = best_solution_value
            fit = best_solution

        if not_improved:
            if looseness == 0:
                local_optima[optima_index] = best_solution
                optima_index = optima_index + 1 if optima_index + 1 < optima_max else 0
            looseness += 1

        return best_solution, best_solution_value, local_optima, optima_index, looseness

    def init():

        global fit
        global fit_value
        global optima_max

        fit = solution
        fit_value = calcdistance_nominal(solution, distances)
        optima_max = int((clients/vehicles))

        def startSearch():
            best_solution = solution
            best_solution_value = fit_value
            local_optima = [[] for i in range(optima_max)]
            optima_index = 0
            looseness = 0
            t_end = time.time() + (ts * tx)
            while time.time() < t_end:
                best_solution, best_solution_value, local_optima, optima_index, looseness = search(best_solution, (best_solution_value+looseness), distances, local_optima, optima_index, looseness)
            return best_solution, best_solution_value
        return startSearch()

    return init()