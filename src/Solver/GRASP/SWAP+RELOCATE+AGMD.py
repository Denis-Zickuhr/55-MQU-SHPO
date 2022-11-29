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
from operators import relocate
from operators import swap

ins = sys.argv[1]
solution  = solve(0.2, _LOAD(ins))
(vehicles, clients, vehicle_capacity, distances, client_demand) = _LOAD(ins)

def GRASP(solution, distances, visited_solutions, relax_value):

    global fit
    global fit_solution

    best_solution_value = calcdistance(solution, distances) + relax_value
    not_improved = True
    best_solution = solution
    solutions = relocate(solution, client_demand, calcweigth(solution, client_demand, vehicle_capacity))
    solutions.extend(swap(solution, client_demand, calcweigth(solution, client_demand, vehicle_capacity)))

    for solution_n in solutions:
        new_soltion_value = calcdistance(solution_n, distances)

        if best_solution_value > new_soltion_value and solution_n not in visited_solutions:
            best_solution_value = new_soltion_value 
            best_solution = solution_n
            
            if fit > best_solution_value:
                not_improved = False

    if fit > best_solution_value:
        fit = best_solution_value
        fit_solution = best_solution

    if not_improved:
        relax_value += 1
    else:
        relax_value = 0

    visited_solutions.append(best_solution)
    return best_solution, best_solution_value, visited_solutions, relax_value

best_solution = solution
best_solution_value = calcdistance(solution, distances)
fit = best_solution_value
visited_solutions = [solution]
relax_value = 0

t_end = time.time() + eval(sys.argv[2]) * eval(sys.argv[3])
while time.time() < t_end:
    best_solution, best_solution_value, visited_solutions, relax_value = GRASP(best_solution, distances, visited_solutions, relax_value)

print(fit, fit_solution)