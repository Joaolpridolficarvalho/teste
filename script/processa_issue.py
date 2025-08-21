import os
import json
import subprocess
import re

NOME_ARQUIVO = "issue.json"

def parse_issue(arquivo: str) -> dict:
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()

    resultado = {}

    # Captura título
    titulo = re.search(r"Título:\s*(.*)", texto)
    if titulo:
        resultado["Título"] = titulo.group(1).strip()

    # Captura e remove bloco Labels
    labels = re.search(r"Labels:\s*(\[[\s\S]*])", texto)
    if labels:
        m_label_name = re.search(r"name:\s*([^\s,]+)", labels.group(1))
        if m_label_name:
            resultado["Label"] = m_label_name.group(1).strip()
        texto = texto[:labels.start()]

    # Captura campos do corpo (### Campo)
    padrao = re.compile(r"###\s*(.*?)\n\n(.*?)(?=\n###|\Z)", re.DOTALL)
    matches = padrao.findall(texto)

    for campo, valor in matches:
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
        print(f'A issue referente ao evento "{titulo}" possui a label "{label}".')
        # subprocess.run(["py", scripts[label], str(issue.get("id", ""))], check=True)
    else:
        print("Nenhum script correspondente à label encontrada.")


if __name__ == "__main__":
    import sys
    arquivo = sys.argv[1]
    issue = parse_issue(arquivo)
    processa_issue(issue)
