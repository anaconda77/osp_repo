#!/usr/bin/python
import sys

cnt = int(input("How many numbers?: "))
mysum = 0

for i in range(0,cnt):
	num = int(input("number : "))
	mysum +=num

aver = mysum/cnt
print("average is %d" %aver)
