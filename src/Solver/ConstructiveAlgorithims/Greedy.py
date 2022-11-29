import numpy

def InitialSolutionGreedy(load):

    (vehicles, clients, vehicle_capacity, distances, client_demand) = load

    distances_copy = distances.copy()
    client_supply = client_demand.copy()
    solution = [[0, 0] for i in range(vehicles)]
    vehicles_demand = [0 for i in range(vehicles)]
    
    while (client_supply.count(0) != len(client_supply)):
        for vehicle_k in range(vehicles):
            current_client = solution[vehicle_k][-2]
            valid_clients = []

            for client_i in range(clients):
                distance_client_i_current = distances_copy[client_i][current_client]
                if not numpy.isnan(distance_client_i_current):
                    function_val = (distance_client_i_current * (1/(client_demand[client_i]+0.001)))
                    if client_i not in solution and client_supply[client_i] != 0 and vehicle_capacity - (vehicles_demand[vehicle_k] + client_demand[client_i])  >= 0:
                        valid_clients.append([function_val, client_i])
            
            current_client = min(valid_clients)[1] if len(valid_clients) > 0 else None
            if(current_client != None):
                solution[vehicle_k].insert(len(solution[vehicle_k])-1, current_client)
                vehicles_demand[vehicle_k] += client_demand[current_client]
                client_supply[current_client] = 0

    return solution