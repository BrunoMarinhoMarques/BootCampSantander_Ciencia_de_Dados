nome = "Bruno Henrique Marinho Marques"
idade  = 27
profissao = "Programador"
linguagem = "Python"

#old style, não é mais utilizado
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))

#old style, não é mais tão utilizado
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))

#consigo editar pois ele coloca o indice conforme está em .format
print("Olá, me chamo {1}. Eu tenho {3} anos de idade, trabalho como {2} e estou matriculado no curso de {0}".format(nome, idade, profissao, linguagem))

#mais utilizado, passo as variaveis direto
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159
#coloco o numero de casas e o f representa que é um float
print(f"Valor de PI: {PI:.3f}")

#o 10 indica que vai pular 10 espaços e o 2f a quantidade de casas que vai ter
print(f"Valor de PI: {PI:10.2f}")