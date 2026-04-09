import os
import shutil

def organizar_arquivos(caminho):
    if not os.path.exists(caminho):
        print(f"❌ Erro: O caminho '{caminho}' não foi encontrado.")
        return

    extensoes = {
        ".jpg": "Imagens",
        ".png": "Imagens",
        ".txt": "Documentos",
        ".pdf": "Documentos",
        ".mp3": "Músicas",
        ".zip": "Compactados"
    }

    print(f"🧹 Organizando: {caminho}...")
    contagem = 0

    for item in os.listdir(caminho):
        item_path = os.path.join(caminho, item)

        if os.path.isfile(item_path):
            if item == "main.py":
                continue

            _, ext = os.path.splitext (item)
            pasta_destino = extensoes.get(ext.lower() , "Outros")

            destino_path = os.path.join(caminho, pasta_destino)
            os.makedirs(destino_path, exist_ok=True)

            shutil.move(item_path, os.path.join(destino_path, item))
            print(f" [>] {item} -> {pasta_destino}")
            contagem += 1

    print (f"\n✅ Organização concluída! Total de arquivos organizados: {contagem}")

if __name__ == "__main__":
    pasta = input("📂 Digite o caminho da pasta a ser organizada: ")
    try:
        organizar_arquivos(pasta)
    except Exception as e:
        print(f"❌ Erro: {e}")