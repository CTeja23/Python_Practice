d1={}
d2={}
d3={'dummy':0}
res = ""


n=int(input("enter d1"))
for i in range(n):
    key,value =input().split()
    d1[key]= value
print(d1)

w=int(input("enter d2"))
for j in range(w):
    key,value =input().split()
    d2[key]= value
print(d2)

if (len(d1) == len(d2)):
	for key in d1:
		
		if d1.get(key) == d2.get(key):
			res= False
		elif d1.get(key) > d2.get(key):
			res = True
		elif d1.get(key) < d2.get(key):
			res = False
			

if res == True:
	print("True sdfgrty")
else:
	print("False 456")