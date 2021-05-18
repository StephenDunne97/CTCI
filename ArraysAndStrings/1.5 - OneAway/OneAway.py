def replace(string1, string2):
    diff = False
    i=0
    while i<len(string1):
        if string1[i] != string2[i]:
            if diff == True:
                return False
            else:
                diff = True
        i+=1
    return True
    

def insert(string1, string2):
    i = 0 # index for string 1
    j = 0 # index for string 2
    while j < len(string2) and i < len(string1):
        if string1[i] != string2[j]: # If the smaller string i is not equal to longer string j, increment longer unless already done, in which case, return False
            if i != j:
                return False
            j+=1
        else:
            i+=1
            j+=1
    return True 


s1 = "apple"
s2 = "appless"
cond = True
if len(s1) == len(s2): # If s1 & s2 are the same length
    cond = replace(s1,s2) 
elif len(s1)+1 == len(s2): # If s1 is 1 smaller than s2. 
    cond = insert(s1,s2) # Smaller string is sent first. Ensures the longer string's index increments by 1 instead of the shorter string.
elif len(s1)-1 == len(s2): # If s1 is 1 bigger than s2.
    cond = replace(s2,s1) # Smaller string is sent first.Ensures the longer string's index increments by 1 instead of the shorter string.
else: # If s1 & s2 are not the same length, or 1 bigger/smaller than one another
    cond = False

if cond==True: 
    print("True")
else:
    print("False")