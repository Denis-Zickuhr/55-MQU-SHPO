import cmath
import random
import sys
import time
import json
sys.path.extend(json.load(open('.vscode/settings.json'))['python.analysis.extraPaths'])
from loader import _LOAD
from solutioncalculation import *
from operators import *

def localSearch(ins, initial_construction, T, limit_seconds):
        
    ins = ins
    solution  = initial_construction
    (vehicles, clients, vehicle_capacity, distances, client_demand) = _LOAD(ins)

    def search(solution, best_solution_value, distances, inner_temperature):

        global fit
        global fit_value

        best_solution = solution

        weigth = calcweigth(solution, client_demand, vehicle_capacity)
        
        solutions = []
        solutions.extend(swap(solution, client_demand, weigth))
        solutions.extend(route_robbing(best_solution, client_demand, weigth))
        solutions.extend(relocate(best_solution, client_demand, weigth))
        solutions.extend(shuffle(solution))

        for solution_n in solutions:

            new_solution_value = calcdistance_nominal(solution_n, distances)

            delta = new_solution_value - best_solution_value

            if delta < 0:
                best_solution = solution_n
                best_solution_value = new_solution_value
                if fit_value > best_solution_value:
                    fit_value = best_solution_value
                    fit = best_solution
                break
            else:
                r = random.uniform(0.000, 1.000)
                E = cmath.e**-delta/inner_temperature
                if r < E:
                    best_solution = solution_n
                    break
        
        inner_temperature -= 0.1

        return best_solution, best_solution_value, inner_temperature

    def init():

        global fit
        global fit_value

        fit = solution
        fit_value = calcdistance_nominal(solution, distances)

        def startSearch():
            best_solution = solution
            best_solution_value = fit_value
            t_end = time.time() + limit_seconds
            inner_temperature = T
            while inner_temperature > 0 and time.time() < t_end:
                best_solution, best_solution_value, inner_temperature = search(best_solution, best_solution_value, distances, inner_temperature)
            return best_solution, best_solution_value
        return startSearch()

    return init()
    