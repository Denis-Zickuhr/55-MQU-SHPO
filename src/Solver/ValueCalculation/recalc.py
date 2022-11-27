import numpy
def recalcf(Solution, Points):

    pairs = [[] for i in range(len(Solution))]

    for i in range(len(Solution)):
        for j in range(len(Solution[i])-1):
            pairs[i].append([Solution[i][j], Solution[i][j+1]])

    S_Value = 0

    for pair in pairs:
        for x in pair:
            if x != 0:
                n = round(Points[x[0]][x[1]], 0)
                S_Value += n if not numpy.isnan(n) else 0
        
    return round(S_Value, 0)

import numpy
def recalc(Solution, Points):

    S_Value = 0

    for i in range(len(Solution)):
        for j in range(len(Solution[i])-1):
                n = round(Points[Solution[i][j]][Solution[i][j+1]], 0)
                S_Value += n if not numpy.isnan(n) else 0
        
    return round(S_Value, 0)