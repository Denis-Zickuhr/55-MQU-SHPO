import sys
import json
sys.path.extend(json.load(open('.vscode/settings.json'))['python.analysis.extraPaths'])
from loader import _LOAD
from SimpleSearch import localSearch
from AlphaGreedyMinDMaxD import solve

def GRASP(ins, ts, tx, a, R):
    r = 0
    S = solve(a, _LOAD(ins))
    S, S_Star = localSearch(ins, ts, tx, S)

    while r < R:
        NS = solve(a, _LOAD(ins))
        NS, NS_Star = localSearch(ins, ts, tx, NS)
        if NS_Star < S_Star:
            S, S_Star = NS, NS_Star
        r += 1
    
    return S, S_Star

print(GRASP(sys.argv[1], eval(sys.argv[2]), eval(sys.argv[3]), eval(sys.argv[4]), eval(sys.argv[5])))