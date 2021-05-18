s = "Hello World I am Stephen"
r = "%20"
i = 0
for x in s:    
    if x == " ":
        n = s[0:i] + r + s[i+1:]
        print(n)
    i+=1

# Python solution:
s = s.replace(" ","%20")
print (s)