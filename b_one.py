class inp():
	def __init__(self,val,isD):
		self.val = val
		self.isD = isD

	def freeFall(self):
		if self.isD==True:

			distance = float(self.val)
			t = (2 * distance / 9.81) ** 0.5

			print(round(t,2))

		else:
			time = float(self.val)

			d = 0.5 * 9.81 * time**2

			print(round(d,2))



p = inp(0.45,False)
p.freeFall()