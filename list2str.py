# • list2str([‘a’,[‘b’,‘c’]]) should return ‘[a[bc]]’.
# • list2str([‘a’,[‘b’,[‘c’]]]) should return ‘[a[b[c]]]’.



def get_strings(l):
	string = ""
	for i in l:
		if type(i) is list:
			string += '['+str(get_strings(i))+']'
		else:
			string += str(i)
	
	return string


def list2str(l):
	s = get_strings(l)
	return '['+s+']'



print(list2str(['a',['b',['c',['d']]]]))