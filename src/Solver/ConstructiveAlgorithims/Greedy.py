import sys
sys.path.append('55-MQU-SHPO/src/Utils')
from loader import _LOAD



(k, d, c, P, D, Depot) = _LOAD('55-MQU-SHPO\instances\A-n32-k5.txt')

print(k, d, c, P, D, Depot)