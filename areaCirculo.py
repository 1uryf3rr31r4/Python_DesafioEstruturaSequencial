from time import sleep

print("Calculo da Área do Círculo")
raio = float(input("Digite o comprimento do raio: "))
opcao = 0

while opcao != 3:
    print("[1]Calcular")
    print("[2]Novos valores")
    print("[3]Sair do programa")
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        area = 3.14159 *(raio * raio)
        print("A área do círculo é {} ".format(area))
    elif opcao == 2:
        print("Informe os valores novamente")
        raio = float(input("Digite o comprimento do raio do círculo: "))
    elif opcao == 3:
        print("Finalizando...")

    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
print("Fim do programa")












