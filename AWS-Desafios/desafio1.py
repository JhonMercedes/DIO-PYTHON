# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma vantagem e retornar sua respectiva descrição.
def descrever_vantagem(vantagem):
    if vantagem == "economia de custos":
        return "otimizacao de gastos por meio de modelos de precos flexiveis"
        
    # TODO: Preencha corretamente a descrição de cada vantagem, considerando as condições abaixo e Saídas possíveis:
    
    elif vantagem == "infraestrutura global":
        return "fornecer recursos eficientemente em qualquer lugar do mundo"
        
    elif vantagem == "alta disponibilidade":
        return "garantia de que os recursos estejam sempre disponiveis"
        
    elif vantagem == "elasticidade":
        return "capacidade de dimensionar recursos conforme a demanda"
        
    elif  vantagem == "agilidade":
        return "capacidade de desenvolver, testar e implantar rapidamente"
 
# Imprime a descrição da vantagem recebida na "entrada" através da função "descrever_vantagem".
print(descrever_vantagem(entrada))