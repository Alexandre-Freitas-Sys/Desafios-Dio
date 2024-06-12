#Desafio Sistema Bancário V1.0
#Menu:
menu = """
\033[2;32m
████████████████-Python Bank-████████████████

    [1] Depositar           [2] Sacar
    [5] Extrato             [6] Limites 
    [0] Sair

██████████████████-24Horas-██████████████████

Digite aqui a sua opção ---> """

# Variáveis Principal:
saldo = 0.00
limite = 850.00
extrato = ""
numero_saques = 0
limite_saques = 5

# Comandos Operacionais:

while True:
    user = input(menu)

# Linha de comando para DEPÓSITO:
    if user == "1":
        valor = float(input("Informe o Valor Para Depósito: R$:"))
        print("\033[4;33mDEPOSITO REALIZADO COM SUCESSO.")
        voltar = input("\033[0;31mPressione ENTER para Voltar ao Início.")

        if valor > 0:
            saldo += valor
            extrato += f"Depósito....: +R$:{valor:.2f}\n"

        else:
            print("\033[0;31mOperação Falhou! Valor informado é inválido.")
            voltar = input("\033[0;31mPressione ENTER para Voltar ao Início.")

# Linha de comando para Saque:
    elif user == "2":
        print("\033[3;33mVocê possui {} Saque(s) disponível até as 24h.".format(limite_saques - numero_saques))
        print("\033[3;35mSeu limite para saque é de R$:{:.2f}".format(limite))
        print("\033[1;36mSaldo disponível em conta de R$:{:.2f}".format(saldo))
        valor = float(input("\033[2;32mInforme um Valor Para Saque: R$:"))

        # Variáveis para saque:
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\033[0;31mOperação Falhou!\nVocê Não possui Saldo Suficiente.")
            voltar = input("\033[0;31mPressione ENTER para Voltar ao Início.")

        elif excedeu_limite:
            print("\033[0;31mOperação Falhou!\nO Valor Desejado excede o Limite Permitido.")
            voltar = input("\033[0;31mPressione ENTER para Voltar ao Início.")

        elif excedeu_saques:
            print("\033[0;31mOperação Falhou!\nExcedeu o limite de Saques Permitido.")
            voltar = input("\033[0;31mPressione ENTER para Voltar ao Início.")

        elif valor > 0:
            print("\033[4;33mSAQUE REALIZADO COM SUCESSO.")
            voltar = input("\033[0;31mPressione ENTER para Voltar ao Início.")
            saldo -= valor
            extrato += f"Saque.......: -R$:{valor:.2f}\n"
            numero_saques += 1

        else:
            print("\033[0;31mOperação Falhou! Valor informado é inválido.")
            voltar = input("\033[0;31mPressione ENTER para Voltar ao Início.")

# Linha de comando para Extratos:

    elif user == "5":
        print("████████████████-Python Bank-████████████████")
        print("\033[3;37m================== EXTRATO ==================")
        print("Não Foram Realizadas Movimentações." if not extrato else extrato)
        print(f"\nSaldo em Conta: R$:{saldo:.2f}")
        print("================ FIM EXTRATO ================")
        voltar = input("\033[0;31mPressione ENTER para Voltar ao Início.")

# Linha de comando para Limites:

    elif user == "6":
        print("████████████████-Python Bank-████████████████")
        print("\033[3;37m================== LIMITES ==================")
        print("Confira seus limites:")
        print("")
        print("Você possui um limite de 5 saques diários.")
        print("")
        print("Você já utilizou {} de {}".format(numero_saques, limite_saques))
        print(f"\nSeu valor máximo por saque é de R$:{limite:.2f}")
        print(f"\nSaldo Disponível em Conta: R$:{saldo:.2f}")
        print("")
        print("================ FIM LIMITES ================")
        voltar = input("\033[0;31mPressione ENTER para Voltar ao Início.")

# Linha de comando para Sair:

    elif user == "0":
        break
    else:
        print("\033[0;31mOperação Falhou! Valor informado é inválido.")
