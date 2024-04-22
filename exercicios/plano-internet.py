
consumo = float(input())

def recomendar_plano(consumo):
    if consumo <= 10:
        print("Plano Essencial Fibra - 50Mbps")
    elif consumo <= 20:
        print("Plano Prata Fibra - 100Mbps")
    else:
        print("Plano Premium Fibra - 300Mbps")
    

recomendar_plano(consumo)




