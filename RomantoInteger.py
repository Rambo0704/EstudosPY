def main():
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = "III"
    result = 0
    anterior = 0
    for char in reversed(s):
        value = roman[char]
        if value < anterior:
            result -= value
        else:
            result += value
        anterior = value
    print(result)

main()