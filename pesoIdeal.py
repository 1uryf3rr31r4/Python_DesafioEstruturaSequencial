from time import sleep

print("Calcular o Peso Ideal")
h = float(input("Digite a sua altura: "))
opcao = 0

while opcao != 4:
    print("[1] Calcular peso ideal para homens")
    print("[2] Calcular peso ideal para mulheres")
    print("[3] Nova altura")
    print("[4] Sair do programa")
    opcao = int(input("Qual é a opção: "))

    if opcao == 1:
        pesoMIdeal = (72.7 * h) - 58
        print("O peso ideal para homens com {}m de altura é de {}kg".format(h,pesoMIdeal))
        
    elif opcao == 2:
        pesoFIdeal = (62.1 * h) - 44.7
        print("O peso ideal para mulheres com {}m de altura é de {}kg".format(h,pesoFIdeal))

    elif opcao == 3:
        h = float(input("Digite a sua altura: "))
        
    elif opcao == 4:
        print("Finalizando...")
        
    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
print("Fim do programa")

        




