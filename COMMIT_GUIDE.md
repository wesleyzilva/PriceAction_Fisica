# Guia de Commits Automáticos

## Padrão de Mensagens de Commit

Este projeto segue o padrão **Conventional Commits** para manter o histórico limpo e automatizável.

### Formato Padrão

```
<tipo>(<escopo>): <descrição breve>

<corpo opcional>

<rodapé opcional>
```

### Tipos de Commit

- **feat**: Nova funcionalidade
- **fix**: Correção de bug
- **docs**: Alterações em documentação
- **style**: Formatação, sintaxe (não afeta lógica)
- **refactor**: Refatoração de código
- **perf**: Melhorias de performance
- **test**: Adição/alteração de testes
- **chore**: Tarefas gerais (deps, build, etc)
- **data**: Adição/alteração de dados ou arquivos de análise

### Escopos Comuns

- `core`: Funcionalidade principal
- `analise`: Análises e scripts
- `docs`: Documentação
- `config`: Configuração do projeto
- `robo`: Robôs de Price Action
- `gradiente`: Sistema de cores e gradientes

### Exemplos

```
feat(robo): Adicionar sistema de gradiente de cores Version 3

docs: Atualizar manual final de Price Action Física

data(analise): Adicionar dados de backtest 2024_26

chore: Organizar arquivos de teoria e operacional
```

## Convenção para Mensagens Automáticas

Quando Claude faça commits, ele usará este padrão baseado no tipo de alteração:

### Nova Adição de Arquivos/Pastas
```
feat: Adicionar [descrição dos arquivos]

- Inclui [lista dos itens principais]
```

### Atualização de Documentação
```
docs: Atualizar [qual doc]

Atualizações incluem [mudanças principais]
```

### Reorganização de Dados
```
chore: Organizar estrutura do projeto

- [alterações realizadas]
```

## Timestamp no Commit

Todo commit deve incluir a hora no final da mensagem para facilitar rastreamento no log:

```bash
git commit -m "Descrição da mudança [$(date +%d/%m\ %H:%M)]"
```

Resultado no log:
```
a041c67  feat(robo): novo esquema de cores [01/04 14:32]
```

> Funciona no bash do Git for Windows (MINGW64).

---

## Como Claude Gerará Mensagens

1. Analisa os arquivos alterados
2. Identifica o tipo primário (feat, docs, chore, etc)
3. Cria mensagem descritiva seguindo o padrão
4. Inclui timestamp `[DD/MM HH:MM]` no final
5. Inclui contexto relevante no corpo

## Configuração

Esta convenção é aplicada automaticamente em commits feitos via Claude Code. Para commits manuais, mantenha este padrão.
