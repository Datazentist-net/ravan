# Insert methods possibly: insert_last, insert_first, insert_anywhere
# Remove methods 
# Possible check conditions 
# Everyone commit the part of the code to the repo /  Before 28/12 
class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None # doubly linked list structure

class DoublyLinkedList:

    def __init__(self):
        self.head = None # None means null in java
        self.prev = None

#
def connect_next_node(node1, node2):
    node1.next = node2

# Connect the node1 as a previous node for node2
def connect_prev_node(node1, node2):
    node2.prev = node1


def print_list(node):
    while node != None:
        print(node.item, end=" ")
        node = node.next


linked_list = DoublyLinkedList() # student s1 = new student() - in java

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

connect_next_node(n1, n2)
connect_next_node(n2, n3)
connect_prev_node(n1, n2)

print('+++++++++++++++++ on the Node 2 +++++++++++++++++++++')
print(n2.prev.item) # Explanation purpose only
print('+++++++++++++++++ on the Node 2 +++++++++++++++++++++')

print_list(n1)


