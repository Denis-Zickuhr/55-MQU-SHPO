import random
import sys

def solve(ALPHA, load):

    (vehicles, clients, vehicle_capacity, distances, client_demand) = load
    distances_copy = distances.copy()
    client_supply = client_demand.copy() 
    solution = [[0, 0] for i in range(vehicles)]
    vehicles_demand = [0 for i in range(vehicles)]

    while (client_supply.count(0) != len(client_supply)):
        if client_supply.count(0) != 1 and len(valid_clients) == 0:
            return solve(ALPHA, load)

        for vehicle_k in range(vehicles):
            current_client = solution[vehicle_k][-2]
            valid_clients = []
            for client_i in range(clients):
                distance_client_i_current = distances_copy[client_i][current_client]
                if not distance_client_i_current is None:
                    function_val = -sys.maxsize - client_supply[client_i]
                    if client_i not in solution and client_supply[client_i] != 0 and vehicle_capacity - (vehicles_demand[vehicle_k] + client_demand[client_i])  >= 0:
                        valid_clients.append([function_val, client_i])

            valid_clients.sort()
            r = random.randint(-1, int((len(valid_clients)-1)*ALPHA))
            current_client = valid_clients[r][1] if len(valid_clients) > 0 else None
            if(current_client != None):
                solution[vehicle_k].insert(len(solution[vehicle_k])-1, current_client)
                vehicles_demand[vehicle_k] += client_demand[current_client]
                client_supply[current_client] = 0
                
    return solution
