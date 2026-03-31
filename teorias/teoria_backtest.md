# Teoria do Backtest

## O que é Backtest?

Backtest é o processo de testar uma estratégia de negociação em dados históricos para avaliar sua viabilidade e performance antes de arriscar capital real. Ele simula como a estratégia teria se comportado no passado.

## Importância no Projeto

Neste projeto, o backtest é fundamental para:

- **Validação de Hipóteses:** Verificar se as analogias entre Física e Price Action produzem resultados de negociação positivos e consistentes.
- **Otimização de Parâmetros:** Ajustar variáveis da estratégia (como períodos de médias, valores de stop) para encontrar a configuração mais robusta.
- **Análise de Risco:** Entender o drawdown (pior sequência de perdas), a lucratividade e a estabilidade de cada robô.
- **Evitar Erros:** Identificar falhas lógicas na estratégia em um ambiente controlado, sem perdas financeiras.

## Processo de Backtest

1.  **Coleta de Dados:** Utilizar dados históricos do ativo (WIN B3).
2.  **Execução da Estratégia:** Aplicar as regras do robô sobre os dados, candle a candle.
3.  **Análise de Performance:** Gerar um relatório com métricas chave (lucro/prejuízo, fator de lucro, etc.).
4.  **Documentação:** Registrar os resultados e configurações na pasta `resultados_backtest`.
