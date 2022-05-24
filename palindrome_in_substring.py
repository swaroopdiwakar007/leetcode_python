s = input()
res = ''
for i in range(len(s)):
    l = i - 1
    r = i + 1
    pal = s[i]
    while l>=0 and r<len(s) and s[l]==s[r]:
        pal = s[l] + pal + s[r]
        l -= 1
        r += 1
    # res = max(pal, res)
    # dict1[pal] = len(pal)
    l = i 
    r = i + 1
    pal = s[i]
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l == 1:
            pal = pal + s[r]
        else:
            pal = s[l] + pal + s[r]
        l -= 1
        r += 1
    # dict1[pal] = len(pal)
    res = pal if len(pal) > len(res) else res
print(res)
