import numpy
import sys
sys.path.append('./src/Utils')
from loader import _LOAD

(k, d, c, P, D, Depot) = _LOAD('.\instances\A-n32-k5.txt')

def InitialSolutionGreedy():

    Pw = P.copy()
    Dc = D.copy()

    S = [[0 for i in range(d)] for i in range(k)]

    BetterClients = numpy.array([None for i in range(d)] for i in range(k))

    S_Value = 0
    while (Dc.count(0) != len(Dc)):

        # Seleciona o cliente mais próximo para o K veiculo

        xy = 0
        path = [xy, xy]
        TOTAL_DISTANCE = 0
        TOTAL_COST = 0
        COST = 0
        MINIMAL_COST = 0
        
        for j in range(d):

            index = None
            
            DISTANCE_DEMAND_RATIO = -sys.maxsize

            for i in range(d):

                if(xy == None):
                    break
                value = Pw[i][xy]

                f = Dc[i]/value

                if f > DISTANCE_DEMAND_RATIO and i not in path and Dc[i] != 0 and c - (TOTAL_COST + D[xy])  >= 0:
                    DISTANCE_DEMAND_RATIO = f
                    COST = D[xy]
                    MINIMAL_COST = value
                    index = i
            
            xy = index
            if(xy != None and not 0):
                path.insert(1, xy)
                TOTAL_DISTANCE += MINIMAL_COST
                TOTAL_COST += COST
                Dc[xy] = 0
        
        S_Value += TOTAL_DISTANCE
        print(path, "CP: ", round(TOTAL_DISTANCE, 2), "CR: ", round(TOTAL_COST, 2))  

    print("Valor da Solução", S_Value)       

            

                
    # numpy.set_printoptions(threshold=sys.maxsize)
    # print(numpy.asanyarray(Pw))

    # se não viola restrições adiciona

    return S

InitialSolutionGreedy()
# print(InitialSolutionGreedy())