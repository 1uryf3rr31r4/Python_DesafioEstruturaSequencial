from time import sleep
print("Custos com Impostos")

ganhoHora = float(input("Digite o valor de ganho por hora: "))
horaMes = float(input("Digite o número de horas trabalhadas: "))
opcao = 0

while opcao != 3:
    print("[1]Calcular")
    print("[2]Novos valores")
    print("[3]Sair do programa")
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        salarioBruto = ganhoHora * horaMes
        ir = salarioBruto * 0.11
        inss = salarioBruto * 0.08
        sindicato = salarioBruto * 0.05
        salarioLiq = salarioBruto - ir - inss - sindicato
        print("+ Salário Bruto : R$ {}".format(salarioBruto))
        print("- IR (11%) : R$ {}".format(ir))
        print("- INSS (8%) : R$ {}".format(inss))
        print("-Sindicato (5%) : R$ {}".format(sindicato))
        print("O Salário L´quido : R$ {} ".format(salarioLiq))
        
    elif opcao == 2:
        print("Informe os valores novamente")
        ganhoHora = float(input("Digite o valor de ganho por hora: "))
        horaMes = float(input("Digite o número de horas trabalhadas: "))
    elif opcao == 3:
        print("Finalizando...")

    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
print("Fim do programa")
