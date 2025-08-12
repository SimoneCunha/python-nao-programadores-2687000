ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
>>> idade_na_formatura = ano_formatura - ano_nascimento
>>> print(idade_na_formatura)
21

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
>>> ano_formatura > ano_nascimento
True
>>> ano_formatura < ano_nascimento
False
>>> ano_formatura == ano_nascimento
False
>>> ano_formatura <= ano_nascimento
False
>>> ano_formatura >= ano_nascimento
True

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
>>> 21 == 21 and 20 == 20
True
>>> 21 == 21 and 19 == 20
False
>>> 21 == 21 or 19 == 20
True
>>> 19 == 21 or 19 == 20
False
>>> not 3 == 1
True
>>> not 3 == 3
False