# 
b = [100,2,100,2,100]
#b = [3,15,4,12,10]
#b = [4,7,9]
list_tuples = []
for it in range(len(b)-1):
	pair1 = b[it]
	pair2 = b[it+1]
	dif1 = [abs(pair1 - 1),abs(pair1 - pair2)] 
	dif2 = [abs(pair2 - 1),abs(pair2 - pair1)]

	# testing
	pos_pair2 = dif1.index(max(dif1[0],dif1[1]))
	pos_pair1 = dif2.index(max(dif2[0],dif2[1]))
	
	item_pair1, item_pair2 = [0,0]
	
	item_pair1 = pair1 if(pos_pair1 == 1) else 1
	item_pair2 = pair2 if(pos_pair2 == 1) else 1

	option1 = (pair2,item_pair1)
	option2 = (item_pair2,pair1)
	list_tuples += [[option1,option2]]

#print(list_tuples)
options = []
for it in range(len(list_tuples)):
	

	dif1 = abs(list_tuples[it][0][1] - list_tuples[it][0][0])
	dif2 = abs(list_tuples[it][1][1] - list_tuples[it][1][0])
	

	if(it==0):
		if(dif1>dif2):
		# if differences are equal by default take the first option
			curr_option = list_tuples[it][0]
		elif(dif1<dif2):
			curr_option = list_tuples[it][1]
	else:
		if(dif1>dif2):
			if(curr_option[0] == list_tuples[it][0][1]):
				curr_option = list_tuples[it][0]
			else:
				curr_option = list_tuples[it][1]
		elif(dif1<dif2):
			if(curr_option[0] == list_tuples[it][1][1]):
				curr_option = list_tuples[it][1]
			else:
				curr_option = list_tuples[it][0]
		else:
			break
	
	# print("curr_option:",curr_option)
	# print("curr_option:",curr_option[1])

	# only the first value in the tuple
	options += [curr_option[1]]
	
	# print(curr_option)
	# print(list_tuples[it][0],list_tuples[it][1])
	
	# check links coincidence (todo: check all options)
	# TODO: not always the maximum difference is the correct choice
	if(it!=len(list_tuples)-1 and ((curr_option[0] != list_tuples[it+1][0][1]) and (curr_option[0] != list_tuples[it+1][1][1]))):
		# print("pop")
		break

	if(it==len(list_tuples)-1):
		#adding last pair item from the current option
		options += [curr_option[0]]

# print(options)
acum = 0
for it in range(len(options)-1):
	acum += abs(options[it+1] - options[it])
# print(acum)
	







