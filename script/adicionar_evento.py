import json

def carregar_dados_issues():
    
    with open('issue_data.json', 'r') as file:
        return json.load(file)
    
def imprimir_issue(issue):
    print("Arquivo: script/adicionar_evento.py")
    print(issue)

if __name__ == "__main__":
    dados_issues = carregar_dados_issues()
    imprimir_issue(dados_issues)
