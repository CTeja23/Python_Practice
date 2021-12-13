function str2list(l) {

	
	old_arr = new Array()

	for(var i = 0; i<l.length;i++){
		if(l[i]=='['){
			new_arr = new Array()
			new_arr.push(new_arr)
		}
		else if(l[i]==']'){
			new_arr.pop()
		}
		else{
			new_arr.push(l[i])
			old_arr.push(new_arr)
		}
	}


	old_arr.pop()
	var sh = String(old_arr.shift())
	old_arr.unshift(sh)

	console.log(old_arr)
	




}

console.log(str2list("[a[bc]]"));































