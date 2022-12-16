from cmath import sqrt



def _LOAD(path):
    file = open(path, "r")
    file = file.readlines()

    vehicles = 0
    clients = 0
    vehicle_capacity = 0
    optimal_solution_value = 0

    for line in file:

        if line.startswith("NAME :"):
            data = line.split("-")
            vehicles = int(data[len(data)-1].replace("k", ""))
            clients = int(data[len(data)-2].replace("n", ""))

        if line.startswith("COMM"):
            data = line.replace(")", "").replace("\n", "").split(" ")
            data.reverse()
            optimal_solution_value = data[0]

        if line.startswith("CAPACITY :"):
            vehicle_capacity = int(line.replace("CAPACITY :", "").replace("\n", ""))
        
    Pa = [0 for i in range(clients)]     
    clients_demands = [0 for i in range(clients)] 
    Depot = []

    avail = False
    for line in file:

        if line.startswith("DEMAND_SECTION"):
            avail = False

        if avail:
            data = line.replace("\n", "").split(" ")
            Pa[int(data[1])-1] = [int(data[2]), int(data[3])]

        if line.startswith("NODE_COORD_SECTION"):
            avail = True

    for line in file:

        if line.startswith("DEPOT_SECTION"):
            avail = False

        if avail:
            data = line.replace("\n", "").split(" ")
            clients_demands[int(data[0])-1] = int(data[1])

        if line.startswith("DEMAND_SECTION"):
            avail = True

            
    for line in file:

        if line.startswith("EOF"):
            avail = False

        if avail:
            data = line.replace("\n", "").replace(" ", "")
            Depot.append(int(data))

        if line.startswith("DEPOT_SECTION"):
            avail = True

    distances = [[None for i in range(clients)] for i in range(clients)]
    for i in range(clients):
        p1 = Pa[i]
        for j in range(clients):
            p2 = Pa[j]
            Delta = (((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**(1/2)
            if Delta == 0.0:
                distances[i][j] = None
            else:
                distances[i][j] = Delta
        
    return vehicles, clients, vehicle_capacity, distances, clients_demands 