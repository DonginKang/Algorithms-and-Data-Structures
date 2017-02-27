# Linear Search

A = [1,4,2,3]

def solution(alist,item):
	found = False
	first = 0
	last = len(A)-1
	
	while first <= last and not found:
		if alist[first] == item:
			found = True
		else:
			first += 1
			
	return found
	
print solution(A,3)