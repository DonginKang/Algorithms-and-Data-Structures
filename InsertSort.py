#-*- coding: utf-8 -*-

'''
삽입 정렬
내가 처음 생각했던 가장 쉬운정렬

'''

x = [5,4,3,2,1]

def InsortSort(x):
	for i in range(len(x)):
		for j in range(i,len(x)):   # range(i,len(x))가 중요.
			if x[i] > x[j]:
				print i,j
				x[i],x[j] = x[j],x[i]
				
	return x
	
	

print InsortSort(x)


