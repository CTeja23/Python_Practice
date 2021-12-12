function isGreaterThan(dict1,dict2){





	var similar_key_dict1 = new Object();
	var similar_key_dict2 = new Object();

	for(var key_1 in dict1){
		for(var key_2 in dict2){
			if(key_1 == key_2){
				similar_key_dict1[key_1] = dict1[key_1]
				similar_key_dict2[key_2] = dict2[key_2]
			}
		}
	}


	

	status = false
	for(var key_1 in similar_key_dict1){
		for(var key_2 in similar_key_dict2){
			if(similar_key_dict1[key_1] > similar_key_dict2[key_2]){
				status = true
			}
			else{
				status = false
			}
		}
	}

	return status



}





console.log(isGreaterThan({'a':1,'b':2},{'a':1,'b':1}))