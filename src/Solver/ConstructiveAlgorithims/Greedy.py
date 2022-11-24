import random
import numpy
import sys
sys.path.append('./src/Utils')
sys.path.append('./src/Solver/ValueCalculation')
from loader import _LOAD
from calc import calc

(k, d, c, P, D, Depot) = _LOAD('./instances/A/A-n80-k10.vrp')

def InitialSolutionGreedy():

    Pw = P.copy()
    Dc = D.copy()
    START_POINT = Dc.index(min(Dc))
    
    S_Value = 0
    path = []

    # K_Elite Strategy
    ELITE = [0 for i in range(k*2)]
    ELITE_COST = []
    ELITE_START_POINT = []
    ELITE_END_POINT = []

    for y in range(k*2):
        F = sys.maxsize
        for i in range(d):
                mv = Pw[i][START_POINT] 
                if mv < F and i not in ELITE and Dc[i] != 0:
                    F = mv
                    COST = D[START_POINT]
                    MINIMAL_COST = mv
                    index = i
            
        ELITE[y] = index

    for z in range(k):
        
        start = ELITE[0]
        ELITE.remove(start)
        Dc[start] = 0

        F = sys.maxsize
        for i in range(d):
                mv = Pw[i][start] 
                if mv < F and Dc[i] != 0 and i in ELITE:
                    F = mv
                    COST = D[START_POINT]
                    MINIMAL_COST = mv
                    index = i
            
        end = index
        ELITE.remove(end)
        Dc[end] = 0

        ELITE_COST.append([D[start], D[end]])
        ELITE_START_POINT.append(start)
        ELITE_END_POINT.append(end)
        path.append([0, start, end, 0])

    TOTAL_COST = [sum(ELITE_COST[i]) for i in range(k)]
    while (Dc.count(0) != len(Dc)):

        TOTAL_DISTANCE = 0
        COST = 0
        MINIMAL_COST = 0
        
        # Aplica F para selecionar o "melhor caminho" da ida até a volta
        for K in range(k):
            xy = ELITE_START_POINT[K]
            index = None
            F = sys.maxsize
            for i in range(d):
                mv = Pw[i][xy] 
                f = (mv + Pw[i][ELITE_END_POINT[K]])
                if f < F and i not in path and Dc[i] != 0 and c  - (TOTAL_COST[K] + D[i])  >= 0:
                    F = f
                    COST = D[i]
                    MINIMAL_COST = mv
                    index = i
            
            xy = index
            if(xy != None):
                path[K].insert((len(path[K])-2), xy)
                TOTAL_DISTANCE += MINIMAL_COST
                TOTAL_COST[K] += COST
                Dc[xy] = 0

                
    S = path
    S_Value = calc(Pw, D, S, c)

    print("Valor da Solucao", S_Value)
    print("Solucao: ")
    print(S)

    return S_Value, S

InitialSolutionGreedy()