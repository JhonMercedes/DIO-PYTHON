menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[s] Fim/Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0

LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do dep�sito: "))

        if valor > 0:
            saldo += valor
            extrato += f"       Dep�sito: R$ {valor:.2f}\n"

        else:
            print("Opera��o falhou! O valor informado � inv�lido.")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeuSaldo = valor > saldo
        excedeuLimite = valor > limite
        excedeuSaques = numeroSaques >= LIMITE_SAQUES

        if excedeuSaldo:
            print("Opera��o falou! Voc� n�o tem saldo suficiente.")

        elif excedeuLimite:
            print("Opera��o falou! O valor do saque excedeu o limite.")

        elif excedeuSaques:
            print("Opera��o falou! N�mero m�ximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"       Saque: R$ {valor:.2f}\n"
            numeroSaques += 1

        else:
            print("Opera��o falhou! O valor informado � inv�lido.")

    elif opcao == "e":
        print("\n=============EXTRATO===============")
        print("N�o foram realizadas movimenta��es." if not extrato else extrato)
        print(f"\n       Saldo: R$ {saldo:.2f}")
        print("*************************************")

    elif opcao == "s":
        break

    else:
        print("Opera��o inv�lida, por favor selecione corretamnete a op��o desejada.")