import sys
import json
sys.path.extend(json.load(open('.vscode/settings.json'))['python.analysis.extraPaths'])
from loader import _LOAD
from SimulatedAnnealing import localSearch
from AlphaGreedyMinDMaxD import solve

def GRASP(ins, a, R, T):
    r = 0
    S = solve(a, _LOAD(ins))
    S, S_Star = localSearch(ins, S, T)

    while r < R:
        NS = solve(a, _LOAD(ins))
        NS, NS_Star = localSearch(ins, NS, T)
        if NS_Star < S_Star:
            S, S_Star = NS, NS_Star
        r += 1
    
    return S, S_Star

print(GRASP(sys.argv[1], eval(sys.argv[2]), eval(sys.argv[3]), eval(sys.argv[4])))