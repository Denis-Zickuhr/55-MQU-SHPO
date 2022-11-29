import random
import numpy

def AlphaGreedy(ALPHA, load):

    (vehicles, clients, vehicle_capacity, distances, client_demand) = load
    distances_copy = distances.copy()
    client_supply = client_demand.copy() 
    solution = [[0, 0] for i in range(vehicles)]
    vehicles_demand = [0 for i in range(vehicles)]

    while (client_supply.count(0) != len(client_supply)):
        if client_supply.count(0) != 1 and len(valid_clients) == 0:
            return AlphaGreedy(ALPHA, load)

        for K in range(vehicles):
            current_client = solution[K][-2]
            valid_clients = []
            for i in range(clients):
                distance_client_i_current = distances_copy[i][current_client]
                if not numpy.isnan(distance_client_i_current):
                    function_val = (distance_client_i_current * (1/(client_demand[i]+0.001)))
                    if i not in solution and client_supply[i] != 0 and vehicle_capacity - (vehicles_demand[K] + client_demand[i])  >= 0:
                        valid_clients.append([function_val, i])

            valid_clients.sort()
            r = random.randint(-1, int((len(valid_clients)-1)*ALPHA))
            current_client = valid_clients[r][1] if len(valid_clients) > 0 else None
            if(current_client != None):
                solution[K].insert(len(solution[K])-1, current_client)
                vehicles_demand[K] += client_demand[current_client]
                client_supply[current_client] = 0
                
    return solution