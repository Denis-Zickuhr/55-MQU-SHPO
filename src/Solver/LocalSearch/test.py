import itertools
import sys
import numpy
import time
sys.path.append('./src/Solver/ValueCalculation')
sys.path.append("./src/Solver/ConstructiveAlgorithims")
from recalc import recalc
from Greedy import InitialSolutionGreedy

def improveRouteOrder(Solution, Points):
    newS = []
    for k in Solution.copy():
        mv = sys.maxsize
        length = len(k)-3
        k.remove(0)
        k.remove(0)
        permutations = list(itertools.permutations(k))
        for subk in permutations:
            permutations.pop()
            rec = Points[0][subk[0]] + Points[0][subk[len(subk)-1]] 
            for j in range(length):
                n = round(Points[subk[j]][subk[j+1]], 0)
                rec += n
            if rec < mv:
                mv = rec
                osubk = list((0,) + subk + (0,))
        newS.append(osubk)
        
    return newS

def improveRoute(Solution, Points, seconds, sx):
    t_end = time.time() + seconds * sx
    while time.time() < t_end:
        pass

    return Solution

(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n37-k5.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n63-k9.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n65-k9.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n46-k7.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n55-k9.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n48-k7.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n37-k5.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n37-k6.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n80-k10.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n39-k5.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points)  = InitialSolutionGreedy('./instances/A/A-n69-k9.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))
(S_Value, S, opt, pairs, STATUS, Points) = InitialSolutionGreedy('./instances/A/A-n80-k10.vrp')
print("W: ",S_Value) # ¨§
print("B: ", recalc(improveRoute((improveRouteOrder(S, Points)), Points, 1, 1), Points))