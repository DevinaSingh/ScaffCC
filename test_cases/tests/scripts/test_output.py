from qiskit import *
import os
import glob
import sys
import json
from qiskit.transpiler import PassManager, transpile
from qiskit.transpiler.passes import ResourceEstimation

# Add config directory to filepath
sys.path.append(os.getcwd()[:-7] + 'config')
import Config_IBMQ_experience
from qiskit.transpiler.passes import resource_estimation

'''// NISQ_tests
	// config files with API token and URL 
	// each type of NISQ_test
		// qasm, qasmh, qasmf, scaffold, number of gates, counts
	// scripts
		// get_gates
		// run all the tests and compare measurments'''

filepath = os.getcwd()
benchmarks_filepath = filepath[:-7] + 'benchmarks'
root = filepath[:-13]
scaf_filepath = root + "scaffold.sh"

print("\nRunning NISQ Test Benchmarks")
print("===================================")

IBMQ_token = Config_IBMQ_experience.API_token
IBMQ_URL = Config_IBMQ_experience.API_URL
IBMQ.enable_account(IBMQ_token, IBMQ_URL)

backend_sim = IBMQ.get_backend('ibmq_qasm_simulator')
correct_tests = 0
total_tests = 0


for path, subdir, files in os.walk(benchmarks_filepath):
	for file_name in files:
		'''if (file_name.endswith(".scaffold")):
			print(file_name[:-9] + " Generating Hierarchical Qasm File")
			os.system(scaf_filepath + " -q -T  " + benchmarks_filepath + "/" + file_name[:-9] + "/" + file_name)
			print(file_name[:-9] + " Generating Flattened Qasm File")
			os.system(scaf_filepath + " -f -T  " + benchmarks_filepath + "/" + file_name[:-9] + "/" + file_name)
			print(file_name[:-9] + " Generating Open Qasm File")
			os.system(scaf_filepath + " -b -T  " + benchmarks_filepath + "/" + file_name[:-9] + "/" + file_name)'''
		if (file_name.endswith(".qasm")):
			qc = QuantumCircuit.from_qasm_file(benchmarks_filepath + "/" + file_name[:-5] + "/" + file_name)

			print('\033[1m' + "Generating " + file_name[:-5] + " Resource Estimation" + '\033[0m')
			passmanager = PassManager()
			passmanager.append(ResourceEstimation())
			resources = qiskit.compiler.transpile(qc, backend_sim, pass_manager=passmanager)
			print("Size: " + str(passmanager.property_set['size']) + "; Depth: " + str(passmanager.property_set['depth']) + "; Width: " + str(passmanager.property_set['width']) + "; Count Ops: " + str(passmanager.property_set['count_ops']))

			print('\033[1m'+ "Testing " + file_name[:-5] + " measurement output ---" + '\033[0m', end =" ")
			job_sim = execute(qc, backend_sim) # default is 1024 shots
			result_sim = job_sim.result()
			counts_sim = result_sim.get_counts(qc)
			counts = json.dumps(counts_sim).split("\"")[1]
			benchmark_file = benchmarks_filepath + "/" + file_name[:-5] + "/" + file_name[:-5] + ".counts"
			counts_file = open(benchmark_file, "r")
			benchmark_measurement = counts_file.readline()
			print(counts)
			if counts == benchmark_measurement:
				print('\033[92m' + "  passed" + '\033[0m' + '\n')
				correct_tests = correct_tests + 1
			else:
				print('\033[91m' + " failed - " + str(counts) +" measurement is not " + benchmark_measurement + '\033[0m' + '\n')
			total_tests = total_tests + 1


print("\n===================================")
if (correct_tests == total_tests):
	print('\033[92m' + str(correct_tests) + "/" + str(total_tests) + " tests passed" + '\033[0m')
else:
	print('\033[91m' + str(correct_tests) + "/" + str(total_tests) + " tests passed"  + '\033[0m')



IBMQ.disable_accounts(token=IBMQ_token)


