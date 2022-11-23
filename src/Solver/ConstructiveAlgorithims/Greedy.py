import sys
sys.path.append('./src/Utils')
from loader import _LOAD

(k, d, c, P, D, Depot) = _LOAD('.\instances\A-n32-k5.txt')

print(P)

def InitialSolotionGreedy():

    S = [[0 for i in range(d)] for i in range(k)]

    while(len(P) > 0):
        # Seleciona os K clientes mais próximos
        pass
    
    return S

print(InitialSolotionGreedy())