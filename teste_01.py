# Criando Variaveis em Python. #
nome = "Eduardo" # Tipo da Variavel: STRING #
sobrenome = "Moura" # Tipo da Variavel: STRING #
idade = 20 # Tipo da Variavel: INT/INTEGER #
altura = 1.75 # Tipo da Variavel: FLOAT #
humano = True # Tipo da Variavel: BOOLEAN #

# Concatenando Variaveis. #
nome_completo = nome +" "+ sobrenome

# Alterando Valores nas Variaveis INT. #
idade = idade + 1 # Ou idade += 1 #

# Exibindo o Tipo de Dado Presente nas Variaveis. #
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(altura))
print(type(humano))

# Exibindo Dados Presentes nas Variaveis. #
print("Ola meu nome é: "+nome_completo)
print("Eu tenho "+str(idade)+" anos") # str(idade) esta convertendo o tipo da variavel idade(INT) para o tipo STRING. #
print("Eu tenho "+str(altura)+" metros de altura") # str(altura) esta convertendo o tipo da variavel altura(FLOAT) para o tipo STRING. #
print("Eu sou um humano? "+str(humano)) # str(humano) esta convertendo o tipo da variavel huamno(BOOL) para o tipo STRING. #