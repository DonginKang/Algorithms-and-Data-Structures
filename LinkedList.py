class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
		
		
temp1 = Node(93)
temp2 = Node(92)
temp3 = Node(91)
print temp1.getData()
temp1.setNext(temp2)
print temp1.getNext()
temp3.setNext(temp2)
print temp3.getNext()

