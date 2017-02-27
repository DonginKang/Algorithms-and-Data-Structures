#-*- coding: utf-8 -*-

# Binary Search

'''
이미 정렬 되어 있다는걸 숙지
재귀 함수를 이용하는 방법
'''
def binarySearch(alist, item): 
    if len(alist) == 0: 
        return False 
    else: 
        midpoint = len(alist)//2 # // = 몫 반환 하는 연산자
        if alist[midpoint]==item: 
          return True 
        else: 
          if item<alist[midpoint]: 
            return binarySearch(alist[:midpoint],item) # len(alist[:0]) = 0 
          else: 
            return binarySearch(alist[midpoint+1:],item) 
  
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,] 
print(binarySearch(testlist, 3)) # return False
print(binarySearch(testlist, 13)) # return True
