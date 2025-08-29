# Q1 - Contar vogais e consoantes:
frase = input("Digite uma frase: ").lower()

vogais = "aeiou"
cont_vogais = 0
cont_consoantes = 0


for c in frase:
    if c.isalpha():
        if c in vogais:
            cont_vogais += 1
        else:
            cont_consoantes += 1

print(f"Vogais: {cont_vogais} | Consoantes: {cont_consoantes}")
