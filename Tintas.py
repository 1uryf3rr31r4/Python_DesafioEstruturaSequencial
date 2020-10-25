from time import sleep
print("Loja de Tintas")

parede = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
opcao = 0

while opcao != 3:
    print("[1]Calcular")
    print("[2]Novos dados")
    print("[3]Sair do programa")
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        cobTinta = 3
        quantTinta = parede / cobTinta
        baldeTinta = quantTinta / 18
        galaoTinta = quantTinta / 3.6
        excedente = baldeTinta - int(baldeTinta)
        resto = excedente * 18

        if baldeTinta == int(baldeTinta):
            pBalde = baldeTinta * 80
            print("Será necessário {} baldes custando R$ {}".format(baldeTinta, pBalde))

        else:
            pBalde2 = (int(baldeTinta)+1) * 80
            print("Será necessário {} baldes custando R$ {}".format((int(baldeTinta)+1), pBalde2))

        if galaoTinta == int(galaoTinta):
            pGalao = galaoTinta * 25
            print("Será necessário {} galões custando R$ {}".format(galaoTinta, pGalao))

        else:
            pGalao2 = (int(galaoTinta)+1) * 25
            print("Será necessário {} galões custando R$ {}".format((int(galaoTinta)+1), pGalao2))

        galaoTinta2 = resto / 3.6
        pBalde3 = int(baldeTinta) * 80
        pGalao3 = galaoTinta2 * 25
        pMisturado = pBalde3 + pGalao3

        print("Será necessário {} baldes e {} galões custando R$ {}".format(int(baldeTinta), round(galaoTinta2), round(pMisturado)))

    elif opcao == 2:
        print("Informe os dados novamente")
        parede = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

    elif opcao == 3:
        print("Finalizando...")

    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
print("Fim do programa")
