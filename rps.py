# RPS(‘RPS’) should return ‘PSR’.
# RPS(‘PRSPRR’) should return ‘SPRSPP’.



d = { 'R' : 'P' , 'P' : 'S' , 'S' : 'R'}


def RPS(UI):
	computer_shape = ''
	if UI.isupper() == True:
		UI = UI
	else:
		UI = UI.upper()
	for i in UI:
		for j,k in d.items():
			if j == i :
				computer_shape += k

	return computer_shape




print(RPS('RPS'))