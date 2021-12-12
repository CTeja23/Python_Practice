function toString(l){

	var string = ""


	for(var i = 0;i<l.length;i++){
		if(Array.isArray(l[i]) == true){
			string += '['+(toString(l[i]))+']';
		}
		else{
			string += String(l[i]);

		}
	}

	 return string;

}

function driveMotor(l){

        var s = toString(l);
        return '['+s+']';

}






console.log(driveMotor(["a",["b","c"]]))




// def get_strings(l):
// 	string = ""
// 	for i in l:
// 		if type(i) is list:
// 			string += '['+str(get_strings(i))+']'
// 		else:
// 			string += str(i)
	
// 	return string


// def list2str(l):
// 	s = get_strings(l)
// 	return '['+s+']'



// print(list2str(['a',['b',['c',['d']]]]))