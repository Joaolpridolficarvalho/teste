## Descrição
Adiciona filtro para processar somente issues com o label "evento:adicionar".

## Mudanças Propostas
- Atualiza o arquivo `.github/workflows/adicionar_evento.yml`.
## Benefícios da Mudança
Permite fazer o processamento apenas de issues relevantes, evitando ações desnecessárias.

## Como Testar
Crie ou edite uma issue com o label "evento:adicionar" e uma issue sem esse label. Verifique se o workflow exibe um 'check' apenas para a issue com o label.

## Anexos



## Checklist de Revisão
<!--- Marque as caixas que se aplicam. Você pode deixar caixas desmarcadas se elas não se aplicarem.-->
- [x] Eu testei minhas mudanças localmente e/ou em um repositório de teste.
- [x] Eu certiifiquei que meu código segue as diretrizes de estilo do projeto.
- [x] Eu certiifiquei que a branch contém apenas mudanças relacionadas a este Pull Request.


## Issue Relacionada
<!---Todos os PRs devem ter uma issue relacionada. Dessa forma, podemos garantir que ninguém perca tempo trabalhando em algo que não precisa ser feito. -->

Closes #43
