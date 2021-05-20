def palindrome_permutation(s1="Navan",s2="Navna"):
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

def main():
    perm = palindrome_permutation("anna", "aann")
    not_perm = palindrome_permutation("anna", "annb")
    print(perm)
    print(not_perm)

if __name__ == "__main__":
    main()