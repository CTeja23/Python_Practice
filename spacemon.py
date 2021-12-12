def spacemonSim(roster1,roster2):

	planet_1 = [list(r) for r in roster1]
	planet_2 = [list(r) for r in roster2]

	roster1 = planet_1[0]
	roster2 = planet_2[0]

	planet_one = roster1[0]
	planet_one_energy = roster1[1]
	planet_one_power = roster1[2]

	planet_two = roster2[0]
	planet_two_energy = roster2[1]
	planet_two_power = roster2[2] 


	x = fight(planet_one,planet_two,planet_one_energy,planet_two_energy,planet_one_power,planet_two_power)

	if x[1] == True:
		planet_one_energy = x[0]
		planet_one = roster1[0]
		planet_one_energy = roster1[1]
		planet_one_power = roster1[2]


		roster2 = planet_2[1]
		planet_two = roster2[0]
		planet_two_energy = roster2[1]
		planet_two_power = roster2[2]
		y = fight(planet_one,planet_two,planet_one_energy,planet_two_energy,planet_one_power,planet_two_power)

		if y[1] == False:
			return False
		elif y[1] == True:
			return True

	elif x[1] == False:
		return False
			

def battle(planet_energy,damage):
	energy = planet_energy - damage
	return energy

def fight(planet_one,planet_two,planet_one_energy,planet_two_energy,planet_one_power,planet_two_power):
	attack_multiplier = { 'mercury' : { 'mercury': 1, 'venus': 2 , 'earth': 1 , 'mars': 0.5},
							'venus': { 'mercury': 0.5, 'venus': 1 , 'earth': 2 , 'mars': 1},
							'earth': {'mercury': 1, 'venus':  0.5, 'earth': 1 , 'mars': 2},
							'mars': {'mercury': 2, 'venus': 1 , 'earth': 0.5 , 'mars': 1}}


	damage_by_planet_one = attack_multiplier[planet_one.lower()][planet_two.lower()]*planet_one_power
	damage_by_planet_two = attack_multiplier[planet_two.lower()][planet_one.lower()]*planet_two_power

	player_choice = 1

	while planet_one_energy != 0 and planet_two_energy != 0:
		if player_choice == 1:
			power = damage_by_planet_one
			health = planet_two_energy
		elif player_choice == 2:
			power = damage_by_planet_two
			health = planet_one_energy


		if planet_one_energy != 0 or planet_two_energy != 0:
			x = battle(health,power)

			if player_choice == 1:
				planet_two_energy = abs(x)
				if planet_two_energy == 0:
					return [planet_one_energy, True]
				player_choice = 2
			elif player_choice == 2:
				planet_one_energy = abs(x)
				if planet_one_energy == 0:
					return [planet_two_energy,False]
				player_choice = 1


print(spacemonSim([('Earth',100,10)], [('Mercury',80,10), ('Mars',80,10)]))