def cadastro():
    class Usuario:
        def __init__(self, nome, telefone):
            self.nome = nome
            self.telefone = telefone

    lista = []  # Cria a lista vazia para armazenar os usuários.

    while True:
        nome_cad = input("Digite o nome: ")
        telefone_cad = input("Digite o telefone: ")
        
        # Cria uma instância da classe Usuario
        usuario_cadastrado = Usuario(nome_cad, telefone_cad)
        
        # Adiciona o usuário à lista
        lista.append(usuario_cadastrado)
        
        # Pergunta se deseja adicionar outro usuário
        cont = input("Deseja adicionar mais? (S/N): ")
        
        if cont.lower() != "s":
            break  # Sai do loop se a resposta não for "S" ou "s"
    
    # Exibe os usuários cadastrados
    print("\nUsuários cadastrados:")
    for usuario in lista: 
        print(f"Nome: {usuario.nome}, Telefone: {usuario.telefone}")
    
    return lista  # Retorna a lista de usuários cadastrados para ser usada em outras funçoes

def coleta():
    lista = []
    quant_opcoes = int(input("Digite quantas opções do dia: "))
    for _ in range(quant_opcoes):
        opcao = input("Digite a opção: ")
        quant_complemento = int(input("Digite a quantidade de complementos: "))
        complementos = []
        for j in range(quant_complemento):
            complemento = input("Digite o complemento: ")
            complementos.append(complemento)
        lista.append((opcao, complementos))
    return lista

def exibir(lista):
   
    print("Opções disponíveis:")
    for cont, (opcao, complementos) in enumerate(lista, 1):
        print(f"{cont}. {opcao} - Complementos: {complementos}")
    
    opcao_escolhida = int(input("Selecione uma opção: "))
    if 1 <= opcao_escolhida <= len(lista):
        opcao_selecionada = lista[opcao_escolhida - 1]
        print(f"Você escolheu a opção: {opcao_selecionada[0]}")
        print(f"Complementos: {', '.join(opcao_selecionada[1])}")
    else:
        print("Opção inválida!")

def main():
    print("---------Enviar opções para cliente----------\n")
    lista_coleta = coleta()  # Lista de opções coletadas \as funções que não tem argumentos tenho que designar a uma variável
    print("---------Cadastro Cliente------------\n")
    lista_usuarios = cadastro()  # Lista de usuários cadastrados \as funções que não tem argumentos tenho que designar a uma variável
    print("---------Cardápio do dia-------------\n")
    exibir(lista_coleta)  # Exibe as opções coletadas

main()
