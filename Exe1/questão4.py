# Q4 -  Verificador de senha “forte”
senha = input("Digite uma senha: ")

forte = (
    len(senha) >= 8
    and any(c.islower() for c in senha)
    and any(c.isupper() for c in senha)
    and any(c.isdigit() for c in senha)
)

if forte:
    print("Senha forte")
else:
    print("Senha fraca")