function textPreprocessing(text){

	    const p_words = ['.','?','!',':',';','-','[',']','{','}','(',')','’',',','"',];
   		const s_words = ['i', 'a', 'about', 'am', 'an', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'how', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the', 'this', 'to', 'was', 'what', 'when', 'where', 'who', 'will', 'with'];

   		var new_line = "";


   		for(var i=0;i<text.length;i++){
   			if(p_words.includes(text[i]) == false){

   				new_line += text[i];

   			}
   		}


   		var new_word_arr = new_line.split(' ');

   		var final_word_ls = [];

   		for(var i = 0; i<new_word_arr.length;i++){
   			word = new_word_arr[i].toLowerCase();
   			if(s_words.includes(word) == false){
   				final_word_ls.push(word);
   			}
   		}

   		var output = [];
   		for(var i = 0; i<final_word_ls.length;i++){
   			output_word = final_word_ls[i].toString();
   			if(output_word.endsWith('ing') == true){
   				var x = output_word.slice(0,-3);
   				output.push(x);

   			}
   			else if(output_word.endsWith('ed') == true){

   				var x = output_word.slice(0,-2);
   				output.push(x);
   			}
   			else if(output_word.endsWith('s') == true){
   				console.log('s',output_word)
   				var x = output_word.slice(0,-1);
   				output.push(x);

   			}
   			else{
   				output.push(output_word);

   			}
   		}



	return output

}







console.log(textPreprocessing("When life gives you lemons, make lemonade."))