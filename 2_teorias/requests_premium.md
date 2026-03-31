# Requests Premium — Guia Prático

Este arquivo reúne dicas, exemplos e melhores práticas para aproveitar ao máximo as requests premium no workspace RepoRobos.

---

## Como montar queries eficientes

- Seja objetivo: especifique o ativo, timeframe, filtro e tipo de estratégia.
- Use exemplos de código já existentes (ex: IFR, MME, price action) como referência.
- Sempre peça inputs parametrizáveis, nunca valores hardcoded.
- Solicite comentários explicativos e bloco de ativação/log.

### Exemplo de prompt para robô NTSL

> "Gerar um robô NTSL para WIN, timeframe 60min, entrada por IFR < 20, saída por IFR > 80, com bloco de inputs de risco e log de ativação."

### Exemplo de prompt para backtest Python

> "Criar script Python para backtest de estratégia IFR extremo, usando estrutura da pasta IFR_RSI, salvando resultado em CSV com nome padronizado."

---

## Tabelas de parâmetros comuns

| Parâmetro            | Descrição                                |
| -------------------- | ---------------------------------------- |
| UsarGestaoRisco      | Ativa/desativa gestão de risco           |
| SaldoConta           | Valor inicial da conta                   |
| RiscoDiaPct          | % do saldo para limite diário            |
| RiscoSemanaPct       | % do saldo para limite semanal           |
| MaxStopsConsecutivos | Stops em sequência antes de bloquear     |
| ValorPorPonto        | Valor financeiro por ponto (WIN = 0,20)  |
| DiaSemanaReset       | Dia de reset semanal (2 = segunda-feira) |

---

## Limitações e melhores práticas

- Sempre especifique o timeframe no nome do arquivo.
- Não operar sem stop definido.
- Use filtros de contexto (MME, VWAP, price action) para refinar entradas.
- Documente cada robô com taxa de acerto, descrição e parâmetros.
- Salve resultados de backtest em resultsBackTestTimeframe/.

---

## Dicas para organização

- Mantenha exemplos de código em IFR_RSI/top10/ ou legado/.
- Centralize templates em WorkspaceRobosTrade/instrucao_robos.md.
- Atualize o MAPA_GRUPOS.md para indexar scripts, resultados e teorias.
- Crie snippets para MQL5 e Python em diretório próprio.

---

> Consulte este arquivo antes de enviar requests premium para garantir máxima eficiência e padronização.
