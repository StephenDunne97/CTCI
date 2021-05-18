def PalindromePermutation(s1="Navan",s2="Navna"):
    s1_sorted = sorted(s1.lower())
    s2_sorted = sorted(s2.lower())
    i = 0

    if len(s1_sorted) != len(s2_sorted):
        return False
    else:
        while (i <len(s1)):
            if s1_sorted[i] != s2_sorted[i]:
                return False
            i+=1
        return True


perm = PalindromePermutation()
if perm == True:
    print("True")
else:
    print("False")