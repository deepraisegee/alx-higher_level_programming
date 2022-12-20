#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	"""
	prints x elements of a list
	"""
	count = 1
	for i in range(x):
		try:
			print(my_list[i], end="")
			count += i
		except IndexError:
			break

	return count
		
