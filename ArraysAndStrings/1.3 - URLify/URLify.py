def urlify(s): # Long-form solution
    r = "%20"
    i = 0
    for x in s:    
        if x == " ":
            n = s[0:i] + r + s[i+1:]
            print(n)
        i+=1
        
def urlify_pythonic(s): # Same solution done pythonically
    s = s.replace(" ","%20")
    print (s)

def main():
    s = "Hello World I am Stephen"
    urlify(s)
    urlify_pythonic(s)

if __name__ == "__main__":
    main()
