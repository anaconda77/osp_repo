#!/usr/bin/python
import sys

def Fibo(num):
	arr = []

	for i in range(0,num):
		if(i==0) or (i==1):
			arr.append(1)
		else:
			arr.append(arr[i-1] + arr[i-2])

	print(arr)
	print("F%d = %d" %(num, arr[num-1]))


num = int(input("What's number ?: "))
Fibo(num)
