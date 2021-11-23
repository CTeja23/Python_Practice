
# • dict1={‘a’:1,‘b’:2} and dict2={‘a’:1,‘b’:1}. In this case, dict1 is equal to dict2 with respect to a, but it is greater with respect to b; therefore, the function should return True.
# • dict1={‘a’:1,‘b’:1} and dict2={‘a’:1,‘b’:1}. In this case, dict1 and dict2 are equivalent; therefore, the function should return False.
# • dict1={‘a’:1,‘b’:0} and dict2={‘a’:0,‘b’:1}. In this case, dict1 is greater than dict2 with respect to a, but it is lower with respect to b; therefore, the function should return False.


# • dict1={‘a’:1,‘b’:2,‘c’:-10} and dict2={‘a’:1,‘b’:1}. dict1 is greater than dict2 with respect to all the keys; therefore, the func- tion should return True.
# • dict1={‘a’:1,‘b’:1} and dict2={‘c’:0}. In this case, dict1 is not greater than dict2, as dict1 does not have the key c; therefore the function should return False.



def isGreaterThan(dict1,dict2):
	