import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha_lista = []

    for _ in range(tamanho):
        escolha = random.choice(caracteres)
        senha_lista.append(escolha)

    senha_final = "".join(senha_lista)

    return senha_final

if __name__ == "__main__":
    print("🔐 --- GERADOR DE SENHAS SEGURAS --- 🔐")

    try:
        tamanho = int(input("Qual o comprimento da senha?"))

        if tamanho < 4:
            print("⚠️ Tente um comprimento maior para sua segurança!")
        else:
            resultado = gerar_senha(tamanho)
            print("-" * 30)
            print(f"🔑 Sua nova senha é: {resultado}")
            print("-" * 30)

    except ValueError:
        print("⚠️ Por favor, insira um número válido para o comprimento da senha.")