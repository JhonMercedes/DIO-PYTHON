menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Fim/Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0

LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"       Deposito: R$ {valor:.2f}\n"

        else:
            print("Operacao falhou! O valor informado e invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeuSaldo = valor > saldo
        excedeuLimite = valor > limite
        excedeuSaques = numeroSaques >= LIMITE_SAQUES

        if excedeuSaldo:
            print("Operacao falou! Voce nao tem saldo suficiente.")

        elif excedeuLimite:
            print("Operacao falou! O valor do saque excedeu o limite.")

        elif excedeuSaques:
            print("Operacao falou! Numero maximo de saques excedido [3 Saques Diarios].")

        elif valor > 0:
            saldo -= valor
            extrato += f"       Saque: R$ {valor:.2f}\n"
            numeroSaques += 1

        else:
            print("Operacao falhou! O valor informado e invalido.")

    elif opcao == "e":
        print("\n=============EXTRATO===============")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\n       Saldo: R$ {saldo:.2f}")
        print(f"\n       Quantidade de saques diarios: {numeroSaques}")
        print("*************************************")

    elif opcao == "q":
        break

    else:
        print("Operacao invalida, por favor selecione corretamnete a opcao desejada.")