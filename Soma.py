from time import sleep

print("Calculo para Somar")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = 0

while opcao != 3:
    print("[1]Calcular")
    print("[2]Novos números")
    print("[3]Sair do programa")
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        soma = num1 + num2
        print("A soma entre {} e {} é {}".format(num1, num2, soma))
    elif opcao == 2:
        print("Informe os valores novamente")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    elif opcao == 3:
        print("Finalizando...")
    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
        
print("Fim do programa")






