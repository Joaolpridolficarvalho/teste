import os
import json
import subprocess
import re

def normaliza_label(label):
    return label.strip().lower()


def parse_issue(issue_json: dict) -> dict:
    body = issue_json.get("body", "")

    # Expressão regular para capturar blocos "### Campo\n\nvalor"
    pattern = r"### (.*?)\n\n(.*?)(?=\n###|$)"
    matches = re.findall(pattern, body, re.DOTALL)

    parsed_fields = {}
    for key, value in matches:
        parsed_fields[key.strip()] = value.strip()

    result = {
        "number": issue_json.get("number"),
        "title": issue_json.get("title"),
        "user": issue_json.get("user"),
        "labels": [label["name"] for label in issue_json.get("labels", [])],
        "fields": parsed_fields
    }
    return result

def processa_issue(arquivo: dict) -> None: 
    print(f"Processando issue do arquivo: {arquivo}")
    
    nome_evento = arquivo.get('title', 'Evento sem título')
    labels = arquivo.get('labels', [])
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scripts = {
        'adicionar': os.path.join(base_dir, 'adicionar_evento.py'),
        'atualizar': os.path.join(base_dir, 'atualizar_evento.py'),
        'remover': os.path.join(base_dir, 'excluir_evento.py')
    }

    for label in labels:
        if label in scripts:
            print('A issue referente ao evento "{}" possui a label "{}".'.format(nome_evento, label))
            # subprocess.run(
            #     ["py", scripts[label], str(issue['id'])],
            #     check=True
            # )
            break  # executa só o primeiro script que encontrar correspondente
    else:
        print("Nenhum script correspondente às labels encontrado.")

if __name__ == "__main__":
    import sys
    arquivo = sys.argv[1]
    processa_issue(arquivo)
