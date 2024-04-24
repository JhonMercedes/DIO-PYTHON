import re

def validate_numero_telefone(phone_number):
   
    pattern = r'\(\d{2}\) 9\d{4}-\d{4}'


    if re.match(pattern, phone_number):  
        return "numero de telefone valido"
    else:
        return "numero de telefone invalido"
       
phone_number = input()  

result = validate_numero_telefone(phone_number)

print(result)