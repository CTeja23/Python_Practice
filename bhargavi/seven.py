
def str2list(l):

	output = [[]]
	for i in l:
		if i == '[':
			output[-1].append([])
			output.append(output[-1][-1])
		elif i == ']':
			output.pop()
		else:
			output[-1].append(i)
	output = output.pop()

	return output[0]


print(str2list('[a[bc]]'))






