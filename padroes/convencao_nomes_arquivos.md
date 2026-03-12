# Convenção de Nomes de Arquivos

A estrutura de nomenclatura de arquivos é projetada para garantir organização e clareza, permitindo identificar rapidamente o propósito de cada robô.

## Estrutura

`Código mar_IDunicocomLetraeNumero_priceactionfisica_60min.ntsl`

### Componentes:

- **mar**: Mês do ciclo de desenvolvimento ou da versão do robô (ex: jan, fev, mar).
- **IDunicocomLetraeNumero**: Identificador único que mistura letras e números para versionamento (ex: A1B2C3, V2X5, R10).
- **priceactionfisica**: Grupo de conceito ao qual o robô pertence.
- **60min**: Timeframe no qual o robô foi projetado para operar (ex: 1min, 5min, 15min, 60min).
- **.ntsl**: Extensão obrigatória para estratégias na plataforma Profit.

### Exemplos Válidos

- `mar_A1B2C3_priceactionfisica_60min.ntsl`
- `abr_X9Y8Z7_priceactionfisica_15min.ntsl`
- `mai_KL45MN_priceactionfisica_5min.ntsl`
