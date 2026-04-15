def mostrar_menu():
    print("\n" + "=" * 25)
    print("📋 --- MENU DE TAREFAS --- 📋")
    print("=" * 25)
    print("1. Adicionar Tarefa")
    print("2. Ver Minhas Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")
    print ("=" * 25)

def main():
    tarefas = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("O que você precisa fazer?")
            tarefas.append(tarefa)
            print(f"✅ Tarefa '{tarefa}' adicionada!")

        elif opcao == "2":
            if not tarefas:
                print("📭 Sua lista de tarefas está vazia!")
            else:
                print("\n📋 Suas Tarefas:")
                for i, t in enumerate(tarefas, start=1):
                    print(f"{i}. {t}")

        elif opcao == "3":
            if not tarefas:
                print("📭 Sua lista de tarefas está vazia!")
            else:
                try:
                    n_tarefa = int(input("Digite o número da tarefa que deseja remover: "))
                    removida = tarefas.pop(n_tarefa - 1)
                    print(f"✅ Tarefa '{removida}' removida!")
                except (ValueError, IndexError):
                    print("⚠️ Número inválido. Tente novamente.")

        elif opcao == "4":
            print("👋 Até a próxima!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()