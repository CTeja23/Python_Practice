def freeFall(val,isD):
	val = float(val)
	while isD:
		t = (2*val/9.81) ** 0.5
		return round(t,2)
	else:
		d = 0.5 * 9.81 * val**2
		return round(d,2)






# print(freeFall(1,True))
# print(freeFall(0.45,False))