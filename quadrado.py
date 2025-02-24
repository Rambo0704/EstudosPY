def main():
    tamanho = int(input("Digite o tamnho do quadrado:\n"))
    for i in range(tamanho):
        if i == 0 or i == tamanho - 1:
         print("*" * tamanho)
        else :
            print("*"+" "*(tamanho - 2)+"*")
def quad():        
    x = int(input("Digite o eixo X: "))
    y = int(input("Digite o eixo Y: "))
    for i in range(y):
        if i == 0 or i == y - 1:
            print("*" * x)
        else:
            print("*" + " " * (x - 2) + "*")
quad()