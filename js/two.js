function RPS(play){


	let opp_values = new Map([['R', 'P'],['P', "S"],['S','R']
]);
	var computer_output = "";

	for(var i=0; i<=play.length;i++){
		for(const [key,value] of opp_values.entries()){
			if(play[i]==key){
				computer_output += value;
			}
		}

		
	}
	 return computer_output
}



console.log(RPS('PSR'))

