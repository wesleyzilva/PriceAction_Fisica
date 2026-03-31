# Massa no Price Action: Corpo e Sombras do Candle

## Conceito de Massa
No contexto de price action, a "massa" representa o peso ou a importância de um movimento de preço. Ela pode ser usada para filtrar movimentos realmente relevantes, ignorando candles de indecisão ou rejeição.

## Como calcular a massa considerando corpo e sombras

### 1. Massa proporcional ao corpo

$$
M = \frac{\text{Close} - \text{Open}}{\text{High} - \text{Low}}
$$

- Candles com corpo grande em relação ao range total têm mais massa.
- Candles com corpo pequeno e sombras grandes têm menos massa (mais indecisão).

### 2. Massa ponderada pelas sombras

$$
\text{Sombras} = (\text{High} - \max(\text{Close}, \text{Open})) + (\min(\text{Close}, \text{Open}) - \text{Low})
$$

$$
M = (\text{Close} - \text{Open}) \times \left(1 - \frac{\text{Sombras}}{\text{High} - \text{Low}}\right)
$$

- Quanto maior a proporção de sombras, menor a massa.
- Candles de rejeição (martelo, doji) terão massa reduzida.

### 3. Massa = Range ponderado pelo corpo

$$
M = (\text{High} - \text{Low}) \times \frac{|\text{Close} - \text{Open}|}{\text{High} - \text{Low}}
$$

- Só há massa relevante se o corpo for significativo no contexto do range.

## Interpretação
- **Alta massa:** Movimento decidido, direção clara, pouca rejeição.
- **Baixa massa:** Indecisão, rejeição, possível reversão ou pausa na tendência.

## Aplicação prática
- Use a massa para filtrar sinais falsos e dar mais peso a movimentos realmente direcionais.
- Combine a massa com volume ou OBV para calcular a força (F = M × A) de cada candle.

---

**Resumo:**
A massa pode ser ajustada conforme o seu objetivo operacional, mas sempre representa o quanto o movimento do candle foi "decidido" e relevante no contexto do preço.