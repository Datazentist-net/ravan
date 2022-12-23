class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None # None means null in java

linked_list = LinkedList() # student s1 = new student() - in java

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

linked_list.head = n1
linked_list.head.next = n2

n2.next = n3

n4 = Node(12)
n5 = Node(25.8)
n6 = Node("Gowrees")
n7 = Node(7895.258)

n4.next = n5
n5.next = n6
n6.next = n7

n3.next = n4

while n1 != None:
    print(n1.item, end=" ")
    n1 = n1.next

