# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma afirmação e retornar a categoria do serviço à qual se refere.
def escolher_categoria(afirmacao):
    if "nivel mais baixo de abstracao" in afirmacao:
        return "iaas"
        
    # TODO: Preencha corretamente a categoria de serviço indicada para cada afirmação, considerando as condições abaixo e Saídas possíveis:

    elif "nivel intermediario de abstracao" in afirmacao:
        return "paas"
        
    elif "nivel mais alto de abstracao" in afirmacao:
        return "saas"
        
    elif "acesso direto aos recursos de computacao" in afirmacao:
        return "iaas"
        
# Imprime a categoria do serviço referenciada na afirmação recebida na "entrada" através da função "escolher_categoria".
print(escolher_categoria(entrada))