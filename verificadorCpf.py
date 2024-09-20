# cpf 469.743.048-46

cpf = input("Digite o seu cpf, inclua pontos e traço: ")

cpf = cpf[:-2]
cpfNumero = ""
soma = 0
i = 10

for numero in cpf:
    try:
        numero = int(numero)
        soma += numero * i
        i -= 1
    except:
        ...

multi = soma * 10

resto = multi % 11

print(resto)