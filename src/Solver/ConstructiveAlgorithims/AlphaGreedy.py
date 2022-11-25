import random
import numpy
import sys
sys.path.append('./src/Utils')
sys.path.append('./src/Solver/ValueCalculation')
from loader import _LOAD
from calc import calc

def AlphaGreedy(ALPHA, ins):

    (k, d, c, P, D, Depot, opt, FarthestPoint) = _LOAD(ins)

    Pw = P.copy()
    Dc = D.copy()
    
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

                mv = Pw[i][xy]/int(FarthestPoint)
                if not numpy.isnan(mv):
                    Q = 1 if random.uniform(((10/FarthestPoint)/mv), (1 + ((10/FarthestPoint)/mv))) >= ALPHA else sys.maxsize
                    f = (mv * Q)

                    if f < F and i not in path and Dc[i] != 0 and c - (TOTAL_COST + D[i])  >= 0:
                        F = f
                        COST = D[i]
                        MINIMAL_COST = mv
                        index = i
            
            xy = index
            if(xy != None):
                path[K].insert(len(path[K])-1, xy)
                TOTAL_DISTANCE += MINIMAL_COST
                TOTAL_COST += COST
                Dc[xy] = 0
                
    S = path
    S_Value, STATUS, pairs = calc(Pw, Dc, S, c, Dc)

    return S_Value, S, opt, pairs, STATUS

(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n80-k10.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n63-k9.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n65-k9.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n46-k7.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n55-k9.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n48-k7.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n37-k5.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n37-k6.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n80-k10.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n39-k5.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))
(S_Value, S, opt, pairs, STATUS) = AlphaGreedy( 0.5, './instances/A/A-n69-k9.vrp')
print((f"Optimal: {opt}", S_Value, STATUS))