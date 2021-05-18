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
    i = 0
    j = 0
    while j < len(string2) and i < len(string1):
        if string1[i] != string2[j]:
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
if len(s1) == len(s2):
    cond = replace(s1,s2)
elif len(s1)+1 == len(s2):
    cond = insert(s1,s2)
elif len(s1)-1 == len(s2):
    cond = replace(s2,s1)
else:
    cond = False

if cond==True:
    print("True")
else:
    print("False")