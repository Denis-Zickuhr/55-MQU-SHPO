import random
import numpy
import sys
sys.path.append('./src/Utils')
sys.path.append('./src/Solver/ValueCalculation')
from loader import _LOAD
from calc import calc

(k, d, c, P, D, Depot) = _LOAD('./instances/A/A-n33-k5.vrp')

def InitialSolutionGreedy():

    Pw = P.copy()
    Dc = D.copy()
    START_POINT = Dc.index(min(Dc))
    
    S_Value = 0
    path = [[0, 0] for i in range(k)]

    while (Dc.count(0) != len(Dc)):

        TOTAL_DISTANCE = 0
        TOTAL_COST = 0
        COST = 0
        MINIMAL_COST = 0
        
        # Aplica F para selecionar o "melhor caminho" da ida até a volta
        for K in range(k):

            xy = path[K][len(path[K])-2]

            index = None
            
            F = sys.maxsize

            for i in range(d):

                mv = Pw[i][xy] 
                f = mv/(mv + Pw[i][START_POINT])

                if f < F and i not in path and Dc[i] != 0 and c - (TOTAL_COST + D[xy])  >= 0:
                    F = f
                    COST = D[xy]
                    MINIMAL_COST = mv
                    index = i
            
            xy = index
            if(xy != None):
                last = path[K].pop()
                path[K].append(xy)
                path[K].append(last)
                TOTAL_DISTANCE += MINIMAL_COST
                TOTAL_COST += COST
                Dc[xy] = 0
                
    S = path
    S_Value = calc(Pw, Dc, S, c)

    print("Valor da Solucao", S_Value)

    return S_Value, S

InitialSolutionGreedy()