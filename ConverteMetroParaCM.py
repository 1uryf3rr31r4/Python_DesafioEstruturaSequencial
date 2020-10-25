from time import sleep
print("Conversão de metros para centimetros")

m = float(input("Digite o comprimento em metros para converter: "))
opcao = 0

while opcao != 3:
    print("[1]Converter")
    print("[2]Novos números")
    print("[3]Sair do programa")
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        cm = m*100
        print("{} metro(s) equivale a {} centimetro(s)".format(m, cm))
    elif opcao == 2:
        print("Informe os valores novamente")
        m = float(input("Digite o comprimento em metros para converter: "))
    elif opcao == 3:
        print("Finalizando...")

    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(2)
print("Fim do programa")


