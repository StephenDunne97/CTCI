count = 0
new = ""
prev = ""
word = "AAaaBBbbCCccdddddddd"
st = sorted(word)

for x in st:
    count = 0
    if x == prev:
        continue
    else:
        for y in st:
            if x == y:
                count += 1
                
    new = new + x + str(count)
    prev = x

if len(new) >= len(st):
    print(st)
else:
    print(new)
