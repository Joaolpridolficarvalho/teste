## Descrição
Modifica o workflow para executar o script `adicionar_evento.py` imprimindo o JSON da issue quando uma issue é criada ou editada com o label "🗓️ evento:adicionar" e limpar a saída. 

## Mudanças Propostas
- Atualiza o arquivo `.github/workflows/adicionar_evento.yml`.
- Adiciona o script `backend/adicionar_evento.py` que extrai e imprime o JSON da issue.
## Benefícios da Mudança
Permite melhor organização do código e facilita a manutenção do workflow.

## Como Testar
Crie ou edite uma issue com o label "evento:adicionar" e uma issue sem esse label. Verifique se o workflow exibe o json corretamente.

## Anexos



## Checklist de Revisão
<!--- Marque as caixas que se aplicam. Você pode deixar caixas desmarcadas se elas não se aplicarem.-->
- [x] Eu testei minhas mudanças localmente e/ou em um repositório de teste.
- [x] Eu certiifiquei que meu código segue as diretrizes de estilo do projeto.
- [x] Eu certiifiquei que a branch contém apenas mudanças relacionadas a este Pull Request.


## Issue Relacionada
<!---Todos os PRs devem ter uma issue relacionada. Dessa forma, podemos garantir que ninguém perca tempo trabalhando em algo que não precisa ser feito. -->

Closes #46
