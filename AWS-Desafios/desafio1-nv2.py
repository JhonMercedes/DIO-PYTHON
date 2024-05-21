# Recebe a Entrada do usu�rio e armazena na vari�vel "entrada"
entrada = input()

# Fun��o respons�vel por receber uma afirma��o e retornar a categoria do servi�o � qual se refere.
def escolher_categoria(afirmacao):
    if "nivel mais baixo de abstracao" in afirmacao:
        return "iaas"
        
    # TODO: Preencha corretamente a categoria de servi�o indicada para cada afirma��o, considerando as condi��es abaixo e Sa�das poss�veis:

    elif "nivel intermediario de abstracao" in afirmacao:
        return "paas"
        
    elif "nivel mais alto de abstracao" in afirmacao:
        return "saas"
        
    elif "acesso direto aos recursos de computacao" in afirmacao:
        return "iaas"
        
# Imprime a categoria do servi�o referenciada na afirma��o recebida na "entrada" atrav�s da fun��o "escolher_categoria".
print(escolher_categoria(entrada))