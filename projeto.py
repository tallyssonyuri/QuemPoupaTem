# essa é uma alteração

# Nome: Tallysson Yuri Campelo Fidelis
# R.A. 22.222.005-5
# Equipe: 33

# Este é o projeto semestral desenvolido para a disciplina "Fundamentos de Algorítimos" sob a monitoria dos docentes: Prof.º Charles Porto Ferreira e Prof.ª Gabriela Biondi
# O objetivo é desenvolver um sistema bancário completo e este deve ser realizado todo em Python

# Inicio as minhas linhas de código designinando todas as funções que serão utilizadas no sistema, elas serão utilizadas quando o usuário selecionar as opções que as chamam

def novo_cliente ():
    # A função "novo_cliente" será utilizada para adicionar um cliente ao banco de dados ao banco, abaixo será solicitado ao usuário alguns dados para que esse cadastro seja feito
    
    while True: # a função funciona dentro de um laço de repetição infinito que só termina a partir do momento que o usuario tiver confirmados os dados inseridos, caso o usuario ter digitado algum valor errado, ele retorna para que possa inseri-los novamente
        
        print("NOVO CLIENTE")
        print()
    
        nome = input("Nome: \n")
        cpf = input("CPF: \n")
        tipo_de_conta = input("Tipo de conta (comum ou plus): \n")
        valor_inicial = float(input("Valor inicial da conta:\nR$ ")) # o valor em dinheiro é classificado como um float, pois é um dado númerico real
        senha = input("Digite sua senha: \n")

        print("Você confirma todos os dados digitados?")
        confirma = input("Os dados digitados estão corretos? Aperte 0 para prosseguir ou qualquer outra tecla para retornar: ")
        if confirma == '0':
            print()
            print("Novo cliente cadastrado!")
            print()
            print("Nome: ", nome)
            print("CPF: ", cpf)
            print("Tipo de conta: ", tipo_de_conta)
            print("Valor inicial da conta: R$ %.2f" % valor_inicial)
            print("Senha: ", senha)
            print()
            break
          
def apaga_cliente ():
    cpf_apagado = input("Qual o CPF do cliente que você deseja apagar? (Somente número)\n")
    print("Cliente do CPF %d excuiído!" % cpf_apagado)
    print()

def listar_clientes ():
    print("Clientes listados")

def debito ():
    cpf_debito = input("Digite o CPF do cliente: ")
    senha = input("Digite a senha: ")
    valor_debito = float(input("Digite o valor do débito: R$"))
    print()
    print(cpf_debito)
    print(senha)
    print(valor_debito)

def deposito ():
    cpf_deposito = int(input("Digite o CPF do cliente (Somente números): "))
    valor_deposito = float(input("Digite o valor do depósito: R$"))
    print()
    print(cpf_deposito)
    print(valor_deposito)

def extrato ():
    cpf_extrato = int(input("Digite o CPF do cliente (Somente números): "))
    senha = input("Digite a senha: ")
    print()
    print(cpf_extrato)
    print(senha)

def transferencia ():
    cpf_cliente = int(input("Digite o CPF do cliente (Somente números): "))
    senha = input("Digite a senha: ")
    cpf_transferencia = int(input("Digite o CPF para transferência (Somente números): "))
    valor_transferencia = float(input("Digite o valor da transferência: R$"))
    print()
    print(cpf_cliente)
    print(senha)
    print(cpf_transferencia)
    print(valor_transferencia)

def operacao_livre ():
    print("Operação em construção")

# Aqui começa a exbição do programa, onde exibe uma mensagem de boas vindas inicial e logo após inicia-se um laço de repetição infinito, onde é explicado ao usuário como funciona o menu inicial e o que ele precisa digitar para prosseguir, assim que o usuário finaliza a ação, a mensagem do menu retornará até ele sair

print("Seja bem vindo ao Banco QuemPoupaTem!")
print()

while True:
    print("Qual operação você deseja realizar?")
    print()

    print("1. Novo cliente")
    print("2. Apaga cliente")
    print("3. Listar clientes")
    print("4. Débito")
    print("5. Depósito")
    print("6. Extrato")
    print("7. Transferência entre contas")
    print("8. Operação livre")
    print("9. Sair")
    print()

    operacao = int(input("Digite o número correspondente a operação escolhida: "))
    print()

    if operacao == 1:
        novo_cliente()
    elif operacao == 2:
        apaga_cliente()
    elif operacao == 3:
        listar_clientes()
    elif operacao == 4:
        debito()
    elif operacao == 5:
        deposito()
    elif operacao == 6:
        extrato()
    elif operacao == 7:
        transferencia()
    elif operacao == 8:
        operacao_livre()
    elif operacao == 9:
        break
    else:
        print("Por favor, digite uma operação válida")
    
print("Obrigado por utilizar os serviços do Banco QuemPoupaTem!") # Esta mensagem vai ser exibida após o usuario optar por sair do laço de repetição e assim, finalizando as ações no programa
print()