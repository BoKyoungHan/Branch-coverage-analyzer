import os
import sys
import shutil

program = sys.argv[1] #program
noi = sys.argv[2] #number of iterations
strategy = sys.argv[3] #strategy

if strategy == '-dfs' :
	bound = sys.argv[4] #only for bounded dfs	
file_dir = strategy[1:] + '_input'
#path = '/' + strategy[1:] + '/' 

#TODO exception handling

command1 = '../bin/crestc ./' + program
command2 = '../bin/run_crest ' + './' + program[ :-2] + ' ' + noi + ' ' + strategy

if strategy == '-dfs' :
	command2 = command2 + ' ' + bound

print(command2)

for x in range (10):
	os.system(command1) #crestc
	os.system(command2) #run_crest	
	if os.path.exists(file_dir) :
		print("d")
		shutil.copy2('input', file_dir + '/input' + str(x) + '.txt')
	else :
		os.system('mkdir ' + file_dir) 
		shutil.copy2('input', file_dir + '/input' + str(x) + '.txt')
