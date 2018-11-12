#!/usr/bin/env python3

import operator
import math

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
    '//': operator.floordiv
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
	    if token == 'h':
		print(history)
	    else:
		function = operators[token]
		if token == '!':
		    arg = stack.pop()
		    result = function(arg)
		    history = "{}{} = {}".format(arg, token, result)
		else:
            	    arg2 = stack.pop()
            	    arg1 = stack.pop()
		    if token == '/' and arg2 == 0:
                        return "Divide by zero error"
		    result = function(arg1, arg2)
		    history = "{} {} {} = {}".format(arg1, token, arg2, result)
            stack.append(result)
        #print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()


history = ""

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
