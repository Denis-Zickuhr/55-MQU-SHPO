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
    TOTAL_COST = [0 for i in range(k)]
    Alpha = []

    while (Dc.count(0) != len(Dc)):
        if Dc.count(0) != 1 and len(Alpha) == 0:
            return AlphaGreedy(ALPHA, ins)
                
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

            Alpha.sort()
            r = random.randint(-1, int((len(Alpha)-1)*ALPHA))
            xy = Alpha[r][1] if len(Alpha) > 0 else None
            if(xy != None):
                path[K].insert(len(path[K])-1, xy)
                TOTAL_COST[K] += D[xy]
                Dc[xy] = 0
                
    S = path
    S_Value, STATUS, pairs, Points = calc(Pw, D, S, c, Dc)

    return S_Value, S, opt, pairs, STATUS, Points

for i in range(99):
    SUM = 0
    for j in range(10):
        a = eval(f"0.0{i+1}") if i+1 < 10 else eval(f"0.{i+1}")
        (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n80-k10.vrp')
        SUM += S_Value
    print(f"{a}: {SUM/10}")
    
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n63-k9.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n65-k9.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n46-k7.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n55-k9.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n48-k7.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n37-k5.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n37-k6.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n80-k10.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n39-k5.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))
# (S_Value, S, opt, pairs, STATUS, Points)  = AlphaGreedy( a , './instances/A/A-n69-k9.vrp')
# print((f"Optimal: {opt}", S_Value, STATUS))