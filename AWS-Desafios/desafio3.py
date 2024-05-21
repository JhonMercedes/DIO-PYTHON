# Recebe a Entrada do usu�rio e armazena na vari�vel "entrada"
entrada = input()

# Fun��o respons�vel por receber um cen�rio e retornar a estrat�gia indicada.
def escolher_estrategia(cenario):
    if "aplicativo a ser descomissionado" in cenario or "sem valor comercial" in cenario:
        return "retire"
        
    # TODO: Preencha corretamente a estr�tegia indicada para cada cen�rio, considerando as condi��es abaixo e Sa�das poss�veis:

    elif "manter aplicativos no ambiente de origem" in cenario or "adiar sua migracao para a nuvem" in cenario:
        return "retain"
        
    elif "mover aplicativos para a nuvem sem modifica-los" in cenario or "lift and shift" in cenario:
        return "rehost"
        
    elif "transferir servidores ou instancias para outra plataforma na nuvem" in cenario:
        return "relocate"
        
    elif "substituir o aplicativo por uma versao ou produto diferente" in cenario:
        return "repurchase"
        
    elif "mover o aplicativo para a nuvem" in cenario or "introduzir otimizacoes para opera-lo de forma eficiente" in cenario:
        return "replatform"
        
    elif "modificar a arquitetura do aplicativo" in cenario or "aproveitar os recursos nativos para melhorar agilidade" in cenario:
        return "refactor or re-architect"
        
# Imprime a estrat�gia indicada para o cen�rio recebido na "entrada" atrav�s da fun��o "escolher_estrategia".
print(escolher_estrategia(entrada))