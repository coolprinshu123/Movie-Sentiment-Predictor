import os
import sys

if len(sys.argv) <2:
	print "Incorrect argument provided. Format : python master.py task_no"
	exit(0)

path = os.getcwd()
if int(sys.argv[1]) == 2:
	pathFile = "python " + path + "/create_decision_tree.py"
	os.system(pathFile)
	
elif int(sys.argv[1]) == 3:
	pathFile = "python " + path + "/noise_addition.py"
	os.system(pathFile)
	
elif int(sys.argv[1]) == 4:
	pathFile = "python " + path + "/pruning.py"
	os.system(pathFile)
	
elif int(sys.argv[1]) == 5:
	pathFile = "python " + path + "/random_forest.py"
	os.system(pathFile)
	
else:
	print "Invalid argument provided."
