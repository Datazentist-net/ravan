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
        self.head = None # None means null in java