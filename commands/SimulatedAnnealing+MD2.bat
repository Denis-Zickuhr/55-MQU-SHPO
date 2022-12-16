@echo off

pypy src\Solver\GRASP\SimulatedAnnealingMD2.py --ins instances/A/A-n33-k5.vrp --alpha 0.26 --repeat 100 --seconds 60 --trace yes --verbose no --totaltime 300 --temperature 78