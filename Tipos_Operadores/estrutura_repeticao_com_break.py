while True:
    numero = int(input("Informe um número: "))

    #ele sai do laço de repetição
    if numero == 10:
        break
    print(numero)


for numero in range(0,101, 5):
    #ele ignora e continua o laço(não foi impresso)
    if numero == 20:
        continue
    print(numero, end=" ")