# Q2 - Verificar palíndromo (ignorando espaços e maiúsculas):
texto = input("Digite uma palavra: ")

texto_normal = texto.replace(" ", "").lower()#Normalizando a palavra

if texto_normal == texto_normal[::-1]:
    print("É Palíndromo")
else:
    print("Não é Palíndromo")