#-*- coding: utf-8 -*-

'''
�̹� ���� �Ǿ� �ִٴ°� ����
��� �Լ��� �̿��ϴ� ���
'''

A = [1,2,3,4,5,6,7,8,9]

def BinarySearch(alist,key,left,right):
	if (right-left) < 0:
		return False
		
	middle = (left+right) // 2
	
	if (alist[middle] == key):
		return True
	elif (alist[middle] > key):
		return binarysearch(alist,key,left,middle-1) # ����Լ� �տ� return
	else:
		return binarysearch(alist,key,middle+1,right)
		

print binarysearch(A,6,0,len(A)-1)

