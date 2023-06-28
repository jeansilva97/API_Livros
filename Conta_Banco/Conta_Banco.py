from datetime import datetime #Importando o pacote datatime para usar a data e hora no método de transações
import pytz #Realizado o ajuste de fuso-horário


class ContaCorrente: #Criando uma classe conta corrente
    """
     Cria um objeto ContaCorrente para gerenciar as contas dos clientes.
     
     Atributos:
     nome: Nome do Cliente
     cpf: CPF do Cliente
     agencia: Agência responsável pela conta do Cliente
     conta: Numero da conta corrente do Cliente
     saldo: Saldo disponivel na conta do cliente
     limite: Limite de cheque especial do Cliente
     transacoes: Histórico de transações do Cliente
     
    """

    @staticmethod #Atenção no código de método estático
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East") #Ajustando o fuso-horário para o horário de Brasilia
        horario_BR = datetime.now(fuso_BR) #Registrando o horário na variável horario_BR
        return horario_BR.strftime("%d,%m,%Y %H:%M:%S") #Método dará como retorno o horário atual (de brasilia) formatado pelo strftime

    def __init__(self, nome, cpf, agencia, conta): #Definindo os atributos que uma conta corrente deve ter e definindo os parametros
        self.nome = nome #Definindo o parametro nome da pessoa que vai ser adicionado ao criar a conta
        self.cpf = cpf #Definindo o parametro CPF da pessoa que vai ser adicionado ao criar a conta
        self.saldo = 0 #Definindo o parametro saldo da conta que inicialmente definimos como zero ao ser criado a conta
        self. limite = None #Criando um atributo limite e não definindo valor para ele. Esse atributo foi criado para ser chamado para o método limite_conta(abaixo)
        self.agencia = agencia #Criando um atributo de agencia
        self.conta = conta #Criando um atributo de conta
        self.transacoes =[] #Criando uma lista de transações vázia para armazenar o histórico de transações que serão realizados

    def Consultar_saldo(self): #Definindo um método para consulta de saldo
        print("Seu saldo é de R${:,.2f}" .format(self.saldo)) #Atributo desse método

    def Depositar_valor(self, valor): #Definindo método que permite realizar deposito na conta
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora())) #Adicionando a transação de deposito na lista de transações, saldo e data hora do momento da transação
        
    def _Limite_conta(self): #Criando método AUXILIAR de limite de conta que será utilizado como verificação de disponiblizade para retirada de valor pelo método de retirada. Underline na frente é metodo de boas práticas para informar aos desenvolvedores que este métodos só deve ser utilizado na classe e não fora dela no programa.
        self.limite = -1000 #Definindo valor limite da conta sendo no máximo -R$1.000,00
        return self.limite

    def retirada_valor(self, retirada): #Criado método de retirada de valor
        if self.saldo - retirada < self._Limite_conta(): #Definido verificação se possui saldo suficente para retirada
            print("Retirada negada. Você não possui saldo disponível")
            self.Consultar_saldo()
        else:
            self.saldo -= retirada
            self.transacoes.append((-retirada, self.saldo, ContaCorrente._data_hora())) # Adicionando a transação de retirada na lista de transações, saldo e data hora do momento da transação

    def Consultar_LimiteChequeEspecial(self): #Definindo método de consulta de cheque especial
        print("O limite do seu cheque especial é de R${:,.2f}" .format(self._Limite_conta()))

    def Consultar_Historico_transacoes(self): #Criando método pra demonstrar histórico de transação formatado
        print("Histórico de Transações:")
        for transacoes in self.transacoes: #Demonstrar transação por transação separado por linha
            Valor_Transacao = transacoes[0]
            saldo =transacoes[1]
            momento = transacoes[2]
            print("Valor da Transação: R${:,.2f}. Saldo: R${:,.2f}. Data e hora: {}".format(Valor_Transacao, saldo, momento))

    def transferir(self, valor, conta_destino): #Criando um método de transferencia de valor entre contas
        if self.saldo - valor < self._Limite_conta():
            print("Transferência negada pelo saldo ser insuficiente.")
        else:
            self.saldo -=valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
            conta_destino.saldo += valor
            conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


