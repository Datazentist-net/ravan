# key, value
# hash function input transform integer by using ascii
# Collection of chars --- ASCII 128 chars / Internationatization UTF-8 , 16,32, EBCIDC
#  
s = "b" # 65 66 ----- 97 
st = "INFORMIX"

value1 = "cat" # 312 Indrajith
value2 = "dog" # 314 Pallavi
value3 = "act" # 312 Kajan


# Indrajith
sumValue1 = 0
for charStr in value1:
    sumValue1 = sumValue1 + ord(charStr)
print(value1 + "'s ASCII Value is " + str(sumValue1))


for ch in value1:
    print (ch)

# Repetition take the one char from the string and get the ascii value sum it until reach the last char
