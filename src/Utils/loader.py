import numpy

def _LOAD(path):
    file = open(path, "r")
    file = file.readlines()

    k = 0
    d = 0
    c = 0
    opt = 0


    for line in file:

        if line.startswith("NAME :"):
            data = line.split("-")
            k = int(data[len(data)-1].replace("k", ""))
            d = int(data[len(data)-2].replace("n", ""))

        if line.startswith("COMM"):
            data = line.replace(")", "").replace("\n", "").split(" ")
            data.reverse()
            opt = data[0]

        if line.startswith("CAPACITY :"):
            c = int(line.replace("CAPACITY :", "").replace("\n", ""))
        
    Pa = [0 for i in range(d)]     
    D = [0 for i in range(d)] 
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
            D[int(data[0])-1] = int(data[1])

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

    P = numpy.array([[None for i in range(d)] for i in range(d)], dtype=numpy.float64)
    FarthestPoint = 0
    for i in range(d):
        p1 = Pa[i]
        for j in range(d):
            p2 = Pa[j]
            # √((x2 – x1)² + (y2 – y1)²)
            Delta = numpy.sqrt(((numpy.power((p2[0] - p1[0]), 2)) + (numpy.power((p2[1] - p1[1]), 2))))
            if Delta == 0.0:
                P[i][j] = None
            else:
                P[i][j] = Delta
            if Delta > FarthestPoint:
                FarthestPoint = Delta
            
    return k, d, c, P, D 
    # ,Depot, opt, FarthestPoint