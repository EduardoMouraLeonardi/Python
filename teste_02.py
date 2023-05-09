# Metodos Para String #

# Criando Variaveis em uma unica linha. #
nome, sobrenome, idade = "eduardo", "MOURA", "20"

# Exibindo o Tamanho de um Dado do Tipo STRING. #
print("O tamanho do dado na variavel nome é: ")
print(len(nome))

# Exibindo a Posição de um Caractere Expecifico em uma STRING. #
print("Na variavel \"nome\" a letra \"e\" se encontra na posição: ")
print(nome.find("e"))# "e" é representado como 0 pois computadores começão contagens a partir de 0 ao inves de 1. #

# Contar Quantos Caracteres Especificos Estão Presentes no Dado Armazanado. #
print("Na variavel \"nome\" a letra \"d\" esta presente: ")
print(str(nome.count("d"))+" veses")

# Alterando Caracteres Especificos Presentes no Dado Armazanado. #
print("Ao alterar caracteres especificos da variavel \"nome\" as letras \"d\" se tornam \"D\"")
print("De "+nome+" para "+nome.replace("d","D"))

# Transformando a 1° Letra de uma STRING em Caixa Alta. #
print("Capitalizando a 1° letra da variavel \"nome\"")
print(nome.capitalize())

# Transformando Todo valor de uma STRING em Caixa Alta. #
print("Capitalizando toda a variavel \"nome\"")
print(nome.upper())

# Transformando a 1° Letra de uma STRING em Caixa Baixa. #
print("Convertendo caracteres para caixa baixa:")
print("De "+sobrenome+" para "+sobrenome.lower())

# Verificando se o Valor do Dado tipo STRING é Composto por Numeros. #
print("O valor na variavel \"idade\" é composto por numeros?")
print(idade.isdigit())

# Verificando se o Valor do Dado tipo STRING é Composto por Letras. #
print("O valor na variavel \"idade\" é composto por letras?")
print(idade.isalpha())

# Exibindo Dados Presentes nas Variaveis. #
print("Ola meu nome é: "+nome+" "+sobrenome+" e tenho: "+idade+" anos.")

# Exibindo um Dado Multiplas Vezes. #
print("Exibindo o valor de uma variavel multiplas vezes")
print(nome*3)