# cpf 469.743.048-46

cpf = input("Digite um CPF: ")

#declarando variáveis
cpf_dois_ultimos_digitos = cpf[-2:]
cpf = cpf[:-2]
cpfNumero = ""
soma1 = 0
soma2 = 0
contador1 = 10
contador2 = 11

#descobrindo cpf sem caracteres especiais e fazendo a primeira soma

for numero in cpf:
    try:
        int(numero)
        cpfNumero += numero
        numero = int(numero)
        soma1 += numero * contador1
        contador1 -= 1
    except:
        ...

#descobrindo o primeiro digito

digito1 = soma1 * 10 % 11

digito1 = digito1 if digito1 <=9 else 0

#descobrindo o segundo digito

cpf_verificacao1 = int(cpfNumero) + digito1

for numero in str(cpf_verificacao1):
    soma2 += int(numero) * contador2
    contador2 -= 1

digito2 = soma2 * 10 % 11
digito2 = digito2 if digito2 <=9 else 0

#verificação do cpf inteiro

cpf_verificado = cpfNumero + str(digito1) + str(digito2)

if (cpfNumero+cpf_dois_ultimos_digitos) == cpf_verificado:
    print("CPF válido")
else:
    print("CPF inválido")