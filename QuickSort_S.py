#-*- coding: utf-8 -*-

'''
간단한 퀵정렬, pivot을 중위값으로 했다.
재귀 에서 메모리가 동적으로 생성 된다..
pivot이 계속 맨 가장자리에 생기면 
N 제곱의 시간 복잡도를 가진다.
가장 이상적인것은 pivot이 리스트의 정중앙을
가르키게 하는것이다.
'''

def quicksort(x):
	if len(x) <= 1:            # 재귀에서 빠져나가기 위한 조건
		return x
		
	pivot = x[len(x) // 2]
	less = []
	more = []
	equal = []
	
	for a in x:
		if a > pivot:
			more.append(a)
		elif a < pivot:
			less.append(a)
		else:
			equal.append(a)

	return quicksort(less) + equal + quicksort(more)
