# Teoria: Online vs. Atraso (Tempo Real vs. Dados Históricos)

## Contexto

No desenvolvimento e teste de estratégias de negociação, lidamos com dois cenários de dados:

1.  **Dados Históricos (Atraso):** São os dados passados, utilizados para realizar backtests. O robô processa os candles "depois" que eles fecharam. Isso permite uma análise rápida de longos períodos, mas pode mascarar o comportamento real do preço.

2.  **Dados em Tempo Real (Online):** São os dados que chegam tick a tick durante o pregão ao vivo. A estratégia reage a cada mudança de preço. Este é o ambiente real de operação (seja em simulação ou conta real).

## Implicações para os Robôs

Uma estratégia pode ter um desempenho excelente no backtest (com dados em atraso) e falhar em tempo real. Isso ocorre porque o backtest padrão geralmente não simula o movimento do preço _dentro_ do candle (repintura). Por exemplo, um stop pode ser violado e depois o preço voltar, algo que o backtest simples pode não capturar.

É crucial validar o desempenho de um robô em ambiente de simulação (online) por um tempo relevante antes de confiar nos resultados do backtest.
