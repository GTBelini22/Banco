class Clientes:

    contador =0
    def __init__(self, nome, cpf, saldo):
        self.__id = Clientes.contador +1
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        Clientes.contador = self.__id

    @property
    def id(self):
        return self.__id
    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,novo_saldo):
        self.__saldo = novo_saldo

    def saque(self):
        try:
            qtd = float(input("\nInforme a quantidade que deseja sacar:"))
            if qtd> self.__saldo:
                print("\nA Quantidade informada é maior que o saldo atual!!")
            else:
                self.__saldo -=qtd
                print(f"\nSeu saldo atual é de {self.__saldo}")
        except:
            print("Algo deu errado! Tente novamente")

    def deposito(self):
        try:
            qtd = float(input("\nInforme a quantidade a ser depositada: "))
            if qtd>0:
                self.__saldo += qtd
                print(f"\nSaldo atualizado para: {self.__saldo}")
            else:
                print("Quantidades negativas são inválidas!")
        except:
            print("Algo deu errado!Tente novamente")

    def imprime_dados(self):
        print(f"\nNome do titular{self.__nome} ")
        print(f"Saldo {self.__saldo}")
        print(f"CPF {self.__cpf}")
