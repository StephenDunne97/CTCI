
def isUnique(word):
    unique = True
    for x in word:
        count = 0
        for y in word:
            if x == y:
                count = count + 1
                if count > 1: 
                    return False

    return True

st = "steph"
result = isUnique(st)

if result == False:
    print(st + " is not unique.")
else:
    print(st + " is unique.")
