menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[a] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação não realizada! O valor do saqe excede o limite.")

        elif excedeu_saques:
            print("Operação não realizada! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada! O valor informado é inválido")

    elif opcao == "e":
        print("\n----------------Extrato----------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R& {saldo:.2f}")
        print("---------------------------------------")

    elif opcao == "a":
        print("Até logo!")
        break

    else:
        print ("Operação invalida, por favor selecione novamente a operação desejada.")