from time import sleep

print("Calculo da Área do Quadrado")
lado = float(input("Digite o comprimento do lado do quadrado: "))
opcao = 0

while opcao != 3:
    print("[1]Calcular")
    print("[2]Novos valores")
    print("[3]Sair do programa")
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        area = lado * lado
        print("A área do quadrado é {}".format(area))
        print("O dobro da mesma área é {}".format(area*area))
    elif opcao == 2:
        print("Informe os valores novamente")
        lado = float(input("Digite o comprimento do lado do quadrado: "))
    elif opcao == 3:
        print("Finalizando...")

    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
print("Fim do programa")












