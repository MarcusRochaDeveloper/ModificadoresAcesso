import time
import random

class Veiculo():
    def __init__(self, modelo, placa, marca):
        self.modelo = modelo
        self.placa = placa
        self.marca = marca

    def ligar(self):
        print(f"Ligando o veículo {self.modelo} - {self.marca}...")
        time.sleep(2)
        print(f"O veículo {self.modelo}, {self.marca} de placa {self.placa} foi ligado com sucesso!")

class veiculoCarro(Veiculo):
    def __init__(self, modelo, placa, marca, cavalos):
        super().__init__(modelo, placa, marca)
        self.cavalos = cavalos
        
    def Potencia(self):
        print(f'O {self.modelo} tem atualmente {self.cavalos} de HP')

class ContaBancaria():
    def __init__(self, titular="", saldo=0, nConta=0):
        self.titular = titular
        self.__saldo = saldo
        self.numero_conta = nConta

    def userTitular(self):
        self.titular = input("Digite seu nome completo:  ")
        numeroRandomico = random.randint(100000, 999999)
        self.numero_conta = numeroRandomico
        print(f"Conta criada com sucesso!: {self.titular}, Numero da conta: {self.numero_conta}")

    def set_saldo(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Saldo de R${valor:.2f} setado com sucesso. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Valor inválido")

    def get_saldo(self):
        return self.__saldo

def MenuContaBancaria():
    while True:
        conta = ContaBancaria()
        print("\n//// Classe ContaBancaria ////")
        print("1. Criar conta\n2. Setar\n3. Consultar saldo\n4. Voltar")
        try:
            escolha = int(input("Sua escolha: "))
            if escolha == 1:
                conta.userTitular()
            elif escolha == 2:
                valor = float(input("Valor para setar: "))
                conta.set_saldo(valor)
            elif escolha == 3:
                saldo = conta.get_saldo()
                print(f"Saldo atual: R${saldo:.2f}")
            elif escolha == 4:
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")
            time.sleep(2)

veiculo = None
def MenuVeiculo():
    while True:
        conta = ContaBancaria()
        print("\n//// Classe Veiculo ////")
        print("1. Cadastrar veículo\n2. Ligar veiculo\n3. Ver potencia\n4. Voltar")
        try:
            escolha = int(input("Sua escolha: "))
            if escolha == 1:
                modelo = input("Digite o modelo do veiculo: ")
                placa = input("Digite a placa do veiculo: ")
                marca = input("Digite a marca do veiculo: ")
                potencia = int(input("Digite a quantidade de potencia: "))

                veiculo = veiculoCarro(modelo, placa, marca, potencia)
            elif escolha == 2:
                if veiculo == None:
                    print("\nCadastre um veículo primeiro!")
                    return
                
                veiculo.ligar()
            elif escolha == 3:
                if veiculo == None:
                    print("\nCadastre um veículo primeiro!")
                    return
                
                potenciaAtual = veiculo.Potencia()
            elif escolha == 4:
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")

def MainMenu():
    while True:
        print("\n//// Modificadores de Acesso ////")
        print("1. Classe ContaBancaria\n2. Classe Veiculo\n3. Sair do sistema")
        try:
            opcao = int(input("Sua escolha: "))
            if opcao == 3:
                print("\nEncerrando o sistema...")
                break
        except ValueError:
            print("Opção inválida")
            time.sleep(2)
            return

        if opcao == 1:
            MenuContaBancaria()
        elif opcao == 2:
            MenuVeiculo()

MainMenu()
