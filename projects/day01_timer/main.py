import time

minutos_usuario = int(input("Quantos minutos deseja configurar no timer?"))
segundos_totais = minutos_usuario * 60

print(f"Timer de {minutos_usuario} minutos iniciado!")

try:
    while segundos_totais > 0:
        minutos_restantes = segundos_totais // 60
        segundos_restantes = segundos_totais % 60

        timer = f"{minutos_restantes:02d}:{segundos_restantes:02d}"

        print(f"Foco total: {timer}", end="\r")

        time.sleep(1)
        segundos_totais -= 1

    print("\n✅ TEMPO ESGOTADO! Vá descansar.")
except KeyboardInterrupt:
    print("\n\nTimer interrompido pelo usuário. Até a próxima!")