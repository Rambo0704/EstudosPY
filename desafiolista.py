def main():
    nomes=[]
    valores=[]
    while True:
        nome=input("Digite o nome: ")
        saldo=input("Digite o saldo: ")
        nomes.append(nome)
        valores.append(saldo)
        cont=input("Deseja adicionar mais(S/N) ")
        if cont == 'N':
            break
    print("LISTA DE CLIENTES-BANCO NACIONAL")
    for usuarios,valor in zip(nomes,valores): ## zip() junta duas listas
        print(f"Nome: {usuarios} Saldo: R${valor}") 
main()
        