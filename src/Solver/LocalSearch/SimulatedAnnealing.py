import random
import sys
import time
import json
sys.path.extend(json.load(open('.vscode/settings.json'))['python.analysis.extraPaths'])
from loader import _LOAD
from solutioncalculation import *
from operators import *

def localSearch(ins, initial_construction, T):
        
    ins = ins
    solution  = initial_construction
    (vehicles, clients, vehicle_capacity, distances, client_demand) = _LOAD(ins)

    def search(solution, best_solution_value, distances, T):

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

            if best_solution_value > new_solution_value:
                best_solution = solution_n
                best_solution_value = new_solution_value
                break
            else:
                r = random.uniform(0, 1)
                if r < ((best_solution_value - new_solution_value)/T):
                    best_solution = solution_n
                    best_solution_value = new_solution_value
                    break
        
        T -= (fit_value/best_solution_value) * 0.5

        if fit_value > best_solution_value:
            fit_value = best_solution_value
            fit = best_solution


        return best_solution, best_solution_value, T

    def init(T):

        global fit
        global fit_value

        fit = solution
        fit_value = calcdistance_nominal(solution, distances)

        def startSearch(T):
            best_solution = solution
            best_solution_value = fit_value
            while T > 0:
                best_solution, best_solution_value, T = search(best_solution, best_solution_value, distances, T)
            return best_solution, best_solution_value
        return startSearch(T)

    return init(T)
    