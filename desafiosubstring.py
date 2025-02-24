def main():
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    cont = 0
    for i in range(len(sequence)):
        if sequence[i:i+ len(word)] == word:
            cont += 1            
    print(cont)
def test():
    list = [1,2,3,4,5,6,7,8,9,10]
    print(list[0:5])
main()