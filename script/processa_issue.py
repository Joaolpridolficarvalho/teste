import os
import json
import re
import subprocess

NOME_ARQUIVO = "issue.json"

def parse_issue_github_generico(arquivo: str) -> dict:
    """Lê uma issue do GitHub e extrai todos os campos automaticamente."""
    with open(arquivo, "r", encoding="utf-8") as f:
        data = json.load(f)

    resultado = {
        "Título": data.get("title", ""),
        "Body": data.get("body", ""),
        "Label": data["labels"][0]["name"] if data.get("labels") else ""
    }

    # Regex para capturar todos os campos do tipo **Campo**: valor
    padrao_campo = re.compile(r"\*\*(.*?)\*\*:\s*(.*)")
    for match in padrao_campo.findall(resultado["Body"]):
        campo, valor = match
        resultado[campo.strip()] = valor.strip()

    # Salva no JSON fixo
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)

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
        # subprocess.run(["py", scripts[label], str(issue.get("number", ""))], check=True)
    else:
        print("Nenhum script correspondente à label encontrada.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_issue_json>")
        exit(1)

    arquivo = sys.argv[1]
    issue = parse_issue_github_generico(arquivo)
    processa_issue(issue)
