import matplotlib.pyplot as plt
import numpy as np
import csv
import array
import sys

fig = plt.figure()
fig.suptitle('coverage and time')
method = ['cfg', 'random', 'random_input', 'uniform_random','dfs_15', 'dfs_14']
try:
	directory = sys.argv[1] #directory
except:
	print 'Usage: python new_drawTime.py <FILE_DIRECTORY>'
	quit()


#Get data
iteration = 0
data = {}


for q in range(0, len(method)):
	sum_time = {}
	ave_time = {}
	db = []
	for i in range(0, 10):
		iteration = 0
		data = {}
		with open(directory + '/' + method[q] + '/coverages' + str(i) + '.csv', 'r') as raw:
			cooked = csv.reader(raw) #cooked: chunk of every record
			for record in cooked: #record: ['coverage', 'time']
				data[iteration] = record #data: {iteration, ['coverage', 'time']}
				iteration += 1 
		
			#add one coverage data to db[]
			db.append(data) #db: {file_num {iteration, ['coverage', 'time']}}

	time = {} #for time info
	for l in range(0, 10):
		for j in range(0, len(db[l])):
			if time.has_key(int(db[l][j][1])):
		 		#temp_of_temp.append(int(db[i][j][0])
				time[int(db[l][j][1])].append(int(db[l][j][0]))
			else:
				time[int(db[l][j][1])] = []
				time[int(db[l][j][1])].append(int(db[l][j][1]))		
	
	print(len(time))
	count = 0	
	for k in range(0, len(time)):
		ave_time[k] = sum(time[k])/float(len(time[k]))
		ave_time[k] = round(ave_time[k], 2)
		count += len(time[k])
	print('count: ' + str(count))
	print(ave_time)

	y = []
	for k in range(0, len(ave_time)):
		if k == 0:
			y.append(ave_time[k])			
		elif k != 0 and ave_time[k-1] <= ave_time[k]:
			y.append(ave_time[k])
		else:
			break

		
	x = [i for i in range(len(y))]

	print(y)
	plt.plot(x, y, label = method[q])

plt.xlabel('time(sec)')
plt.ylabel('coveraged branch')
plt.legend(loc = 'lower right')
plt.show()
