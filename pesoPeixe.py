from time import sleep

pesoPeixe = float(input("Digite o peso do peixe pescado: "))
opcao = 0

while opcao != 3:

    print("[1] Calcular")
    print("[2] Novo número")
    print("[1] Sair do programa")
    opcao = int(input("Qual é a opção: "))
                
    if opcao == 1:
        pesoExcesso = 0
        if pesoPeixe > 50:
            pesoExcesso = pesoPeixe - 50
        multa = 4 * pesoExcesso
        print("Peso do peixe pescado é {}kg ".format(pesoPeixe))
        print("Peso do peixe excedido é {}kg ".format(pesoExcesso))
        print("Valor da multa pelo peso de pesca excedido é de R$ {}".format(multa))
                
    elif opcao == 2:
        pesoPeixe = float(input("Digite o peso do peixe pescado: "))

    elif opcao == 3:
        print("Finalizando...")

    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
print("Fim do programa")
