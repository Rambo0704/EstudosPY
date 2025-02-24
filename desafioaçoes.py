def main():
    preco = [7, 1, 5, 3, 6, 4]
    comp = preco[0]
    lucro_max = 0

    for i in range(1, len(preco)):
        if preco[i] < comp:
            comp = preco[i]
        elif preco[i] > comp:
            lucro = preco[i] - comp
            if lucro > lucro_max:
                lucro_max = lucro

    print(lucro_max)

main()
