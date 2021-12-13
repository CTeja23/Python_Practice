# • str2list(‘[abc]’) should return [‘a’,‘b’,‘c’].
# • str2list(‘[a[bc]]’) should return [‘a’,[‘b’,‘c’]].


def str2list(l):

	stack = [[]]

	for i in l:
		if i == '[':
			stack[-1].append([])
			stack.append(stack[-1][-1])
		elif i == ']':
			stack.pop()
			if not stack:
				pass

		else:
			stack[-1].append(i)

	stack = stack.pop()

	return stack[0]


print(str2list('[a[bc]]'))









