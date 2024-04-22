# quantidade_passos = int(input())

# if quantidade_passos > 0:
#     for passo in range (1,quantidade_passos + 1):
#         print(f"Explorador: {passo} passo{'s' if passo >1 else ''}")
# else:
#     print("Nenhum passo dado na floresta.")


# Lista para armazenar os itens
itens=[]

for i in range(3):
    item = input("Digite o item: ")
    itens.append(item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")
