saldo = 2000
saque = 2001

#utilizado quando é algo simples, o if é verificado e retorna o valor da variavel, o else apenas altera o valor para "Falha" caso o if não seja atendido
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar saque!")