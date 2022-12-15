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
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    


testCircularQueue = CircularQueue(3)







