def isUnique(word):
    for x in word:
        count = 0
        for y in word:
            if x == y:
                count = count + 1
                if count > 1: 
                    print(word + " is not unique.")
                    return False
    print (word + " is unique.")
    return True

def main():
    isUnique("step")
    isUnique("stepe")

if __name__ == "__main__":
    main()