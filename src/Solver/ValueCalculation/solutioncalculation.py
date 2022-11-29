import numpy
def calcdistance(Solution, Points):

    S_Value = 0

    for i in range(len(Solution)):
        for j in range(len(Solution[i])-1):
                n = round(Points[Solution[i][j]][Solution[i][j+1]], 0)
                S_Value += n if not numpy.isnan(n) else 0
        
    return round(S_Value, 0)

def calcweigth(Solution, Demands, C):

    size = len(Solution)
    loads = [0 for i in range(size)]
    Valid = True

    for i in range(size):
        c = 0
        for j in range(len(Solution[i])-1):
            c += Demands[Solution[i][j]]
        loads[i] = c
        if C - c < 0:
            Valid = False
    
    return loads, C