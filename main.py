from classes.cc import ContaCorrente
from classes.cp import ContaPoupanca
from classes.banco import Banco
from classes.cliente import Cliente

# cc = ContaCorrente(1111, 3333, 0, 500)
# cc.depositar(100)
# cc.sacar(250)

banco = Banco()

cliente1 = Cliente('William', 28)
cliente2 = Cliente('Joelma', 35)

conta1 = ContaCorrente(4444, 123456, 0)
conta2 = ContaPoupanca(6666, 654321, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)

banco.inserir_conta(conta1)
banco.inserir_cliente(cliente1)

banco.inserir_conta(conta2)
banco.inserir_cliente(cliente2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Sem Autorização.')

print('####################################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(40)
    cliente2.conta.sacar(20)
else:
    print('Sem Autorização.')
