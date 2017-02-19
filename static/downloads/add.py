#! usr/bin/env python

import string, time

print("This program adds numbers. Type in numbers in the form: a,b. Thanks.")
while True:
	try:
		numstr = input("Input: ")
	except Exception as inst:
		numstr=None
		print("It seems you didn't type in the correct form.")
		continue
	if type(numstr) is not tuple:
		print("It seems you didn't type in the correct form.")
	elif type(numstr) is tuple:
		numls = list(numstr)
		if len(numls) == 2:
			sum = numls[0]+numls[1]
			print("Calculating...")
			time.sleep(1)
			print "...And the solution is:", sum
			break
		else:
			print("It seems you didn't type in the correct form.")
