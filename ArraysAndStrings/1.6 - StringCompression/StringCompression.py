def compress(word):
    count = 0
    new = ""
    prev = ""
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
        return (st)
    else:
        return (new)


def main(): 
    print(compress("AAaaBBbbCCccdddddddd"))

if __name__ == "__main__":
    main()