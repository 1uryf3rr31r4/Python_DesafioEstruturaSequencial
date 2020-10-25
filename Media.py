from time import sleep

print("Calculo para Média de Notas")

nota1 = float(input("Digite o primeiro nota bimestral: "))
nota2 = float(input("Digite o segundo nota bimestral: "))
nota3 = float(input("Digite o terceita nota bimestral: "))
nota4 = float(input("Digite o quarta nota bimestral: "))
opcao = 0

while opcao != 3:
    print("[1]Calcular")
    print("[2]Novas Notas")
    print("[3]Sair do programa")
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        media = (nota1 + nota2 + nota3 + nota4)/4
        print("A média entre as notas é {}".format(media))
    elif opcao == 2:
        print("Informe as notas novamente")
        nota1 = float(input("Digite o primeiro nota bimestral: "))
        nota2 = float(input("Digite o segundo nota bimestral: "))
        nota3 = float(input("Digite o terceita nota bimestral: "))
        nota4 = float(input("Digite o quarta nota bimestral: "))
    elif opcao == 3:
        print("Finalizando...")
    else:
        print("Opção Inválida. Tente Novamente")

    print("=-="*10)
    sleep(1)
        
print("Fim do programa")











