data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável acima
>>> print(type(data_nascimento))
<class 'str'>
print(type(idade_numerica))
<class 'int'>
print(type(altura))
<class 'float'>

# Realize uma operação entre dados do tipo string e inteiro
>>> data_nascimento * 3
'05-10-197605-10-197605-10-1976'

# Realize uma operação entre dados do tipo inteiro e float
>>> soma = idade_numerica + altura
>>> print(soma)
47.74