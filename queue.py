# Create the class for Queue -- FIFO
# Properties: front, rear, size - dynamic  
# methods: enque, deque, isFull, isEmpty
# Update the scractch book -- Highlight the References/ 
# project management - poker planning Features/Issues
#  - enque -   
#  - Channel - VSCode - discord/ Slack Update/ 
#  - Github - code push
#     - common code line --- merge conflicts 
# pipeline 
# Main - dev-rav-enque   dev-ind-deque --dev envir
# 
#  class --- instance -- Object ---  
# #

class CircularQueue():
    # its a initializer aka constrcutor
    def __init__(self, k):
        #print('initiated with size ', str(k))
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full You cannot add anymore data\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
    
    def isFull(self):
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")
        else:
            print("Not Full\n")

    


testCircularQueue = CircularQueue(3)
testCircularQueue.enqueue(5)
testCircularQueue.isFull()
testCircularQueue.enqueue(4)
testCircularQueue.isFull()
testCircularQueue.enqueue(3)
testCircularQueue.isFull()
testCircularQueue.enqueue(2)
testCircularQueue.isFull()







