# Recebe a Entrada do usu�rio e armazena na vari�vel "entrada"
entrada = input()

# Fun��o encarregada de receber uma responsabilidade e retornar o respons�vel por ela.
def indicar_responsavel(responsabilidade):
    if "seguranca da nuvem" in responsabilidade:
        return "AWS"
        
    # TODO: Preencha corretamente o respons�vel indicado para cada responsabilidade, considerando as condi��es abaixo e Sa�das poss�veis:

    elif "seguranca na nuvem" in responsabilidade:
        return "cliente"
        
    elif "garantir que os dados estejam em conformidade com as leis" in responsabilidade:
        return "cliente"
        
    elif "proteger a infraestrutura que executa todos os servicos" in responsabilidade:
        return "AWS"
        
# Imprime o respons�vel pela responsabilidade recebida na "entrada" atrav�s da fun��o "indicar_responsavel".
print(indicar_responsavel(entrada))