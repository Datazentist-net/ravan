# insert - Insert on tail, Insert on Head, Insert Anywhere  :- Indrajith
# delete - Delete on tail, Delete on Head, Delete Anywhere  :- Pallavi
# display - Front to Back, Back to Front                    :- Kajan
class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

def insertNodeInTail(tailNode,newNode):
    tailNode.next = newNode
    newNode.prev = tailNode
# Problem????
def insertNodeInFront(headNode,newNode):
    headNode.prev = newNode
    newNode.next = headNode # assigning the headnode to the prev
    

def insertNodeInAPerticularLocation(location,headNode,newNode):
    count = 0
    while headNode != None:
        count = count + 1
        if(count == location):
            newNode.next = headNode.next
            newNode.prev = headNode
            break
        headNode = headNode.next
    
    if(count<location):
        print("Location is not Available", end=" ")

linked_list = LinkedList()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n5 = Node(4)

insertNodeInTail(n1,n2)
insertNodeInTail(n2,n3)
insertNodeInTail(n3,n5)

n4 = Node(64)

insertNodeInFront(n1,n4)

while n1 != None:
    print(n1.item, end=" ")
    n1 = n1.next