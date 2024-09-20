# cpf 469.743.048-46

cpf = input("Digite o seu cpf, inclua pontos e traço: ")
cpfNumero = ""
soma = 0
i = 10
for caractere in cpf:
    try:
        int(caractere)
        cpfNumero += caractere
    except:
        ...

cpfNumero = cpfNumero[:9]

for numero in cpfNumero:
    soma += int(numero) * i
    i -= 1

multi = soma*10

resto = multi % 11

print(resto)