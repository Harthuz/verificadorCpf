# Validador de CPF

## Descrição
Este script em Python solicita que o usuário digite um CPF e verifica se ele é válido. O CPF (Cadastro de Pessoas Físicas) é um documento de identificação no Brasil, e sua validade é determinada por um algoritmo específico que calcula dois dígitos verificadores.

## Funcionamento do Código

### Passo a Passo

1. **Entrada do Usuário**:
   - O programa solicita que o usuário digite um CPF no formato padrão (com caracteres especiais como pontos e traços).

2. **Declaração de Variáveis**:
   - `cpf_dois_ultimos_digitos`: Armazena os últimos dois dígitos do CPF (os dígitos verificadores).
   - `cpf`: Armazena a parte do CPF sem os dois últimos dígitos.
   - `cpfNumero`: Uma string que irá armazenar os números do CPF sem caracteres especiais.
   - `soma1` e `soma2`: Variáveis que armazenarão o resultado das somas para calcular os dígitos verificadores.
   - `contador1` e `contador2`: Contadores usados para a multiplicação durante o cálculo.

3. **Remoção de Caracteres Especiais e Cálculo da Primeira Soma**:
   - O código percorre cada número do CPF (sem os caracteres especiais) e realiza a primeira soma:
     - Cada número é multiplicado por um contador que começa em 10 e vai até 2.
     - O resultado de cada multiplicação é acumulado na variável `soma1`.

4. **Cálculo do Primeiro Dígito Verificador**:
   - O primeiro dígito verificador (`digito1`) é calculado a partir da soma (`soma1`):
     - `digito1 = soma1 * 10 % 11`
     - Se `digito1` for maior que 9, ele é ajustado para 0.

5. **Cálculo do Segundo Dígito Verificador**:
   - A verificação do primeiro dígito é feita concatenando `cpfNumero` com `digito1` e realizando uma nova soma (`soma2`):
     - Cada número da nova string resultante é multiplicado por um contador que começa em 11 e vai até 2.
   - O segundo dígito verificador (`digito2`) é calculado da mesma forma:
     - `digito2 = soma2 * 10 % 11`
     - Se `digito2` for maior que 9, ele também é ajustado para 0.

6. **Verificação do CPF Completo**:
   - O CPF completo é formado pela concatenação de `cpfNumero`, `digito1` e `digito2`.
   - O código então compara o CPF digitado (incluindo os dígitos verificadores) com o CPF gerado para verificar a validade.

7. **Saída**:
   - O programa imprime "CPF válido" se os CPFs coincidirem, ou "CPF inválido" se não coincidirem.

## Cálculo do CPF
O CPF é composto por 11 dígitos, sendo os 9 primeiros números, seguidos por 2 dígitos verificadores. A validação dos dígitos verificadores é realizada com as seguintes etapas:

- **Primeiro Dígito Verificador**:
  - Calcula-se a soma dos 9 primeiros dígitos, multiplicando cada um deles por pesos de 10 a 2.
  - O resultado é multiplicado por 10 e o resto da divisão por 11 fornece o primeiro dígito verificador.

- **Segundo Dígito Verificador**:
  - Calcula-se a soma dos 9 dígitos originais mais o primeiro dígito verificador, multiplicando por pesos de 11 a 2.
  - O processo é o mesmo: multiplica-se por 10 e o resto da divisão por 11 fornece o segundo dígito verificador.

Com essas etapas, o algorítimo garante que o CPF digitado seja validado corretamente, de acordo com as regras estabelecidas pela Receita Federal do Brasil.
