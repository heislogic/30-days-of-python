import os
import shutil

def organizar_arquivos(caminho):

    extensoes = {
        ".jpg": "Imagens",
        ".png": "Imagens",
        ".txt": "Documentos",
        ".pdf": "Documentos",
        ".mp3": "Músicas",
        ".zip": "Compactados"
    }

    for item in os.listdir(caminho):
        item_path = os.path.join(caminho, item)

        if os.path.isfile(item_path):
            _, ext = os.path.splitext (item)
            pasta_destino = extensoes.get(ext.lower() , "Outros")
            destino_path = os.path.join(caminho, pasta_destino)
            os.makedirs(destino_path, exist_ok=True)
            shutil.move(item_path, os.path.join(destino_path, item))
if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta a ser organizada: ")
    organizar_arquivos(caminho)
    print("Arquivos organizados com sucesso!")