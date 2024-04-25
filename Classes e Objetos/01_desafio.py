class bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        

    def buzinar(self):
        print('plim plim')

    def parar(self):
        print('parando bicicleta')
        print('bicicleta parada')
    
    def correr(self):
        print('vrummmmmmm!')

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
b1 = bicicleta('vermelha','monark',2023,600)
#print(b1.cor,b1.modelo)
print(b1)

