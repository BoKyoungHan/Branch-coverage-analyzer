import matplotlib.pyplot as plt
import numpy as np
import csv
import array

fig = plt.figure()
fig.suptitle('coverage and iterations')
#fig, ax_lst = plt.subplots(2, 2)

#x = np.linspace(0,100,100)
#plt.plot(x, x, label='linear')

method = ['cfg', 'random', 'random_input', 'uniform_random', 'dfs_15', 'dfs_14']

#Get data
iteration = 0
data = {}

cfg = []
sum_for_coverage = {}

for j in range(0, len(method)):
	# iteration = 0
	# data = {}
	for i in range(0, 10):
		with open('../data_1220_v2/' + method[j] + '/coverages' + str(i) + '.csv', 'r') as raw:
			cooked = csv.reader(raw) #cooked: chunk of every record
			for record in cooked: #record: ['coverage', 'time']
				data[iteration] = record #data: {iteration, ['coverage', 'time']}
				if i == 0:
					sum_for_coverage[iteration] = int(record[0])
				else:
					sum_for_coverage[iteration] += int(record[0])
				iteration += 1 
		
			#add one coverage data to cfg[]
			cfg.append(data)
			if i != 9: #initialize info for next coverages.csv file
				iteration = 0
				data = {}

	for i in range(0, iteration):
		sum_for_coverage[i] = sum_for_coverage[i]/10.0

	#print(iteration)
	#x = [i for i in range(iteration)]
	if method[j] == 'dfs_14':
		x = [i for i in range(iteration)]
		y = []
		for i in range(0, iteration):
			y.append(sum_for_coverage[i])
	else:
		x = [i for i in range(4999)]
		y = []
		for i in range(0, 4999):
			y.append(sum_for_coverage[i])

	plt.plot(x, y, label = method[j])

plt.xlabel('iterations')
plt.ylabel('coveraged branch')
plt.legend(loc = 'lower right')
plt.show()
