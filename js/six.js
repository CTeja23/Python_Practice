function CSVsum(filename){

	const fs = require('fs');
 	let csv = fs.readFileSync(filename, 'utf8');

 	csv = csv.split('\n');
 	var list = []
	for(var i = 0 ; i<csv.length;i++){
		list.push(csv[i].split(','))
	}


	for(var i = 0;i<list.length; i++){
		if(list[i].length == 1 || list[i].length == 0){
			list.pop()
		} 
	}

	var data = list.slice(1,)
	console.log('data',data)

	total = 0
	output = []

	for(row = 0;row<data[0].length;row++){
		for(col = 0;col<data.length;col++){
			total += parseFloat(data[col][row])
		}
		output.push(total)
		total = 0
	}


	return output


	
}	










console.log(CSVsum('table2.csv'))
