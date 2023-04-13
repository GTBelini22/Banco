"""
Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuárioescolheroque deseja fazer no banco,
como criar uma conta, efetuar saque, efetuar depósito,
efetuartransferência, listar contas ou sair do sistema.

Dificuldaades - retirar dinheiro de uma conta e colocar na outra
Fazer uma função para verificar o ID


"""
from Clientes import Clientes

def cadastro():
    nome = input("\n\nDigite nome do cliente: ")
    cpf = int(input("\nDigite o Cpf do cliente: "))
    saldo = float(input("\nDigite o saldo do cliente: "))
    clientes_banco.append(Clientes(nome, cpf, saldo))

def verifica_id():
    achou = False
    posicao =0
    try:
        id = int(input("\nInforme o Id da conta que deseja verificar: "))
        for i in range(len(clientes_banco)):
            if id == clientes_banco[i].id:
                posicao = i
                achou = True
        if achou == False:
            print("\nID não encontrado")
        return posicao, achou
    except:
        print("ID informado não compatível, tente novamente")
        return posicao, achou


print("Bem vindo ao sistema do Banco!")
clientes_banco = []#Classe responsável por armazenar os clientes do banco e seus dados
saida =0
achou = False
posicao =0
posicao2 = 0


while saida !=6:
    try:
        saida = int(input("\nSelecione uma opção\n1- Criar uma conta\n2- Efetuar saque\n3- Efetuar depósito\n4- Efetuar transferência\n5- Listar contas\n6- Sair do sistema"))

        if saida ==1: #criar conta
            cadastro()
            print("\nCadastro feito com sucesso!")

        elif saida ==2: #saque
            posicao, achou = verifica_id()
            if achou == True:
                clientes_banco[posicao].saque()

        elif saida ==3:# depósito
            posicao, achou = verifica_id()
            if achou == True:
                clientes_banco[posicao].deposito()

        elif saida ==4:#transferência
            print("\n Informe o ID da pessoa que deseja realizar a transferência:")
            posicao, achou = verifica_id()
            if achou == True:
                print("\n Informe o ID da pessoa que deseja enviar o dinheiro: ")
                posicao2, achou = verifica_id()
                if achou == True:
                    valor1 = float(input("Informe o valor a ser transferido: "))
                    if clientes_banco[posicao].saldo > valor1:
                        clientes_banco[posicao].saldo -= valor1
                        clientes_banco[posicao2].saldo +=valor1
                        print(f"\nSaldo da conta que transferiu {clientes_banco[posicao].saldo}\n Saldo da conta que recebeu {clientes_banco[posicao2].saldo}")
                    else:
                        print("Saldo incompatível")

        elif saida ==5:# Listar contas
            for i in range(len(clientes_banco)):
                clientes_banco[i].imprime_dados()
        elif saida ==6: #saida
            print("\nObrigado por usar nosso sistema!!")
        else:
            print("\nDado inválido tente novamente.")
    except:
        print("\nInformação inválida, tente novamente")


