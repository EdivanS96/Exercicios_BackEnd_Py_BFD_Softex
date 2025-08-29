# Q5 - Gerar acrônimo
frase = input("Digite um nome de curso ou expressão: ").lower()

stopwords = {"de", "da", "do", "das", "dos", "e"}
palavras = frase.split()

acronimo = "".join([p[0].upper() for p in palavras if p not in stopwords])

print("Acrônimo:", acronimo)