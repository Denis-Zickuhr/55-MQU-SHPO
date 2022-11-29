import copy
import itertools
import sys
import numpy
import time
sys.path.append('./src/Solver/ValueCalculation')
sys.path.append("./src/Solver/ConstructiveAlgorithims")
sys.path.append('./src/Utils')
from loader import _LOAD
from calc import calcdistance
from calc import calcweigth
from Greedy import InitialSolutionGreedy

def relocate(Solution, Demand, calcw):
    Load, Weigth, Valid = calcw
    Solutions = []
    size = len(Solution)
    for i in range(size):
        for j in range(len(Solution[i])):
            client_origin = Solution[i][j]
            if client_origin != 0: 
                weigth_origin = Demand[client_origin]
                for k in range(size-1):
                    Dummy = copy.deepcopy(Solution)
                    if Weigth - (Load[k+1] + weigth_origin) >= 0:
                        Dummy[i].remove(client_origin)
                        Dummy[k+1][-1:-1] = [client_origin]
                        Solutions.append(copy.deepcopy(Dummy))
                        Dummy.clear()

    return Solutions

def swap(Solution, Demand, calcw):
    print(Solution)
    Load, Weigth, Valid = calcw
    Solutions = []
    size = len(Solution)
    for i in range(size):
        for j in range(len(Solution[i])):
            client_origin = Solution[i][j]
            if client_origin != 0: 
                W_origin = Demand[client_origin]
                for k in range(size-1):
                    for l in range(len(Solution[k+1])-2):
                        client_destiny = Solution[k+1][l+1]
                        if client_destiny != 0 and client_destiny != client_origin: 
                            W_destiny = Demand[client_destiny]
                            Dummy = copy.deepcopy(Solution)
                            destiny_truck_cargo = Weigth - (Load[k+1] + W_origin)
                            origin_truck_cargo = Weigth - (Load[i] + W_destiny)
                            if destiny_truck_cargo >= 0 and origin_truck_cargo >= 0:
                                Dummy[i][j] = client_destiny
                                Dummy[k+1][l+1]= client_origin
                                Solutions.append(copy.deepcopy(Dummy))
                                Dummy.clear()

    return Solutions

Solution  = InitialSolutionGreedy(_LOAD('./instances/A/A-n37-k5.vrp'))
(k, d, c, P, D) = _LOAD('./instances/A/A-n37-k5.vrp')

print(swap(Solution, D, calcweigth(Solution, D, c)))