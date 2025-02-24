
def senha():
    print("-----CADASTRO-----")
    cad = input("Digite a Senha para Cadastro: ")
    cont = 2
    while cont >=0:
        print("-----LOGIN-----")
        senha = input("Digite a senha de login: ")
        if senha==cad:
         print("Senha correta")
         break
        else:
            print(f"Senha incorreta\nVoce tem mais {cont} tentativas!!")
            cont-=1
senha()