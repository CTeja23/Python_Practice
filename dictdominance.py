def isGreaterThan(dict1,dict2):
	status = False


	similar_key_dict1 = dict()
	similar_key_dict2 = dict()

	for i in dict1.keys():
		for j in dict2.keys():
			if i == j :
				similar_key_dict1[i] = dict1[i]
				similar_key_dict2[j] = dict2[j]


	if bool(similar_key_dict1) == False and bool(similar_key_dict2) == False:
		status = False

	for k,n in zip(similar_key_dict1.values(),similar_key_dict2.values()):
		if k > n :
			status = True
		elif k < n :
			status = False


	return status



print(isGreaterThan({'a':3,'b':0},{'a':0,'b':1}))
# print(isGreaterThan({'a':1,'b':0},{'c': 0}))