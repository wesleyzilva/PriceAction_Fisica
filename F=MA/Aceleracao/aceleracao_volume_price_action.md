# Volume como Aceleração (A) no Price Action

No modelo F = M × A, o volume pode ser usado como aceleração para medir a força do movimento. Veja as principais opções:

## 1. Volume absoluto

$$
A = \text{Volume}
$$
- Usa o volume do próprio candle.
- Simples, mas pode ser distorcido por variações de liquidez.

## 2. Volume relativo à média xxxxxxxxxxxxxxxxx

$$
A = \frac{\text{Volume}}{\text{Média}(N\ \text{períodos})}
$$
- Compara o volume atual com a média dos últimos N candles.
- Destaca candles com volume acima do normal.

## 3. Volume logarítmico

$$
A = \log(\text{Volume})
$$
- Reduz o impacto de volumes extremos.
- Suaviza a aceleração.

## 4. Variação do volume

$$
A = \text{Volume} - \text{Volume}[1]
$$
- Mede o quanto o volume aumentou ou diminuiu em relação ao candle anterior.

## 5. OBV (On Balance Volume) incremental

$$
A = \text{OBV} - \text{OBV}[1]
$$
- Usa a variação do OBV para captar aceleração de fluxo direcional.

## 6. Volume ponderado pelo corpo xxxxxxxxxxxxxxxxxxxxx

$$
A = \text{Volume} \times \frac{|\text{Close} - \text{Open}|}{\text{High} - \text{Low}}
$$
- Dá mais peso ao volume quando o candle é direcional.

### Explicação detalhada:

O volume ponderado pelo corpo busca identificar quando o volume realmente "empurrou" o preço em uma direção. Ele faz isso multiplicando o volume pelo fator direcional do candle:

- Se o corpo do candle (|Close - Open|) for grande em relação ao range (High - Low), significa que o preço se moveu de forma decidida, sem muita rejeição.
- Se o corpo for pequeno e as sombras grandes, mesmo com volume alto, o movimento foi de indecisão ou rejeição, então a aceleração é reduzida.

**Vantagens:**
- Filtra candles de indecisão (doji, martelo, etc.), pois eles terão aceleração baixa mesmo com volume alto.
- Dá mais peso a candles direcionais, onde o volume realmente "empurrou" o preço.
- Ajuda a identificar movimentos fortes e evitar sinais falsos em congestão.

**Exemplo prático:**
- Dois candles com o mesmo volume:
    - Candle 1: Corpo grande, sombras pequenas → aceleração alta.
    - Candle 2: Corpo pequeno, sombras grandes → aceleração baixa.

Assim, você foca nos movimentos em que o volume foi acompanhado de decisão no preço, tornando o modelo mais robusto para identificar força real do mercado.

---

## Qual usar em timeframes de 1 minuto?

Para gráficos de 1 minuto, o mais indicado é:

### Volume relativo à média

$$
A = \frac{\text{Volume}}{\text{Média}(N\ \text{períodos})}
$$
- Normaliza o volume, compensando variações naturais de liquidez.
- Destaca candles realmente atípicos para o período.

Ou, para maior robustez:

### Volume relativo à média ponderado pelo corpo

$$
A = \frac{\text{Volume}}{\text{Média}(N)} \times \frac{|\text{Close} - \text{Open}|}{\text{High} - \text{Low}}
$$
- Só há aceleração relevante quando o volume está acima da média e o candle é direcional.
- Reduz falsos positivos em períodos de congestão.

---

**Dica:**
Teste diferentes abordagens e veja qual responde melhor ao seu ativo e timeframe. O volume como aceleração pode ser combinado com diferentes definições de massa para criar modelos de força personalizados no price action.