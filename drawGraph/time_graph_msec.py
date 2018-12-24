import matplotlib.pyplot as plt
import numpy as np
import csv
import array
import sys
from math import floor


size = 100
fig = plt.figure()
fig.suptitle('coverage and time(' + str(1/float(100))+ ' sec)')
method = ['cfg', 'random', 'random_input', 'uniform_random','dfs_15', 'dfs_14']
try:
	directory = sys.argv[1] #directory
except:
	print 'Usage: python time_graph_msec.py <FILE_DIRECTORY>'
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
	for f in range(0, 10):
		for j in range(0, len(db[f])):
			if time.has_key(floor(float(db[f][j][1]) * size) / size):
		 		time[floor(float(db[f][j][1]) * size) / size].append(float(db[f][j][0]))
			else:
				time[floor(float(db[f][j][1]) * size) / size] = []
				time[floor(float(db[f][j][1]) * size) / size].append(float(db[f][j][0]))		
	
	
	
	for k in sorted(time):
		ave_time[k] = sum(time[k])/float(len(time[k])) #k is key
		ave_time[k] = round(ave_time[k], 2)
		

	y = []
	count = 0
	pre_key = 0
	for k in sorted(time):
		y.append(ave_time[k])

		#try to delete suddenly dereasing part (not perfect)#
		# if count == 0:
		#  	y.append(ave_time[k])
		#  	pre_key = k		
		# elif count != 0 and ave_time[pre_key] <= ave_time[k]:
		#  	y.append(ave_time[k])
		# else:
		#  	break
		# count += 1

	x = []	
	for i in sorted(time):
		x.append(i)

	#try to delete suddenly dereasing part (not perfect)#
	# for i in range(0, len(y)):
		# x.append(round(1/float(size),2) * i)

	print(x)
	print(y)
	#if q == 0:
	plt.plot(x, y, label = method[q])


plt.xlabel('time(sec)')
plt.ylabel('coveraged branch')
plt.legend(loc = 'lower right')
plt.show()
