# Instruções para Execução de Backtests

Este guia descreve o processo para realizar backtests das estratégias desenvolvidas neste repositório.

## 1. Configuração do Ambiente

- **Plataforma:** Profit Pro
- **Ativo:** Mini-índice (WIN)
- **Período de Teste:** Definir o intervalo de datas desejado.
- **Custos:** Configurar custos operacionais (emolumentos, corretagem) para um resultado mais realista.

## 2. Selecionando a Estratégia

1.  Abra o "Editor de Estratégias" no Profit.
2.  Importe o arquivo `.ntsl` desejado da pasta `robos/`.
3.  Compile a estratégia para verificar se há erros de sintaxe.

## 3. Executando o Backtest

1.  No gráfico do ativo (WIN), clique com o botão direito e vá para "Inserir Estratégia de Execução".
2.  Selecione a estratégia importada.
3.  Configure os parâmetros de entrada da estratégia, se houver.
4.  Acesse o "Relatório de Performance" para analisar os resultados.

## 4. Análise de Resultados

Analise métricas como: Fator de Lucro, Saldo Líquido, Número de Trades, Taxa de Acerto e Drawdown. Documente os resultados na pasta `resultados_backtest/`.
