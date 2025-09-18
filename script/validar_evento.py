from jsonschema import validate
import json
import os
esquema_evento = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Evento",
  "type": "object",
  "properties": {
    "Nome do Evento": {
      "type": "string"
    },
    "Site do Evento": {
      "type": "string",
      "format": "uri"
    },
    "Formato do Evento": {
      "type": "string",
      "enum": ["Online", "Híbrido", "Presencial"]
    },
    "Cidade": {
      "type": ["string", "null"]
    },
    "Estado/Província": {
      "type": ["string", "null"]
    },
    "País": {
      "type": ["string", "null"]
    },
    "Ano do primeiro dia de Evento": {
      "type": "integer",
      "minimum": 1900
    },
    "Mês do primeiro dia de Evento": {
      "type": "string"
    },
    "Dia do primeiro dia de Evento": {
      "type": "integer",
      "minimum": 1,
      "maximum": 31
    },
    "Ano do último dia de Evento": {
      "type": "integer",
      "minimum": 1900
    },
    "Mês do último dia de Evento": {
      "type": "string"
    },
    "Dia do último dia de Evento": {
      "type": "integer",
      "minimum": 1,
      "maximum": 31
    },
    "Ano do primeiro dia de Submissão": {
      "type": "integer",
      "minimum": 1900
    },
    "Mês do primeiro dia de Submissão": {
      "type": "string"
    },
    "Dia do primeiro dia de Submissão": {
      "type": "integer",
      "minimum": 1,
      "maximum": 31
    },
    "Ano do último dia de Submissão": {
      "type": "integer",
      "minimum": 1900
    },
    "Mês do último dia de Submissão": {
      "type": "string"
    },
    "Dia do último dia de Submissão": {
      "type": "integer",
      "minimum": 1,
      "maximum": 31
    },
    "Tipos de Submissão aceitos": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "Palestra",
          "Workshop",
          "Lightning talk",
          "Painel",
          "Tutorial",
          "Minicurso",
          "Outros"
        ]
      },
      "uniqueItems": True
    },
    "Se marcou “Outros”, especifique": {
      "type": ["string", "null"]
    }
  },
  "required": [
    "Nome do Evento",
    "Site do Evento",
    "Formato do Evento",
    "Ano do primeiro dia de Evento",
    "Mês do primeiro dia de Evento",
    "Dia do primeiro dia de Evento",
    "Ano do último dia de Evento",
    "Mês do último dia de Evento",
    "Dia do último dia de Evento",
    "Ano do primeiro dia de Submissão",
    "Mês do primeiro dia de Submissão",
    "Dia do primeiro dia de Submissão",
    "Ano do último dia de Submissão",
    "Mês do último dia de Submissão",
    "Dia do último dia de Submissão",
    "Tipos de Submissão aceitos"
  ]
}
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
    caminho_arquivo_valido = os.path.join(".", "evento_valido.json")
    caminho_arquivo_invalido = os.path.join(".", "evento_invalido.json")

    evento_valido = carregar_evento_de_arquivo(caminho_arquivo_valido)
    evento_invalido = carregar_evento_de_arquivo(caminho_arquivo_invalido)

    print("Evento Válido:", validar_evento(evento_valido))      # Deve retornar True
    print("Evento Inválido:", validar_evento(evento_invalido))  # Deve retornar False
