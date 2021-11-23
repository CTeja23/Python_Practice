# DEFYING GRAVITY 
# if isD==True then the value in the function is D or else its t



def freeFall(val,isD):
	

	if isD==True:

		distance = float(val)
		t = (2 * distance / 9.81) ** 0.5

		return round(t,2)

	else:
		time = float(val)

		d = 0.5 * 9.81 * time**2

		return round(d,2)


print(freeFall(1,True))
print(freeFall(0.45,False))