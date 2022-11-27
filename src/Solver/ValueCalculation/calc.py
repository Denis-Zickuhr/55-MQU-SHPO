import numpy
def calc(Points, Demands, Solution, Capacity, MetDemand):

    pairs = [[] for i in range(len(Solution))]

    STATUS = "VALID"

    if MetDemand.count(0) != len(MetDemand):
        STATUS = "INVALID - unmet demand"

    for i in range(len(Solution)):
        c = 0
        for j in range(len(Solution[i])-1):
            pairs[i].append([Solution[i][j], Solution[i][j+1]])
            c += Demands[Solution[i][j]]
        if Capacity - c < 0 and len(STATUS) < 7:
            STATUS = "INVALID"
        if Capacity - c < 0:
            STATUS += f", Vehicle {i}: {c}"

    S_Value = 0

    for pair in pairs:
        for x in pair:
            if x != 0:
                n = round(Points[x[0]][x[1]], 0)
                S_Value += n if not numpy.isnan(n) else 0
        
    return round(S_Value, 0), STATUS, pairs, Points