
def clickcounter(l):

	dict_values = { 'A': 0 , 'B': 1 , 'C': 2, 'D':3,'E':4,'F':5,'G': 6}
	common_dict = dict()
	edge = list()

	def GetKey(val):
	   for key, value in dict_values.items():
	      if val == value:
	         return key

	for row in range(len(l)):
		for col in range(len(l)):
			if l[row][col] == 1:
				edge.append([row,col])
			else:
				pass

	i = list()
	for lst in edge:
		for key,value in dict_values.items():
			if lst[0] == value:
				i.append([key,GetKey(lst[1])])
			else:
				pass

	res = list(set(tuple(sorted(sub)) for sub in i))

	res = sorted(res)
	
	l = list()
	for i in res:
		l.append(list(i))
	

	




	print(n_dict)



	

		












print(clickcounter([[0,1,1,0,0,0,0],[1,0,1,1,0,0,0],[1,1,0,0,0,0,0],[0,1,0,0,1,1,1],[0,0,0,1,0,1,0],[0,0,0,1,1,0,1],[0,0,0,1,0,1,0]]))



