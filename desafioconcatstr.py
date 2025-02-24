
def gcdOfStrings():
    str1="ABABAB"
    str2="ABAB"
    s_new=""
    for i in range(len(str1)):
        if str1[i:i+len(str2)]==str2:
                s_new+= str2
    print(s_new)    
gcdOfStrings()