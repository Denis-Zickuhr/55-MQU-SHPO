import random
import numpy
import sys
sys.path.append('./src/Utils')
sys.path.append('./src/Solver/ValueCalculation')
from loader import _LOAD
from calc import calc

def InitialSolutionGreedy(ins):

    (k, d, c, P, D, Depot, opt, FarthestPoint) = _LOAD(ins)

    Pw = P.copy()
    Dc = D.copy()
    
    S_Value = 0
    path = [[0, 0] for i in range(k)]
    TOTAL_COST = [0 for i in range(k)]
    Alpha = []
    
    while (Dc.count(0) != len(Dc)):

        # Aplica F para selecionar o "melhor caminho" da ida até a volta
        for K in range(k):

            xy = path[K][len(path[K])-2]
            Alpha.clear()

            for i in range(d):

                mv = Pw[i][xy]
                if not numpy.isnan(mv):
                    f = ((mv) * (1/(D[i]+0.001)))

                    if i not in path and Dc[i] != 0 and c - (TOTAL_COST[K] + D[i])  >= 0:
                        Alpha.append([f, i])
            
            xy = min(Alpha)[1] if len(Alpha) > 0 else None
            if(xy != None):
                path[K].insert(len(path[K])-1, xy)
                TOTAL_COST[K] += D[xy]
                Dc[xy] = 0
                
    S = path
    S_Value, STAUTS , pairs, Points = calc(Pw, D, S, c, Dc)

    return S_Value, S, opt, pairs, STAUTS, Points
