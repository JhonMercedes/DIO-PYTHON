# Recebe a Entrada do usu�rio e armazena na vari�vel "entrada"
entrada = input()

# Fun��o respons�vel por receber uma vantagem e retornar sua respectiva descri��o.
def descrever_vantagem(vantagem):
    if vantagem == "economia de custos":
        return "otimizacao de gastos por meio de modelos de precos flexiveis"
        
    # TODO: Preencha corretamente a descri��o de cada vantagem, considerando as condi��es abaixo e Sa�das poss�veis:
    
    elif vantagem == "infraestrutura global":
        return "fornecer recursos eficientemente em qualquer lugar do mundo"
        
    elif vantagem == "alta disponibilidade":
        return "garantia de que os recursos estejam sempre disponiveis"
        
    elif vantagem == "elasticidade":
        return "capacidade de dimensionar recursos conforme a demanda"
        
    elif  vantagem == "agilidade":
        return "capacidade de desenvolver, testar e implantar rapidamente"
 
# Imprime a descri��o da vantagem recebida na "entrada" atrav�s da fun��o "descrever_vantagem".
print(descrever_vantagem(entrada))