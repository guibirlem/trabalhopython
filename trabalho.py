# Codigo com inicio do excluir conta 11:30 | 03/07
# Dicionário para armazenar usuários
usuarios = {}

# Dicionário para armazenar contas correntes
contas = {}

while True:
    print('''####MENU####
        1 - Cadastro de usuário
        2 - Realizar depósito
        3 - Realizar saque
        4 - Consultar saldo 
        5 - Excluir conta
        6 - Sair''')

    opc = int(input('Digite uma opção: '))


    def cadastrar_usuario(nome, cpf):
        if cpf in usuarios:
            print("Usuário já cadastrado.")
        else:
            usuarios[cpf] = {"nome": nome, "cpf": cpf}
            contas[cpf] = {"saldo": 0.0, "extrato": []}
            print(f"Usuário {nome} cadastrado com sucesso.")


    def depositar(cpf, valor):
        if cpf in contas:
            contas[cpf]["saldo"] += valor
            contas[cpf]["extrato"].append(f"Depósito: +R${valor:.2f}")
        else:
            print("Usuário não encontrado.")


    def sacar(cpf, valor):
        if cpf in contas:
            if valor > contas[cpf]["saldo"]:
                print("Saldo insuficiente.")
        else:
            contas[cpf]["saldo"] -= valor
            contas[cpf]["extrato"].append(f"Saque: -R${valor:.2f}")
        """else:
            print("Usuário não encontrado.")"""

    def excluir(conta):
        if conta in usuarios:
            conta.pop('cpf','Valor já removido')
    

    def transferir(cpf_origem, cpf_destino, valor):
        if cpf_origem in contas and cpf_destino in contas:
            if valor > contas[cpf_origem]["saldo"]:
                print("Saldo insuficiente para transferência.")
            else:
                contas[cpf_origem]["saldo"] -= valor
                contas[cpf_destino]["saldo"] += valor
                contas[cpf_origem]["extrato"].append(f"Transferência enviada: -R${valor:.2f} para {usuarios[cpf_destino]['nome']}")
                contas[cpf_destino]["extrato"].append(f"Transferência recebida: +R${valor:.2f} de {usuarios[cpf_origem]['nome']}")
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

    # Adicione a função fechar_conta aqui
    # Adicione a função consultar_saldo aqui

    # Cadastro de usuários (exemplo)
    #if opc == 1: 
    """cadastrar_usuario("João", "12345678900")
    cadastrar_usuario("Maria", "09876543211")"""
    if opc == 1:
        cadastrar_usuario = input('Digite seu nome: ')
        cadastrar_usuario = int(input('Informe seu CPF: '))

    elif opc == 5:
        cpf = input('Informe seu CPF para excluir a conta: ')
        excluir(cpf)
     

    if opc == 6:
        break

    # Realizar algumas operações (exemplo)
    #elif opc ==2:
    #depositar("12345678900", 1000.0)
    #sacar("12345678900", 200.0)
    #transferir("12345678900", "09876543211", 300.0)

    # Gerar extratos (exemplo)
    #elif opc ==3:
    #gerar_extrato("12345678900")
    #print()
    #gerar_extrato("09876543211")


