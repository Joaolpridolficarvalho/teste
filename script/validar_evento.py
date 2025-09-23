from jsonschema import validate
import json
import os

caminho_esquema = 'script/esquema_evento.json'
with open(caminho_esquema, 'r', encoding='utf-8') as f:
    esquema_evento = json.load(f)
def validar_evento(evento):
    try:
        validate(instance=evento, schema=esquema_evento)
        return True
    except Exception as e:
        print(f"Erro de validação: {e}")
        return False

def carregar_evento_de_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)
    
if __name__ == "__main__":
    # caminho_arquivo_valido = os.path.join(".", "evento_valido.json")
    # caminho_arquivo_invalido = os.path.join(".", "evento_invalido.json")

    # evento_valido = carregar_evento_de_arquivo(caminho_arquivo_valido)
    # evento_invalido = carregar_evento_de_arquivo(caminho_arquivo_invalido)

    # print("Evento Válido:", validar_evento(evento_valido))      # Deve retornar True
    # print("Evento Inválido:", validar_evento(evento_invalido))  # Deve retornar False
    caminho_issue = os.path.join(".", "issue_data.json")
    print('resultado:', validar_evento(carregar_evento_de_arquivo(caminho_issue)))
