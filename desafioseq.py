def main():
    t = "abchedf"
    s = "abc"
    i,j = 0,0
    while i < len(t) and j < len(s):
        if t[i] == s[j]:
            j += 1
        i += 1
    print(j == len(s))
main()