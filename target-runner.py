import argparse
import os
import sys
import subprocess
import random

# Get the parameters as command line arguments
configuration_id = sys.argv[1]
instance_id = sys.argv[2]
seed = sys.argv[3]
instance = sys.argv[4]
alghorthim = ''.join(sys.argv[5])
conf_params = ' '.join(sys.argv[6:])

algDict = {
    "GSS1": "src\Solver\GRASP\SimpleSearchMD1.py",
    "GSS2": "src\Solver\GRASP\SimpleSearchMD2.py",
    "GSA1": "src\Solver\GRASP\SimulatedAnnealingMD1.py",
    "GSA2": "src\Solver\GRASP\SimulatedAnnealingMD2.py",
    "GTS1": "src\Solver\GRASP\TabooSearchMD1.py",
    "GTS2": "src\Solver\GRASP\TabooSearchMD2.py",
}

# Create execution command
fixed_params = ' --repeat 1 --seconds 1 '
command = 'pypy ' + algDict[alghorthim] + ' --ins ' + instance + fixed_params + conf_params

# Define the stdout and stderr files
r = str(random.randint(1, 999999))
out_file = './c' + str(configuration_id) + '-' + str(instance_id) + '-' + r + '.stdout'
err_file = './c' + str(configuration_id) + '-' + str(instance_id) + '-' + r + '.stderr'

# Execute
outf = open(out_file, "w")
errf = open(err_file, "w")
return_code = subprocess.call(command, stdout = outf, stderr = errf, shell = True)
outf.close()
errf.close()

# Check return code
if return_code != 0:
    print('Command returned code <' + str(return_code) + '>.')
    sys.exit(1)

# Check output file
if not os.path.isfile(out_file):
    print('Output file <' + out_file  + '> not found.')
    sys.exit(1)

# Get result and print it
result = open(out_file)
lastLine = result.readlines()[-1]
result.close()
lastLine = int(float(lastLine.replace('\n', '')))
print(lastLine)

# Clean files and exit
os.remove(out_file)
os.remove(err_file)
sys.exit(0)
