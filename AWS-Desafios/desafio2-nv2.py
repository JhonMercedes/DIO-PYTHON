# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função encarregada de receber uma responsabilidade e retornar o responsável por ela.
def indicar_responsavel(responsabilidade):
    if "seguranca da nuvem" in responsabilidade:
        return "AWS"
        
    # TODO: Preencha corretamente o responsável indicado para cada responsabilidade, considerando as condições abaixo e Saídas possíveis:

    elif "seguranca na nuvem" in responsabilidade:
        return "cliente"
        
    elif "garantir que os dados estejam em conformidade com as leis" in responsabilidade:
        return "cliente"
        
    elif "proteger a infraestrutura que executa todos os servicos" in responsabilidade:
        return "AWS"
        
# Imprime o responsável pela responsabilidade recebida na "entrada" através da função "indicar_responsavel".
print(indicar_responsavel(entrada))