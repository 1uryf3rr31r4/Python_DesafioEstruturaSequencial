from time import sleep

print("Tempo de Download")

arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
vLink = float(input("Digite a velocidade de um link de Internet (em Mbps): "))
opcao = 0

print("[1]Calcular")
print("[2]Novos números")
print("[#]Sair do programa")

while opcao != 3:

    if opcao == 1:
        convertMBit = arquivo * 8
        tSeg = convertMBit / vLink
        tMin = tSeg / 60
        Hora = tMin / 60
        print("O tamanho do arquivo é de {} (em MegaByte)".format(arquivo))
        print("A velocidade do link de Internet é de {} (em Mbps)".format(vLink))
        print("O tamanho do arquivo é de {} (em Megabit)".format(convertMBit))
        print("Tempo para concluir o download é de {} segundo(s)".format(round(tSeg,2)))
        print("Tempo para concluir o download é de {} minuto(s)".format(round(tMin,2)))
        print("Tempo para concluir o download é de {} hora(s)".format(round(tHora,2)))

    elif opcao == 2:
        print("Informar novamente")
        arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
        vLink = float(input("Digite a velocidade de um link de Internet (em Mbps): "))

    elif opcao == 3:
        print0("Saindo do programa...")

    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
print("Fim do programa")
