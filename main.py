# This application shows how to define stack data struture and basic operations

# Sequence -- Selection  -- Repetition 



# Decalre the stack

def create_stack():
    print(' Creating the stack...')
    stack = [] # declaring the empty array variable
    return stack 

# push

def push(stack, data):
    stack.append(data)
    print(stack, 'now pushed with ', data)


# pop

def pop(stack):
    if(isEmpty(stack)):
        print('Stack is already empty ')
    else:
        print('Poping the last element  ', stack)
        stack.pop()
        print('After removing the stack... ',stack)
   
        



# isEmpty will ensure that stack is isEmpty
def isEmpty(stack):
    return len(stack) == 0


# isFull

# peek

# Demo check

demoStack = create_stack()
push(demoStack, 1)
push(demoStack, 2)
pop(demoStack)
pop(demoStack)
pop(demoStack)

s = 'act'
val = 0
for c in s:
    val += ord(c)
print (val) 





