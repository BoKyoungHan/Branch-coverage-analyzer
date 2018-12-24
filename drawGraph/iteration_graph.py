import matplotlib.pyplot as plt
import numpy as np
import csv
import array
import sys
import os

fig = plt.figure()
fig.suptitle('iterations and covered branch')
#method = ['cfg', 'random', 'random_input', 'uniform_random','dfs_17', 'dfs_16', 'dfs_15', 'dfs_14']


try:
	directory = sys.argv[1] #directory
except:
	print('Usage: python iteration_graph.py <FILE_DIRECTORY>')
	quit()

file_list = os.listdir(directory)
file_list.sort()

print(file_list)


#Get data
iteration = 0
data = {}

db = []

for j in range(0, len(file_list)):

	sum_for_coverage = {}
	ave_for_coverage = {}
	db = []
	print(file_list[j])
	num_of_cov_file = 0
	#TODO count coverages? files and do not use magic number
	sub_flie_list = os.listdir(directory + '/' + file_list[j])
	for k in sub_flie_list:
		if k[0:9] == 'coverages':
			num_of_cov_file += 1 
	#print('cov_file' + str(num_of_cov_file)) 


	#convert non-csv file to csv file
	os.system('for cov in `ls ' + directory + '/' + file_list[j] + '/' + 'coverages?`; do mv $cov ${cov}.csv; done')

	for i in range(0, num_of_cov_file):
		#Do initialize!!!
		iteration = 0
		data = {}

		with open(directory + '/' + file_list[j] + '/coverages' + str(i) + '.csv', 'r') as raw:
			cooked = csv.reader(raw) #cooked: chunk of every record
			for record in cooked: #record: ['coverage', 'time']
				data[iteration] = record #data: {iteration, ['coverage', 'time']}
	
				if iteration in sum_for_coverage:
					sum_for_coverage[iteration] += int(record[0])
				else:
					sum_for_coverage[iteration] = int(record[0])
					
				iteration += 1 
						
			#add one coverage data to db[]
			db.append(data)
			

	for k in range(0, iteration):
		ave_for_coverage[k] = sum_for_coverage[k]/num_of_cov_file

	x = [l for l in range(iteration)]
	print('x' + str(len(x)))
	y = []
	for l in range(0, iteration):
		y.append(ave_for_coverage[l])
	print('y' + str(len(y)))


	plt.plot(x, y, label = file_list[j])

	print('strategy:' + file_list[j] + ', max covered branch: ' + str(ave_for_coverage[iteration-1]))

plt.xlabel('iterations')
plt.ylabel('coveraged branch')
plt.legend(loc = 'lower right')
plt.show()
