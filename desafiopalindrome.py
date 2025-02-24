def main():
    x = list(str(121))
    num = []
    i = len(x)
    while i > 0:
        num.append(x[i])
        i -= 1
    if x == num:
        return True
    else:
        return False
main()