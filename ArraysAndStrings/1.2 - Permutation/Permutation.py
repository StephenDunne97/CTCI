s1 = "abc"
s2 = "baa"
s1_srt = sorted(s1)
s2_srt = sorted(s2)
perm = True
i = 0

while i < len(s2):
    if s1_srt[i] != s2_srt[i]:
        perm = False
    i += 1

if perm == False:
    print ("Not permutation")
else:
    print("Permutation")