# Dicionários para armazenar usuários e contas correntes
usuarios = {}
contas = {}

def menu_principal():
    while True:
        print(r""" 
          ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
          ▐                                                                              ▌
          ▐  ░█▀▄░█▀█░█▀█░█▀▀░█▀█░░░▀█▀░█▀█░▀█▀░█▀▀░█▀▄░░░█▀▀░░░█▀▀░█▀▄░█▀▀░█▄█░▀█▀░█▀█  ▌
          ▐  ░█▀▄░█▀█░█░█░█░░░█░█░░░░█░░█░█░░█░░█▀▀░█▀▄░░░█▀▀░░░█░█░█▀▄░█▀▀░█░█░░█░░█░█  ▌
          ▐  ░▀▀░░▀░▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░░░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀  ▌
          ▐                                                                              ▌
          ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
                                                                                                                                                     
        """)
        print('\nMenu Principal')
        print('1. Criar Conta')
        print('2. Acessar Conta')
        print('3. Sair')

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")
            continue

        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            cpf = input("Digite o CPF do usuário: ").strip()
            if cpf in usuarios:
                menu_usuario(cpf)
            else:
                print("Usuário não encontrado.")
        elif opcao == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_usuario(cpf):
    while True:
        print(r"""
              ╔══════════════════════════════════════════════════════════════════════════════╗
              ║                                                                              ║
              ║  ░█▀▄░█▀█░█▀█░█▀▀░█▀█░░░▀█▀░█▀█░▀█▀░█▀▀░█▀▄░░░█▀▀░░░█▀▀░█▀▄░█▀▀░█▄█░▀█▀░█▀█  ║
              ║  ░█▀▄░█▀█░█░█░█░░░█░█░░░░█░░█░█░░█░░█▀▀░█▀▄░░░█▀▀░░░█░█░█▀▄░█▀▀░█░█░░█░░█░█  ║
              ║  ░▀▀░░▀░▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░░░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀  ║
              ║                                                                              ║
              ╚══════════════════════════════════════════════════════════════════════════════╝
        """)
        print(f"\nMenu do Usuário: {usuarios[cpf]['nome']}")
        print('1. Depositar')
        print('2. Sacar')
        print('3. Consultar Saldo')
        print('4. Transferir')
        print('5. Extrato')
        print('6. Editar Usuário')
        print('7. Fechar Conta')
        print('8. Excluir Usuário')
        print('9. Voltar ao Menu Principal')

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")
            continue

        if opcao == 1:
            depositar(cpf)
        elif opcao == 2:
            sacar(cpf)
        elif opcao == 3:
            consultar_saldo(cpf)
        elif opcao == 4:
            transferir(cpf)
        elif opcao == 5:
            gerar_extrato(cpf)
        elif opcao == 6:
            editar_usuario(cpf)
        elif opcao == 7:
            fechar_conta(cpf)
        elif opcao == 8:
            excluir_usuario(cpf)
            break
        elif opcao == 9:
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_usuario():
    nome = input("Digite o nome: ").strip()
    cpf = input("Digite o CPF: ").strip()
    if cpf in usuarios:
        print("Usuário já cadastrado.")
    else:
        usuarios[cpf] = {"nome": nome, "cpf": cpf}
        contas[cpf] = {"saldo": 0.0, "extrato": []}
        print(f"Usuário {nome} cadastrado com sucesso.")

def depositar(cpf):
    valor = float(input("Digite o valor do depósito: "))
    if cpf in contas:
        contas[cpf]["saldo"] += valor
        contas[cpf]["extrato"].append(f"Depósito: +R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("Usuário não encontrado.")

def sacar(cpf):
    valor = float(input("Digite o valor do saque: "))
    if cpf in contas:
        if valor > contas[cpf]["saldo"]:
            print("Saldo insuficiente.")
        else:
            contas[cpf]["saldo"] -= valor
            contas[cpf]["extrato"].append(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
    else:
        print("Usuário não encontrado.")

def consultar_saldo(cpf):
    if cpf in contas:
        saldo = contas[cpf]["saldo"]
        print(f"Saldo atual de {usuarios[cpf]['nome']}: R${saldo:.2f}")
    else:
        print("Usuário não encontrado.")

def transferir(cpf_origem):
    cpf_destino = input("Digite o CPF do destinatário: ").strip()
    valor = float(input("Digite o valor da transferência: "))
    if cpf_origem in contas and cpf_destino in contas:
        if valor > contas[cpf_origem]["saldo"]:
            print("Saldo insuficiente para transferência.")
        else:
            contas[cpf_origem]["saldo"] -= valor
            contas[cpf_destino]["saldo"] += valor
            contas[cpf_origem]["extrato"].append(f"Transferência enviada: -R${valor:.2f} para {usuarios[cpf_destino]['nome']}")
            contas[cpf_destino]["extrato"].append(f"Transferência recebida: +R${valor:.2f} de {usuarios[cpf_origem]['nome']}")
            print(f"Transferência de R${valor:.2f} realizada com sucesso.")
    else:
        print("Usuário de origem ou destino não encontrado.")

def gerar_extrato(cpf):
    if cpf in contas:
        print(f"Extrato da conta de {usuarios[cpf]['nome']} (CPF: {usuarios[cpf]['cpf']}):")
        for item in contas[cpf]["extrato"]:
            print(item)
        print(f"Saldo atual: R${contas[cpf]['saldo']:.2f}")
    else:
        print("Usuário não encontrado.")

def editar_usuario(cpf):
    if cpf in usuarios:
        novo_nome = input("Digite o novo nome: ").strip()
        usuarios[cpf]['nome'] = novo_nome
        print(f"Dados do usuário {cpf} atualizados para: {usuarios[cpf]}")
    else:
        print("Usuário não encontrado.")

def fechar_conta(cpf):
    if cpf in contas:
        saldo = contas[cpf]["saldo"]
        if saldo != 0:
            print("Não é possível fechar a conta. O saldo deve ser R$0.00.")
        else:
            contas.pop(cpf)
            print("Conta fechada com sucesso.")
    else:
        print("Usuário não encontrado.")

def excluir_usuario(cpf):
    if cpf in usuarios:
        usuarios.pop(cpf)
        contas.pop(cpf, None)
        print("Usuário e conta excluídos com sucesso.")
    else:
        print("Usuário não encontrado.")

# Inicializa o menu principal
menu_principal()
