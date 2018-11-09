#!/usr/bin/env python3

import operator

# https://docs.python.org/3/library/operator.html
# link to the operator functions

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    '!': math.factorial,
    '|': operator.xor,
    '&': operator.and_
    '~': operator.inv,
    '//': operator.floordiv,
}

def calculate(myarg):
    history = ""
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
	    if token == 'h':
		print(history)
	    else:
		if token == '~' || token == '!':
		    arg = stack.pop()
		    result = function(arg)
		    if token == '!':
			history = arg + token + "=" + result
		    else:
			history = token + arg  "=" + result
		else: 
            	    arg2 = stack.pop()
            	    arg1 = stack.pop()
            	    result = function(arg1, arg2)
		    history = arg + token + arg +  "=" + result
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
