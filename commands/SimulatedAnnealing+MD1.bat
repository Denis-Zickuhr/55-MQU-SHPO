@echo off

pypy src\Solver\GRASP\SimulatedAnnealingMD1.py --ins instances/A/A-n80-k10.vrp --repeat 100  --seconds 30 --temperature 78 --alpha 0.28 --trace yes --verbose no