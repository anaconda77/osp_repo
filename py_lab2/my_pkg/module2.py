#!/usr/bin/python

def union_and_intersection_of_integers():
	
	arr1 = []
	arr2 = []
	
	str1 = str(input("1st list: "))
 	str1.split("[")
	str1.split(",")
	str1.split(" ")
	str1.split("]")
	
	for i in range(0,len(str1)): 
		if(str1[i] == "[") or (str1[i] == "]") or (str1[i] == ",") or (str1[i] == " "):			continue
		num = int(str1[i])	
		arr1.append(num)

	
	str2 = str(input("2nd list: "))
 	str2.split("[")
	str2.split(",")
	str2.split(" ")
	str2.split("]")
	
	for i in range(0,len(str2)): 
		if(str2[i] == "[") or (str2[i] == "]") or (str2[i] == ",") or (str2[i] == " "):			continue
		num2 = int(str2[i])	
		arr2.append(num2)
	
	b1 = list(set(arr1) | set(arr2))
	print("union")
	print(b1)

	b2 = list(set(arr1) & set(arr2))
	print("intersection")
	print(b2)


	 
