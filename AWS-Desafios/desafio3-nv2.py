# Recebe a Entrada do usu�rio e armazena na vari�vel "entrada"
entrada = input()

# Fun��o encarregada de receber um cen�rio e retornar se � mais apropriado usar um grupo de seguran�a ou uma ACL.
def determinar_mecanismo_controle(cenario):
    if "uma aplicacao precisa permitir o trafego apenas na porta 80" in cenario:
        return "grupo de seguranca"
        
    # TODO: Preencha corretamente, considerando as condi��es abaixo e Sa�das poss�veis:
        
    elif "uma sub-rede precisa bloquear todo o trafego de entrada" in cenario:
        return "ACL de rede"
        
    elif "bloquear trafego externo para instancias em uma sub-rede privada" in cenario:
        return "ACL de rede"
        
    elif "permitir acesso SSH a uma instancia somente para um endere�o IP" in cenario:
        return "grupo de seguranca"
        
# Imprime o mecanismo de controle indicado para o cen�rio fornecido na "entrada" atrav�s da fun��o "determinar_mecanismo_controle".
print(determinar_mecanismo_controle(entrada))