# Dicionário para armazenar usuários
usuarios = {}

# Dicionário para armazenar contas correntes
contas = {}
#adicionado menu em 03 07 10 horas
while True:
    print('\nMenu Principal')
    print('1. Criar Conta')
    print('2. Depositar')
    print('3. Sacar')
    print('4. Consultar Saldo')
    print('5. Sair')
    
    opcao = int(input('Escolha uma opção: '))
    
    if opcao == 1:
        print("Opção Criar Conta selecionada.")
        pass  
    elif opcao == 2:
        print("Opção Depositar selecionada.")
        pass 
    elif opcao == 3:
        print("Opção Sacar selecionada.")
        pass 
    elif opcao == 4:
        print("Opção Consultar Saldo selecionada.")
        pass  
    elif opcao == 5:
        print("Saindo...")
        break  
    else:
        print("Opção inválida. Tente novamente.")


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
    else:
        print("Usuário não encontrado.")

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
cadastrar_usuario("João", "12345678900")
cadastrar_usuario("Maria", "09876543211")

# Realizar algumas operações (exemplo)
depositar("12345678900", 1000.0)
sacar("12345678900", 200.0)
transferir("12345678900", "09876543211", 300.0)

# Gerar extratos (exemplo)
gerar_extrato("12345678900")
print()
gerar_extrato("09876543211")