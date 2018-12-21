import matplotlib.pyplot as plt
import numpy as np
import csv
import array

fig = plt.figure()
fig.suptitle('coverage and iterations')
#fig, ax_lst = plt.subplots(2, 2)

#x = np.linspace(0,100,100)
#plt.plot(x, x, label='linear')

method = ['cfg', 'dfs', 'random', 'random_input', 'uniform_random']

#Get data
iteration = 0
data = {}
time = {}


cfg = []
sum_time = {}
ave_time = {}
count = {}
for q in range(0, len(method)):
	for i in range(0, 10):
		iteration = 0
		with open('../data_1220/' + method[q] + '/coverages' + str(i) + '.csv', 'r') as raw:
			cooked = csv.reader(raw) #cooked: chunk of every record
			for record in cooked: #record: ['coverage', 'time']
				data[iteration] = record #data: {iteration, ['coverage', 'time']}
				#if i == 0:
				#	sum_for_coverage[iteration] = int(record[0])
				#else:
				#	sum_for_coverage[iteration] += int(record[0])
				iteration += 1 
		
			#add one coverage data to cfg[]
			cfg.append(data)
			if i != 9: #initialize info for next coverages.csv file
				iteration = 0
				data = {}
	
	for i in range(0, 10):
		temp = []
		time = {}
		curr_time = 0 # starat from 0 sec 
		for j in range(0, len(cfg[i])):
			if curr_time == int(cfg[i][j][1]):
				#temp_of_temp.append(int(cfg[i][j][0])
				temp.append(int(cfg[i][j][0]))
			elif j == len(cfg[i]) -1: #save time == 9 data
				time[curr_time] = temp
			else:
				time[curr_time] = temp #save previous data	
				curr_time += 1
				temp = []
				temp.append(int(cfg[i][j][0]))
		if q == 0:
			print(time)
		for k in range(0, len(time)):
			#print(time[k])			
			if sum_time.has_key(k):
				sum_time[k] += sum(time[k])
		#		print(sum(time[k]))
			else:
				sum_time[k] = (sum(time[k]))
			if count.has_key(k):
				count[k] += len(time[k])
			else:
				count[k] = (len(time[k]))
	print("sum")
	print(sum_time)
	for k in range(0, len(sum_time)):
		ave_time[k] = sum_time[k]/float(count[k])
		ave_time[k] = round(ave_time[k], 2)
	print(j)
	#print("ave")
	#print(ave_time)
	print("count")
	print(count)
	#print(iteration)
	x = [i for i in range(len(ave_time))]
	y = []
	for i in range(0, len(ave_time)):
		y.append(ave_time[i])
	
	#print(x)
	#print(y)
	plt.plot(x, y, label = method[q])

plt.xlabel('time(sec)')
plt.ylabel('coveraged branch')
plt.legend(loc = 'lower right')
plt.show()
