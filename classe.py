class Cliente:
    def dados(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def aparencia(self,altura,peso):
        self.altura = altura
        self.peso = peso
def main():
    c1 = Cliente()
    c1.dados("Maria",25)
    c1.aparencia(1.70,60)
    print(c1.nome,c1.idade,c1.altura,c1.peso)
main()