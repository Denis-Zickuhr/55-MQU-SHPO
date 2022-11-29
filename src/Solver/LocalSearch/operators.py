import copy

def relocate(solution, client_demand, calc_function):
    vehicle_loads, vehicle_capacity = calc_function
    solutions = []
    vehicles = len(solution)
    for vehicles_origin in range(vehicles):
        for clients_origin in range(len(solution[vehicles_origin])):
            client_a = solution[vehicles_origin][clients_origin]
            if client_a != 0: 
                vehicle_capacity_a = client_demand[client_a]
                for vehicles_destiny in range(vehicles-1):
                    if vehicle_capacity - (vehicle_loads[vehicles_destiny+1] + vehicle_capacity_a) >= 0:
                        for position in range(len(solution[vehicles_destiny+1])-2):
                            new_solution = copy.deepcopy(solution)
                            new_solution[vehicles_origin].remove(client_a)
                            new_solution[vehicles_destiny+1].insert(position+1, client_a)
                            solutions.append(copy.deepcopy(new_solution))
                            new_solution.clear()

    return solutions

def swap(solution, client_demand, calc_function):
    vehicle_loads, vehicle_capacity = calc_function
    solutions = []
    vehicles = len(solution)
    for vehicles_origin in range(vehicles):
        for clients_origin in range(len(solution[vehicles_origin])):
            client_a = solution[vehicles_origin][clients_origin]
            if client_a != 0: 
                vehicle_capacity_a = client_demand[client_a]
                for vehicles_destiny in range(vehicles-1):
                    for clients_destiny in range(len(solution[vehicles_destiny+1])-2):
                        client_b = solution[vehicles_destiny+1][clients_destiny+1]
                        if client_b != 0 and client_b != client_a: 
                            vehicle_capacity_b = client_demand[client_b]
                            new_solution = copy.deepcopy(solution)
                            destiny_truck_cargo = vehicle_capacity - (vehicle_loads[vehicles_destiny+1] + vehicle_capacity_a)
                            origin_truck_cargo = vehicle_capacity - (vehicle_loads[vehicles_origin] + vehicle_capacity_b)
                            if destiny_truck_cargo >= 0 and origin_truck_cargo >= 0:
                                new_solution[vehicles_origin][clients_origin] = client_b
                                new_solution[vehicles_destiny+1][clients_destiny+1]= client_a
                                solutions.append(copy.deepcopy(new_solution))
                                new_solution.clear()

    return solutions
