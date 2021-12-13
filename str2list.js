// • str2list(‘[abc]’) should return [‘a’,‘b’,‘c’].
// • str2list(‘[a[bc]]’) should return [‘a’,[‘b’,‘c’]].


function str2list(l) {

	stack = [[]];
}
	for (i in l) {
		if (i == '[') {
			stack[-1].push([]);
			stack.push(stack[-1][-1]);
			console.log(stack);
		} else if (i == ']') {
			stack.pop();
			if (!stack) {


		} else {
			stack[-1].push(i);
			}

	stack = stack.pop();
		}
	return stack[0];
	}

console.log(str2list('[a[bc]]'));
