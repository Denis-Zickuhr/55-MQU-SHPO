import random
import numpy
import sys
sys.path.append('./src/Utils')
sys.path.append('./src/Solver/ValueCalculation')
from loader import _LOAD
from calc import calc

def InitialSolutionGreedy(ins):

    (k, d, c, P, D, Depot, opt) = _LOAD(ins)

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
                pv = Pw[i][START_POINT]
                f = (mv + pv) / 2

                if f < F and i not in path and Dc[i] != 0 and c - (TOTAL_COST + D[i])  >= 0:
                    F = f
                    COST = D[i]
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
    S_Value = calc(Pw, Dc, S, c, Dc)

    return S_Value, S, opt

(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n80-k10.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n63-k9.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n65-k9.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n46-k7.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n55-k9.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n48-k7.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n37-k5.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n37-k6.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n80-k10.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n39-k5.vrp')
print(("Optimal:", opt, S_Value))
(S_Value, S, opt) = InitialSolutionGreedy('./instances/A/A-n69-k9.vrp')
print(("Optimal:", opt, S_Value))