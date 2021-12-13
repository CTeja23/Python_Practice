with open('test.csv','r') as f:
	data = f.read().strip().split('\n')
	data = [i.split(',') for i in data]


	matrix = []
	for lst in data:
		matrix_row = []
		for num in lst:
			num = num.strip()
			matrix_row.append(num)
		matrix.append(matrix_row)

	del matrix[0]

	output = []
	count = 0

	for i in range(len(matrix[0])):
		for j in range(len(matrix)):
			count += float(matrix[j][i])
		output.append(count)
		total = 0

	print(output)










