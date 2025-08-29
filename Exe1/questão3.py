# Q3 - ) Frequência de palavras
frase = input("Digite uma frase: ").lower()

palavras = frase.split()
frequencia = {}

for p in palavras:
    frequencia[p] = frequencia.get(p, 0) + 1

for palavra, qtd in frequencia.items():
    print(f"{palavra}: {qtd}")