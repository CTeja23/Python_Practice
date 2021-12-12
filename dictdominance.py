
# • dict1={‘a’:1,‘b’:2} and dict2={‘a’:1,‘b’:1}. In this case, dict1 is equal to dict2 with respect to a, but it is greater with respect to b; therefore, the function should return True.
# • dict1={‘a’:1,‘b’:1} and dict2={‘a’:1,‘b’:1}. In this case, dict1 and dict2 are equivalent; therefore, the function should return False.
# • dict1={‘a’:1,‘b’:0} and dict2={‘a’:0,‘b’:1}. In this case, dict1 is greater than dict2 with respect to a, but it is lower with respect to b; therefore, the function should return False.


# • dict1={‘a’:1,‘b’:2,‘c’:-10} and dict2={‘a’:1,‘b’:1}. dict1 is greater than dict2 with respect to all the keys; therefore, the func- tion should return True.
# • dict1={‘a’:1,‘b’:1} and dict2={‘c’:0}. In this case, dict1 is not greater than dict2, as dict1 does not have the key c; therefore the function should return False.


# if even one (key,value) in dict1 is greater than  (key,value) in dict2:
# 	  then return True

# if all the key,value in dict1 and dict2 are equal :
# 	 then return False
 
# if there is a similar key in dict1 and dict2 :
# 	and values of the simliar keys of dict1 are greater than dict2 :
# 		then return True
# 	else if there are no similar pairs:
# 		 then return False


def isGreaterThan(dict1,dict2):
	status = False


	similar_key_dict1 = dict()
	similar_key_dict2 = dict()

	for i in dict1.keys():
		for j in dict2.keys():
			if i == j :
				similar_key_dict1[i] = dict1[i]
				similar_key_dict2[j] = dict2[j]

	# print(similar_key_dict1,similar_key_dict2)


	if bool(similar_key_dict1) == False and bool(similar_key_dict2) == False:
		status = False

	else:
		for k,n in zip(similar_key_dict1.values(),similar_key_dict2.values()):
			print(k,n)
			if k > n :
				print(k,n)
				status = True
			else:
				status = False
	return status

print(isGreaterThan({'a':1,'b':0},{'a':0,'b':1}))
# print(isGreaterThan({'a':1,'b':0},{'c': 0}))