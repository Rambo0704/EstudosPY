def calcsal(salariobrut):
    ir = salariobrut*(11/100)
    inss = salariobrut*(8/100)
    sind = salariobrut*(5/100)
    salarioliq = salariobrut - (ir+inss+sind)
    print(f"+ Salário Bruto: R${salariobrut}")
    print(f"- IR: R${ir}")
    print(f"- INSS: R${inss}")
    print(f"- Sindicato: R${sind}")
    print(f"= Salário Liquido: R${salarioliq}")
def main():
    valor =int(input("Digite o valor que voce ganha por hora: "))
    horas =int(input("Digite as horas trabalhadas por mes: "))
    sal = valor*horas
    calcsal(sal)
main()