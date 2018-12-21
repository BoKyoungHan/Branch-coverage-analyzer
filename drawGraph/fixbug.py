import matplotlib.pyplot as plt
import numpy as np
import csv
import array
import sys

fig = plt.figure()
fig.suptitle('iterations and covered branch')

try:
	directory = sys.argv[1] #directory
except:
	print 'Usage: python fixbug.py <FILE_DIRECTORY>'
	quit()


method = ['cfg', 'random', 'random_input', 'uniform_random', 'dfs_15', 'dfs_14']

#Get data
iteration = 0
data = {}

db = []

for j in range(0, len(method)):

	sum_for_coverage = {}
	ave_for_coverage = {}
	db = []
	print(method[j])
	for i in range(0, 10):
		#Do initialize!!!
		iteration = 0
		data = {}
		with open(directory + '/' + method[j] + '/coverages' + str(i) + '.csv', 'r') as raw:
			cooked = csv.reader(raw) #cooked: chunk of every record
			for record in cooked: #record: ['coverage', 'time']
				data[iteration] = record #data: {iteration, ['coverage', 'time']}
	
				if sum_for_coverage.has_key(iteration):
					sum_for_coverage[iteration] += int(record[0])
				else:
					sum_for_coverage[iteration] = int(record[0])
					
				iteration += 1 
						
			#add one coverage data to db[]
			db.append(data)
			

	for k in range(0, iteration):
		ave_for_coverage[k] = sum_for_coverage[k]/10.00

	x = [l for l in range(iteration)]
	print 'x' + str(len(x))
	y = []
	for l in range(0, iteration):
		y.append(ave_for_coverage[l])
	print 'y' + str(len(y))


	plt.plot(x, y, label = method[j])

plt.xlabel('iterations')
plt.ylabel('coveraged branch')
plt.legend(loc = 'lower right')
plt.show()
