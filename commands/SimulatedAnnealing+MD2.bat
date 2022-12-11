@echo off

pypy src\Solver\GRASP\SimulatedAnnealingMD2.py --ins instances/A/A-n80-k10.vrp --alpha 0.29 --repeat 10 --temperature 100 --seconds 30 --trace yes --verbose no