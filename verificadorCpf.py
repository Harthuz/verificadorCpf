# cpf 469.743.048-46

cpf = "469.743.048-46"

#declarando variáveis

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

cpfNumero = int(cpfNumero) + digito1

for numero in str(cpfNumero):
    soma2 += int(numero) * contador2
    contador2 -= 1

digito2 = soma2 * 10 % 11
digito2 = digito2 if digito2 <=9 else 0

print(digito2)