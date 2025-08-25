import os
import json
import re
import subprocess
import sys

NOME_ARQUIVO = "issue.json"
def parse_issue_github_generico(arquivo: str) -> dict:
    """Lê uma issue do GitHub e retorna todos os campos estruturados em JSON."""
    with open(arquivo, "r", encoding="utf-8") as f:
        data = json.load(f)

    resultado = {
        "number": str(data.get("number", "")),
        "title": data.get("title", ""),
        "author": data.get("user", ""),
        "labels": [label["name"] for label in data.get("labels", [])]
    }

    body = data.get("body", "")

    # Captura campos no formato ### Campo \n valor
    padrao_markdown = re.compile(r"###\s*(.*?)\n(.*?)(?=\n###|\Z)", re.DOTALL)
    for campo, valor in padrao_markdown.findall(body):
        chave = campo.strip().lower().replace(" ", "_")
        resultado[chave] = valor.strip()

    # Captura campos no formato **Campo**: valor
    padrao_negrito = re.compile(r"\*\*(.*?)\*\*:\s*(.*)")
    for campo, valor in padrao_negrito.findall(body):
        chave = campo.strip().lower().replace(" ", "_")
        resultado[chave] = valor.strip()

    return resultado

def processa_issue(issue: dict) -> None:
    label = issue.get("Label", "")
    titulo = issue.get("Título", "")
    base_dir = os.path.dirname(os.path.abspath(__file__))

    scripts = {
        "adicionar": os.path.join(base_dir, "adicionar_evento.py"),
        "atualizar": os.path.join(base_dir, "atualizar_evento.py"),
        "remover": os.path.join(base_dir, "excluir_evento.py")
    }

    if label in scripts:
        print(f'A issue "{titulo}" possui a label "{label}".')
        # subprocess.run([sys.executable, scripts[label], issue.get("Número", "")], check=True)
    else:
        print("Nenhum script correspondente à label encontrada.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_issue_json>")
        exit(1)

    arquivo = sys.argv[1]
    issue = parse_issue_github_generico(arquivo)
    processa_issue(issue)
