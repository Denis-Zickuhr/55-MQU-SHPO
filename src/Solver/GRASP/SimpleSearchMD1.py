import argparse
import sys
import json
sys.path.extend(json.load(open('.vscode/settings.json'))['python.analysis.extraPaths'])
from loader import _LOAD
from SimpleSearch import localSearch
from AlphaGreedyMaxD import solve

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('--ins', type=str)
   parser.add_argument('--alpha', type=float)
   parser.add_argument('--repeat', type=int)
   parser.add_argument('--seconds', type=int)
   args = parser.parse_args()

def GRASP(ins, a, R, seconds):
    r = 0
    S = solve(a, _LOAD(ins))
    S, S_Star = localSearch(ins, S, seconds)

    while r < R:
        NS = solve(a, _LOAD(ins))
        NS, NS_Star = localSearch(ins, NS, seconds)
        if NS_Star < S_Star:
            S, S_Star = NS, NS_Star
        r += 1
    
    return S_Star

print(GRASP(args.ins, args.alpha, args.repeat, args.seconds))