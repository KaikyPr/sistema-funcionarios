# Sistema de Cadastro de Funcionários

funcionarios = []

def cadastrar_funcionario():
    print("\n--- CADASTRAR FUNCIONÁRIO ---")
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))

    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }

    funcionarios.append(funcionario)
    print(f"\n✅ Funcionário {nome} cadastrado com sucesso!")

def listar_funcionarios():
    print("\n--- LISTA DE FUNCIONÁRIOS ---")

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    for i, funcionario in enumerate(funcionarios):
        print(f"\n👤 Funcionário {i + 1}")
        print(f"   Nome: {funcionario['nome']}")
        print(f"   Cargo: {funcionario['cargo']}")
        print(f"   Salário: R$ {funcionario['salario']:.2f}")

def buscar_funcionario():
    print("\n--- BUSCAR FUNCIONÁRIO ---")
    nome_busca = input("Digite o nome: ")
    encontrado = False

    for funcionario in funcionarios:
        if nome_busca.lower() in funcionario["nome"].lower():
            print(f"\n👤 Encontrado!")
            print(f"   Nome: {funcionario['nome']}")
            print(f"   Cargo: {funcionario['cargo']}")
            print(f"   Salário: R$ {funcionario['salario']:.2f}")
            encontrado = True

    if not encontrado:
        print("Funcionário não encontrado.")

def remover_funcionario():
    print("\n--- REMOVER FUNCIONÁRIO ---")

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    listar_funcionarios()
    numero = int(input("\nDigite o número do funcionário para remover: "))

    if numero < 1 or numero > len(funcionarios):
        print("Número inválido.")
        return

    removido = funcionarios.pop(numero - 1)
    print(f"\n✅ Funcionário {removido['nome']} removido com sucesso!")

def editar_funcionario():
    print("\n--- EDITAR FUNCIONÁRIO ---")

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    listar_funcionarios()
    numero = int(input("\nDigite o número do funcionário para editar: "))

    if numero < 1 or numero > len(funcionarios):
        print("Número inválido.")
        return

    funcionario = funcionarios[numero - 1]

    print("\nO que deseja editar?")
    print("1 - Nome")
    print("2 - Cargo")
    print("3 - Salário")
    opcao = input("Escolha: ")

    if opcao == "1":
        funcionario["nome"] = input("Novo nome: ")
        print("\n✅ Nome atualizado com sucesso!")
    elif opcao == "2":
        funcionario["cargo"] = input("Novo cargo: ")
        print("\n✅ Cargo atualizado com sucesso!")
    elif opcao == "3":
        funcionario["salario"] = float(input("Novo salário: "))
        print("\n✅ Salário atualizado com sucesso!")
    else:
        print("Opção inválida.")

def calcular_media_salarial():
    print("\n--- MÉDIA SALARIAL ---")

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    total = 0
    for funcionario in funcionarios:
        total = total + funcionario["salario"]

    media = total / len(funcionarios)
    print(f"\n💰 Total em salários: R$ {total:.2f}")
    print(f"📊 Média salarial: R$ {media:.2f}")

def maior_salario():
    print("\n--- MAIOR SALÁRIO ---")

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    maior = funcionarios[0]
    for funcionario in funcionarios:
        if funcionario["salario"] > maior["salario"]:
            maior = funcionario

    print(f"\n🏆 Funcionário com maior salário:")
    print(f"   Nome: {maior['nome']}")
    print(f"   Cargo: {maior['cargo']}")
    print(f"   Salário: R$ {maior['salario']:.2f}")

def exibir_menu():
    print("\n===== SISTEMA DE FUNCIONÁRIOS =====")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário")
    print("4 - Editar funcionário")
    print("5 - Remover funcionário")
    print("6 - Calcular média salarial")
    print("7 - Funcionário com maior salário")
    print("0 - Sair")
    print("===================================")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            buscar_funcionario()
        elif opcao == "4":
            editar_funcionario()
        elif opcao == "5":
            remover_funcionario()
        elif opcao == "6":
            calcular_media_salarial()
        elif opcao == "7":
            maior_salario()
        elif opcao == "0":
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

main()