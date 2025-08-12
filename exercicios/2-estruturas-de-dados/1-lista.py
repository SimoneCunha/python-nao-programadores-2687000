# Crie uma lista apenas com elementos numéricos
numerica = [1, 2, 3, 4, 5]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
linguagens = ['python', 'r', 'julia', 'simone', 'helbert']

# Imprima na tela apenas os 5 primeiros elementos da lista
linguagens[0:5]
['python', 'r', 'julia', 'simone', 'helbert']

# Crie um slice na lista para que imprima na tela os elementos de índice par
>>> linguagens[0:-1:2]
['python', 'julia']

# Remova da lista o último item
>>> print(linguagens)
['python', 'r', 'julia', 'simone']
>>> linguagens.pop()
'simone'
>>> print(linguagens)
['python', 'r', 'julia']
>>> 
# Insira na lista um novo item
>>> print(linguagens)
['python', 'r', 'julia']
>>> linguagens_adicionais = ['simone', 'davi']
>>> linguagens.extend(linguagens_adicionais)
>>> print(linguagens)
['python', 'r', 'julia', 'simone', 'davi']
>>> 
# Remova da lista um item específico
>>> linguagens = ['python', 'r', 'julia', 'simone', 'helbert']
>>> print(linguagens)
['python', 'r', 'julia', 'simone', 'helbert']
>>> linguagens.remove('helbert')
>>> print(linguagens)
['python', 'r', 'julia', 'simone']
>>> 