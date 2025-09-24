from jsonschema import validate
import json
import os

# Descobre a pasta onde este script está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto do arquivo de esquema
caminho_esquema = os.path.join(BASE_DIR, "esquema.json")

with open(caminho_esquema, "r", encoding="utf-8") as f:
    esquema_evento = json.load(f)

def validar_evento(evento):
    try:
        validate(instance=evento, schema=esquema_evento)
        return True
    except Exception as e:
        print(f"Erro na validação: {e}")
        return False

def carregar_evento_de_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

if __name__ == "__main__":
    # Exemplos de uso
    # caminho_arquivo_valido = os.path.join(BASE_DIR, "evento_valido.json")
    # caminho_arquivo_invalido = os.path.join(BASE_DIR, "evento_invalido.json")

    # evento_valido = carregar_evento_de_arquivo(caminho_arquivo_valido)
    # evento_invalido = carregar_evento_de_arquivo(caminho_arquivo_invalido)

    # print("Evento Válido:", validar_evento(evento_valido))    # Deve retornar True
    # print("Evento Inválido:", validar_evento(evento_invalido))  # Deve retornar False

    # Exemplo para o issue_data.json (no repositório raiz)
    caminho_issue = os.path.join(os.path.dirname(BASE_DIR), "issue_data.json")
    if validar_evento(carregar_evento_de_arquivo(caminho_issue)):
        print("issue_data.json é válido.")
        os._exit(0)
    else:
        print("issue_data.json é inválido.")
        os._exit(1)

