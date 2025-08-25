import re
import json

NOME_ARQUIVO = "./crud_liquido_issue.json"
def parse_issue() -> dict:
    """
    Recebe um JSON de issue do GitHub (dict) e retorna outro JSON (dict)
    com os campos do body estruturados + label principal.
    """
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
        issue = json.load(f)
    # pega só o nome do primeiro label (se existir)
    labels = [label["name"] for label in issue.get("labels", [])]
    label = labels[0] if labels else ""

    resultado = {
        "number": str(issue.get("number", "")),
        "title": issue.get("title", ""),
        "label": label,
        "labels": labels,
    }

    body = issue.get("body", "")

    # Extrair blocos do tipo ### Campo \n valor
    padrao_markdown = re.compile(r"###\s*(.*?)\n+([^#]+)", re.DOTALL)
    for campo, valor in padrao_markdown.findall(body):
        chave = campo.strip().lower().replace(" ", "_")
        resultado.append({chave: valor.strip()})

    # Extrair blocos do tipo **Campo**: valor
    padrao_negrito = re.compile(r"\*\*(.*?)\*\*:\s*(.*)")
    for campo, valor in padrao_negrito.findall(body):
        chave = campo.strip().lower().replace(" ", "_")
        resultado[chave] = valor.strip()

    # label

    return resultado


# Exemplo de uso
if __name__ == "__main__":
    issue = {
        "number": "7",
        "title": "adicionar evento",
        "body": """### Nome do Evento

teste 333333333

### Formato do Evento

Remoto

### Ano do Evento

2025
### Descrição
teste 3333333
### data do evento
2025-12-31
### Link do Evento
https://www.teste.com
""",
        "labels": [
            {"name": "adicionar"}
        ],
        "user": "Joaolpridolficarvalho"
    }

    parsed = parse_issue()
    print(json.dumps(parsed, indent=2, ensure_ascii=False))
