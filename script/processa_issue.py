import os
import json
import subprocess
import re
from cProfile import label

# def normaliza_label(label):
#     return label.strip().lower()
NOME_ARQUIVO = 'issue.json'



def parse_issue(arquivo: str) -> dict:
    with open(arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()

    resultado = {}
    # Captura título
    titulo = re.search(r"Título:\s*(.*)", texto)
    if titulo:
        resultado["Título"] = titulo.group(1).strip()

    # Captura e remove bloco Labels
    labels = re.search(r"Labels:\s*(\[[\s\S]*])", texto)

    if labels:
        # Pega apenas o name
        m_label_name = re.search(r"name:\s*([^\s,]+)", labels.group(1))
        if m_label_name:
            resultado["Label"] = m_label_name.group(1).strip()

        # Remove o trecho de Labels do texto
        texto = texto[:labels.start()]


    # Captura os campos do corpo
    padrao = re.compile(r"###\s*(.*?)\n\n(.*?)(?=\n###|\Z)", re.DOTALL)
    matches = padrao.findall(texto)

    for campo, valor in matches:
        resultado[campo.strip()] = valor.strip()


    base, _ = os.path.splitext(arquivo)
    nome_saida = f"{base}.json"
    with open(nome_saida, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)
    return resultado
def processa_issue(issue: dict) -> None:
    labels = issue.get("Label", "")
    titulo = issue.get("Título", "")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scripts = {
        'adicionar': os.path.join(base_dir, 'adicionar_evento.py'),
        'atualizar': os.path.join(base_dir, 'atualizar_evento.py'),
        'remover': os.path.join(base_dir, 'excluir_evento.py')
    }

    for label in labels:
        if label in scripts:
            print('A issue referente ao evento "{}" possui a label "{}".'.format(titulo, label))
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
    parse_issue(arquivo)
