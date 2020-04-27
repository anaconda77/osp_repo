#!/usr/bin/python

def binary_to_others_conversion():

	decimal_number = 0
	bi_num = int(input("What's number ?: "))
	bi_num_str = str(bi_num)
	
	for i, digit in enumerate(bi_num_str):
		decimal_number += int(digit)*pow(2, len(bi_num_str)-1-i)
	
	o = oct(decimal_number)
	h = hex(decimal_number)		
	print("OCT>")	
	print(o)
	print("DEC>")
	print(decimal_number)
	print("HEX>")
	print(h)

