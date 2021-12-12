

file = open('test.csv','r').read().strip().split('\n')

file = [ x.split(',') for x in file]


new_data = list()

for lst in file:
	new_lst = []
	for item in lst:
		item = item.strip()
		new_lst.append(item)
	new_data.append(new_lst)

values = new_data[1:]
s__ = list()
total = 0

for row in range(len(values[0])):
	for col in range(len(values)):
		total += float(values[col][row])
	s__.append(total)
	total = 0



print(s__)

