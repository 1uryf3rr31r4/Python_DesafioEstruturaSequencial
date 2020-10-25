from time import sleep

print("Tranformar Temperatura Celsius em Farenheit")
C = float(input("Digite o valor da temperatura em Celsius: "))
opcao = 0

while opcao != 3:
    print("[1]Calcular")
    print("[2]Novos valores de temperatura")
    print("[3]Sair do programa")
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        F = 1.8*(C+32)
        print("{} graus em Celsius equivale a {} graus em Farenheit".format(C,F))
    elif opcao == 2:
        print("Informe os valores novamente")
        C = float(input("Digite o valor da temperatura em Celsius: "))
    elif opcao == 3:
        print("Finalizando...")
    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
print("Fim do programa")












