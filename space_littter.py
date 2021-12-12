def spacemonSim(roster1,roster2):

	

	battle_round = 0

	roaster_one = list(roster1[0])
	roster_two = list(roster2[0])

	x = fight(roaster_one,roster_two)

	if x[1]==True:
		




def battle(planet_energy,damage):
	energy = planet_energy - damage
	return energy




def fight(roster_one,roster_two):
	attack_multiplier = { 'mercury' : { 'mercury': 1, 'venus': 2 , 'earth': 1 , 'mars': 0.5},
							'venus': { 'mercury': 0.5, 'venus': 1 , 'earth': 2 , 'mars': 1},
							'earth': {'mercury': 1, 'venus':  0.5, 'earth': 1 , 'mars': 2},
							'mars': {'mercury': 2, 'venus': 1 , 'earth': 0.5 , 'mars': 1}}

	planet_one = roster_one[0]
	planet_one_energy = roster_one[1]
	planet_one_power = roster_one[2]

	planet_two = roster_two[0]
	planet_two_energy = roster_two[1]
	planet_two_power = roster_two[2] 


	battle_status = True

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
				planet_two_energy = x
				if planet_two_energy == 0:
					return [planet_one_energy, True]
				# print('player_two_energy', planet_two_energy)
				player_choice = 2
			elif player_choice == 2:
				planet_one_energy = x
				if planet_one_energy == 0:
					return False
				# print('player_one_energy', planet_one_energy)
				player_choice = 1

		# if planet_one_energy == 0  and planet_two_energy == 0:
		# 	battle_status == False
		# 	print(planet_one_energy,planet_two_energy)








	# print(planet_two_energy,while_fight_energy_two,damage_by_planet_two,planet_two_power)




		




















print(spacemonSim([('Earth',100,10),('Earth',100,10)],[('Mercury',80,10),('Venus',80,10)]))