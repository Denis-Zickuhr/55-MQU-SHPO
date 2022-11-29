import random
import sys
import time
sys.path.append('./src/Solver/ValueCalculation')
sys.path.append("./src/Solver/ConstructiveAlgorithims")
sys.path.append('./src/Utils')
sys.path.append('./src/Solver/LocalSearch')
from loader import _LOAD
from solutioncalculation import calcdistance
from solutioncalculation import calcweigth
from AlphaGreedyMaxD import solve
from operators import swap

solution  = solve(0.2, _LOAD('./instances/A/A-n37-k5.vrp'))
(vehicles, clients, vehicle_capacity, distances, client_demand) = _LOAD('./instances/A/A-n37-k5.vrp')

def GRASP(solution, distances, visited_solutions):

    best_solution_value = calcdistance(solution, distances)
    not_improved = True
    best_solution = solution
    solutions = swap(solution, client_demand, calcweigth(solution, client_demand, vehicle_capacity))

    for solution_n in solutions:
        new_soltion_value = calcdistance(solution_n, distances)

        if best_solution_value > new_soltion_value and solution_n not in visited_solutions:
            best_solution_value = new_soltion_value 
            best_solution = solution_n
            not_improved = False

    global fit 
    global fit_solution
    if fit > best_solution_value:
        fit = best_solution_value
        fit_solution = best_solution

    visited_solutions.append(best_solution)

    if not_improved:
        while(best_solution in visited_solutions):
            best_solution = solutions[random.randint(0, len(solutions)-1)]
        best_solution_value = calcdistance(solution_n, distances)

    return best_solution, best_solution_value, visited_solutions


fit = sys.maxsize
best_solution = solution
best_solution_value = calcdistance(solution, distances)
visited_solutions = []

t_end = time.time() + 60 * 4
while time.time() < t_end:
    best_solution, best_solution_value, visited_solutions = GRASP(best_solution, distances, visited_solutions)

print(fit, fit_solution)