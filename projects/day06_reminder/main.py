import time

def mostrar_cabecalho():
    largura = 50
    print("=" * largura)
    print ("⏰ Lembrete para o Dia a Dia ⏰".center(largura,))
    print ("=" * largura)

mostrar_cabecalho()

mensagem = input("⏰ O que você gostaria de ser lembrado? ⏰\n> ")

tempo_espera = int(input("\n⏳ Em quantos minutos você quer ser lembrado?\n>  "))

print(f"✅ Lembrete definido! Você será lembrado em {tempo_espera} minutos.")

time.sleep(tempo_espera * 60)

print(f"🔔 Lembrete: {mensagem} 🔔")