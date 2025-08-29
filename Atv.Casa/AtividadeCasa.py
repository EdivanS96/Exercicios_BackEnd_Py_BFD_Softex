# Atividade de Casa - Curso Back-End com Python
# Gerenciador de Palavras

palavras = input("Digite palavras separadas por espaço: ").split()

# Contadores
cont_a = 0
cont_palindromo = 0
cont_longas = 0
cont_comuns = 0

for palavra in palavras:
    categorias = []

    if palavra.lower().startswith("a"):
        categorias.append("Começa com A")
        cont_a += 1

    if palavra.lower() == palavra[::-1].lower():
        categorias.append("É palíndromo")
        cont_palindromo += 1

    if len(palavra) > 7:
        categorias.append("Palavra longa")
        cont_longas += 1

    if not categorias:  # se não entrou em nenhuma
        categorias.append("Palavra comum")
        cont_comuns += 1

    print(f"{palavra} → {', '.join(categorias)}")

print("\nResumo:")
print(f"Palavras que começam com A: {cont_a}")
print(f"Palíndromos: {cont_palindromo}")
print(f"Palavras longas: {cont_longas}")
print(f"Palavras comuns: {cont_comuns}")