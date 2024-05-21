# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função encarregada de receber um cenário e retornar se é mais apropriado usar um grupo de segurança ou uma ACL.
def determinar_mecanismo_controle(cenario):
    if "uma aplicacao precisa permitir o trafego apenas na porta 80" in cenario:
        return "grupo de seguranca"
        
    # TODO: Preencha corretamente, considerando as condições abaixo e Saídas possíveis:
        
    elif "uma sub-rede precisa bloquear todo o trafego de entrada" in cenario:
        return "ACL de rede"
        
    elif "bloquear trafego externo para instancias em uma sub-rede privada" in cenario:
        return "ACL de rede"
        
    elif "permitir acesso SSH a uma instancia somente para um endereço IP" in cenario:
        return "grupo de seguranca"
        
# Imprime o mecanismo de controle indicado para o cenário fornecido na "entrada" através da função "determinar_mecanismo_controle".
print(determinar_mecanismo_controle(entrada))