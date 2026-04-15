import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    saldo_total = 0
    transacoes = []

    while True:
        limpar_tela()
        print(f"💰 Saldo Total: R$ {saldo_total:.2f}")
        print("-" * 25)
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            valor = float(input("Valor do Ganho: "))
            descricao = input("Descrição: ")
            saldo_total += valor
            transacoes.append(f"[+] R$ {valor:.2f} - {descricao}")

        elif opcao == "2":
            valor = float(input("Valor do Gasto: "))
            descricao = input("Descrição: ")
            saldo_total -= valor
            transacoes.append(f"[-] R$ {valor:.2f} - {descricao}")

        elif opcao == "3":
            print("\n📄 Extrato:")
            for t in transacoes:
                print(t)
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "4":
            print("👋 Até a próxima!")
            break

if __name__ == "__main__":
    main()
