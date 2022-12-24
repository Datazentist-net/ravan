# key, value
# hash function input transform integer by using ascii
# Collection of chars --- ASCII 128 chars / Internationatization UTF-8 , 16,32, EBCIDC
#  
s = "b" # 65 66 ----- 97 
st = "INFORMIX"
key_list = []

value1 = "cat" # 312 Indrajith
value2 = "dog" # 314 Pallavi
value3 = "act" # 312 Kajan


# define the hash function to generate the hashed value for a key

def hash(value):
    ascii_result = 0
    for ch in value:
        ascii_result += ord(ch)
    return ascii_result

# Please note take the array length as 4 for this sample only
# Get the value, genearate the key from returning ascii value and using array length 

#def key_value_place(value):



print(hash(value1))
print(hash(value2))
print(hash(value3))





# Indrajith
sumValue1 = 0 # initialise 
# 1st time = 99
 #      sumvalue = 0 + 99
#2nd time
# sumvalue = 196
# 3rd Time
# 196 + 116 = 312

for charStr in value1:
    sumValue1  +=  ord(charStr)
print(value1 + "'s ASCII Value is " + str(sumValue1))


# Repetition take the one char from the string and get the ascii value sum it until reach the last char
