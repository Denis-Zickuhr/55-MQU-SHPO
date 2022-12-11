@echo off

pypy src\Solver\GRASP\SimulatedAnnealingMD1.py --ins instances/A/A-n37-k5.vrp --repeat 10  --seconds 30 --temperature 100 --alpha 0.27 --trace no --verbose no