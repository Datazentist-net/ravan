class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0,item)
        print(self.items)

print ("creating and object")
odj = Deque()
print (odj.add_front(1))