from time import sleep

print("Tranformar Temperatura Farenheit em Celsius")
F = float(input("Digite o valor da temperatura em Farenheit: "))
opcao = 0

while opcao != 3:
    print("[1]Calcular")
    print("[2]Novos valores de temperatura")
    print("[3]Sair do programa")
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        C = (5 * (F-32) / 9)
        print("{} graus em Farenheit equivale a {} graus em Celsius".format(F,C))
    elif opcao == 2:
        print("Informe os valores novamente")
        F = float(input("Digite o valor da temperatura em Farenheit: "))
    elif opcao == 3:
        print("Finalizando...")
    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
print("Fim do programa")












