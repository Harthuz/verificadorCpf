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

digito = soma * 10 % 11

print(digito)