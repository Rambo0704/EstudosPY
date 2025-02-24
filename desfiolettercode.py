def main():
    string="IceCream"
    vowels = "aeiouAEIOU"
    s_vowels = [char for char in string if char in vowels]
    s_new=""
    for char in string:
        if char in vowels:
            s_new += s_vowels.pop()
        else:
            s_new += char
    print(s_new)
main()