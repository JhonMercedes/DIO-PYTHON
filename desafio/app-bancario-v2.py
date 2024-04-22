import textwrap

def menu():
    menu = """\n
     ======= MENU =======

         [d]\tDepositar
         [s]\tSacar
         [e]\tExtrato
         [nu]\tNovo Usu�rio
         [nc]\tNova Conta
         [lc]\tListar Contas
         [lu]\tListar Usu�rios
         [f]\tFim/Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Dep�sito:\tR$ {valor:.2f}\n"
        print("\n=== Dep�sito ralizado com sucesso! ===")
    else:
        print("\n### Oprea��o Falhou! - O Valor informado � inv�lido. ###")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeroSaques, limiteSaques):
    excedeuSaldo = valor > saldo
    excedeuLimite = valor > limite
    excedeuSaques = numeroSaques >= limiteSaques

    if excedeuSaldo:
        print("\n### Opera��o Falhou! - Voc� n�o possui saldo suficiente. ###")

    elif excedeuLimite:
        print("\n### Opera��o Falhou! - Voc� n�o possui limite de saque. ###")

    elif excedeuSaques:
        print("\n### Opera��o Falhou! - Numero de saques di�rios excedido. ###")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numeroSaques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n### Opera��o Falhou! - O valor informado � inv�lido. ###")

    return saldo, extrato

def exibirExtrato(saldo, /, *, extrato):
    print("\n======= Extrato ========")
    print("N�o form feitas movimenta��es." if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")
    print("===========================")

def criarUsuario(usuarios):
    cpf = input("Informe o CPF (somente n�meros): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n### J� existe usu�rio com esse CPF! ###")
        return
    
    nome = input("Informe o nome completo: ")
    dataNascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endere�o (logradouro, numero - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "dataNascimento": dataNascimento, "cpf": cpf, "endereco":endereco})
    print("=== Usu�rio criado com sucesso ===")

def filtrarUsuario(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None

def criarConta(agencia, numeroConta, usuarios):
    cpf = input("Informe o CPF do usu�rio: ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta Criada com Sucesso! ===")
        return {"agencia": agencia, "numeroConta": numeroConta, "usuario": usuario}
    
    print("\n### Usu�rio n�o encontrado, cadastrar usu�rio primeiro.")

def listarContas(contas):
    for conta in contas:
        linha = f"""\
        Ag�ncia:\t{conta['agencia']}
        C/C:\t\t{conta['numeroConta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def listarUsuarios(usuarios):
    for usuario in usuarios:
        linha1 = f"""
        Usu�rio:\t{usuario['nome']} \t CPF:\t{usuario['cpf']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha1))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numeroSaques = 0
    usuarios = []
    contas = []
    numeroConta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do dep�sito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeroSaques=numeroSaques,
                limiteSaques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibirExtrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criarUsuario(usuarios)

        elif opcao == "nc":
            conta = criarConta(AGENCIA, numeroConta, usuarios)
            if conta:
                contas.append(conta)
                numeroConta += 1

        elif opcao == "lc":
            listarContas(contas)

        elif opcao == "lu":
            listarUsuarios(usuarios)

        elif opcao == "f":
            break

        else:
            print("Opera��o falhou! O valor informado � inv�lido.")

        
main()