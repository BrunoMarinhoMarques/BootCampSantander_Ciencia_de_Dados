conta_normal = True
saldo = 2000
saque = 2001
cheque_especial = 450
conta_universitaria = False

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")