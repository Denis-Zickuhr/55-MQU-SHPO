import argparse
import random
import sys
import json
import csv
sys.path.extend(json.load(open('.vscode/settings.json'))['python.analysis.extraPaths'])
from loader import _LOAD
from TabooSearch import localSearch
from AlphaGreedyMaxD import solve

def isBool(str):
    return str not in ['False', 'false', 'f', '!True', '!true', '!t', 'no', '!yes']

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('--ins', type=str)
   parser.add_argument('--alpha', type=float)
   parser.add_argument('--repeat', type=int)
   parser.add_argument('--seconds', type=int)
   parser.add_argument('--verbose', type=isBool)
   parser.add_argument('--trace',type=isBool)
   args = parser.parse_args()

def GRASP(ins, a, R, seconds, isVerbose=False, isTrace=False):

    r = 0
    S = solve(a, _LOAD(ins))
    S, S_Star = localSearch(ins, S, seconds)
    if isTrace:
        rn = str(random.randint(1, 999999))
        out_file = 'src/Solver/GRASP/out/tabooMD1-' + str(ins.replace("/", "-").replace(".vrp", "")) + '-r' + str(R) + '-' + str(rn) + '.csv'
        outf = open(out_file, "w", newline='')
        writer = csv.writer(outf)
        writer.writerow([f"{r};{int(S_Star)};{int(S_Star)}"])

    while r < R:
        NS = solve(a, _LOAD(ins))
        NS, NS_Star = localSearch(ins, NS, seconds)
        if NS_Star < S_Star:
            S, S_Star = NS, NS_Star
        if isTrace:
            writer.writerow([f"{r+1};{int(S_Star)};{int(NS_Star)}"])
        r += 1

    if isTrace:
        outf.close()
    
    if isVerbose:
        return S, S_Star
    else:
        return S_Star

print(GRASP(args.ins, args.alpha, args.repeat, args.seconds, args.verbose, args.trace))