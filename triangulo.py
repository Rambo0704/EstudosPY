def main():
    tam = int(input("Digite o tamanho do triângulo: "))
    for i in range(tam):
        if i == 0 or i == tam - 1:
            print("*" * (i+1))
        else:
            print("*" + " " * (i - 1) + "*")
        
main()