compras = []

def adicionar(compras, item):
    compras.append(item)
    print(f"'{item}' adicionado!")

def listar(compras):
    if not compras:
        print("A lista está vazia.")
        return
    for numero, item in enumerate(compras, start=1):
        print(f"{numero}. {item}")

def remover(compras, item):
    if item in compras:
        compras.remove(item)
        print(f"'{item}' removido!")
    else:
        print("Item não encontrado.")

compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Listar itens")
    print("3. Remover item")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Nome do item: ").strip()
        adicionar(compras, item)
    elif opcao == "2":
        listar(compras)
    elif opcao == "3":
        item = input("Item a remover: ").strip()
        remover(compras, item)
    elif opcao == "4":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")


print(compras)