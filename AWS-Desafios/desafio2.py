# Recebe a Entrada do usu�rio e armazena na vari�vel "entrada"
entrada = input()

# Fun��o respons�vel por receber um pilar e retornar sua respectiva descri��o.
def descrever_pilar(pilar):
    if pilar == "excelencia operacional":
        return "execucao e monitoramento de sistemas e melhoria continua"
        
    # TODO: Preencha corretamente a descri��o de cada pilar, considerando as condi��es abaixo e Sa�das poss�veis:
    
    elif pilar == "seguranca":
        return "protecao de informacoes e sistemas"
        
    elif pilar == "confiabilidade":
        return "capacidade dos sistemas de executar as funcoes pretendidas"
        
    elif pilar == "eficiencia de performance":
        return "alocacao eficaz e otimizada de recursos de TI e computacao"
        
    elif pilar == "otimizacao de custos":
        return "obtencao do melhor retorno sobre o investimento em recursos"
        
    elif pilar == "sustentabilidade":
        return "reducao do impacto ambiental dos sistemas na nuvem"
 
# Imprime a descri��o do pilar recebido na "entrada" atrav�s da fun��o "descrever_pilar".
print(descrever_pilar(entrada))