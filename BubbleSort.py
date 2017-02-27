#-*- coding: utf-8 -*-

x = [5,4,3,2,1]

# 버블 고리로 제일 큰거 뒤로 보내고 제일 큰거 뒤에 생겼으면 그거 빼고 다시 하는거구나.. 

def bubbleSort(x):
	length = len(x)-1
	for i in range(length):
		for j in range(length-i):  # length - i 중요
			if x[j] > x[j+1]:
				x[j], x[j+1] = x[j+1], x[j]
	return x
	

print bubbleSort(x)