@echo off

pypy src\Solver\GRASP\SimulatedAnnealingMD1.py --ins instances/A/A-n80-k10.vrp --repeat 10  --seconds 30 --temperature 100 --alpha 1 --trace no --verbose no