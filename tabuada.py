def cardapio():
    cardapio=[{"Cachorro quente":float(1.20)},{"Bauru Simples":float(1.30)},{"Hamburguer":float(1.50)}]
    for i in range(len(cardapio)):
        print(f"Numero:{i}{cardapio[i].keys()} R${cardapio[i].values()}")
cardapio()