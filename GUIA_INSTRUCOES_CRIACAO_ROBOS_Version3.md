# 📝 GUIA DE INSTRUÇÕES - COMO CRIAR ROBÔS

**Status**: ✅ Instruções completas  
**Data**: 12/03/2026  
**Versão**: 1.0

---

## 📖 ÍNDICE

1. [Instruções de Criação de Robôs](#instruções-de-criação-de-robôs)
2. [Timeframe: Candlestick vs Renko](#timeframe-candlestick-vs-renko)
3. [Quando Usar Cada Um](#quando-usar-cada-um)
4. [Recomendações Finais](#recomendações-finais)

---

## 📝 INSTRUÇÕES DE CRIAÇÃO DE ROBÔS

### INSTRUÇÃO 1: Definição de Padrão

```
"Crie um robô baseado em [PADRÃO]"

Padrões disponíveis:
✅ Rompimento (Breakout)
✅ Martelo (Hammer)
✅ Estrela (Star)
✅ Rejeição Forte
✅ Anomalia de Volume
✅ Continuação
✅ Divergência
✅ Price Action puro
✅ Fusão de padrões
```

**Exemplo:**
```
"Crie um robô baseado em ROMPIMENTO com confirmação de REJEIÇÃO"
```

---

### INSTRUÇÃO 2: Ativo e Timeframe

```
"Use [ATIVO] em timeframe [TIMEFRAME]"

Ativos:
✅ WIN B3 (índice futuro mini)
✅ WIN (índice futuro)
✅ Outros ativos

Timeframes:
✅ 1 minuto (scalping)
✅ 5 minutos (day trade rápido)
✅ 15 minutos (day trade)
✅ 30 minutos (day trade)
✅ 60 minutos (swing)
✅ 4 horas (swing)
✅ Diário (swing/posição)
✅ Renko (volatilidade)
```

**Exemplo:**
```
"Use WIN B3 em timeframe de 60 minutos"
```

---

### INSTRUÇÃO 3: Cores e Gradiente

```
"Aplique gradiente [TIPO]"

Tipos de gradiente:
✅ Branco-Verde-Vermelho (padrão - RECOMENDADO)
✅ Apenas força (sem padrões especiais)
✅ Com padrões especiais (Laranja, Amarelo)
```

**Exemplo:**
```
"Aplique gradiente branco-verde-vermelho com cores especiais 
(Laranja para rejeição, Amarelo para anomalia)"
```

---

### INSTRUÇÃO 4: Validações

```
"Valide com [VALIDAÇÃO]"

Validações disponíveis:
✅ RRR (Razão Risco/Recompensa) ≥ 1.0
✅ Força mínima (F > +40% ou F < -40%)
✅ Volume mínimo (2x, 3x média)
✅ Padrão confirmado
✅ Multi-timeframe
✅ Média móvel
✅ Oscilador (RSI, MACD, etc)
```

**Exemplo:**
```
"Valide com RRR ≥ 1.2 e Força ≥ +50% para compra"
```

---

### INSTRUÇÃO 5: Gestão de Posição

```
"Aplique gestão de risco [TIPO]"

Tipos:
✅ Stop Loss = Range × 1.5
✅ Take Profit = ATR × 2
✅ Trailing Stop (acompanha movimento)
✅ Múltiplas saídas (parcial, total)
✅ Gestão dinâmica (ajusta com tempo)
```

**Exemplo:**
```
"SL = Range × 1.5, TP = ATR × 2, Saída por tempo às 17:00"
```

---

### INSTRUÇÃO 6: Saída

```
"Configure saída por [CONDIÇÃO]"

Condições:
✅ Horário fixo (17:00, 16:00, etc)
✅ Barras em posição (máximo 8 barras)
✅ Reversão de padrão
✅ Quebra de média móvel
✅ Toque de suporte/resistência
```

**Exemplo:**
```
"Feche todas as posições às 17:00 (sem overnight)"
```

---

### INSTRUÇÃO 7: Parâmetros Ajustáveis

```
"Configure inputs [PARÂMETROS]"

Parâmetros comuns:
✅ VolumeMinimo(2000)
✅ CapitalConta(10000)
✅ RiscoPorcentagem(2.0)
✅ ATRMultiplicador(2.0)
✅ PeriodoMedia(20)
✅ ForcaMinima(40)
✅ MaxBarrasPosicao(8)
```

**Exemplo:**
```
"VolumeMinimo(2000), RiscoPorcentagem(2.0), MaxBarrasPosicao(8)"
```

---

## 🕯️ TIMEFRAME: CANDLESTICK vs RENKO

### Candlestick (Padrão - RECOMENDADO)

```
O QUE É:
- Vela baseada em TEMPO
- 1 minuto = 1 vela de 1 min
- 60 minutos = 1 vela de 1 hora
- Cada período = 1 vela

CARACTERÍSTICAS:
✅ Preço pode não mudar muito
✅ Pode ter velas com corpo pequeno
✅ Bom para tendências claras
✅ Melhor para padrões tradicionais

VANTAGENS:
✅ Compatível com Price Action clássico
✅ Força física (F = M × A) funciona bem
✅ Padrões martelo/estrela aparecem
✅ Bom para consolidações

DESVANTAGENS:
❌ Velas fracas podem confundir
❌ Consolidação fica lenta
❌ Muitos sinais falsos em sideways

EXEMPLO:
10:00 - Vela 1 min abertura
10:01 - Vela 1 min fechamento (mesmo que não tenha movimento)
10:02 - Próxima vela 1 min...
```

---

### Renko (Volatilidade - ALTERNATIVO)

```
O QUE É:
- Vela baseada em VOLATILIDADE (não em tempo)
- 1 brick = movimento pré-definido (ex: 100 pontos)
- Nova vela só forma quando preço move essa quantidade
- Ignora o tempo

CARACTERÍSTICAS:
✅ Foca em movimento puro
✅ Remove "ruído" de consolidação
✅ Velas mais "limpas"
✅ Tendências mais claras
✅ Menos velas, mais significância

VANTAGENS:
✅ Filtra ruído de sideways
✅ Padrões mais claros
✅ Reduz sinais falsos
✅ Bom para tendências fortes

DESVANTAGENS:
❌ Difícil configurar "brick size" ideal
❌ Menos compatível com Time-based
❌ Padrões podem deformar
❌ Força F = M × A muda de interpretação

EXEMPLO:
Brick size = 100 pontos

Preço 70.000 → Vela 1 abre
Preço 70.050 → Nada (apenas +50)
Preço 70.100 → Nada (apenas +100 total)
Preço 70.110 → Vela 1 fecha, Vela 2 abre (passou de 100)
Preço 70.200 → Vela 2 fecha (mais 100)
Preço 70.150 → Nada (voltou)
Preço 70.300 → Vela 3 forma
```

---

## 🎯 QUANDO USAR CADA UM

### Use CANDLESTICK (60 min) SE:

```
✅ Quer Price Action tradicional
✅ Trabalha com padrões clássicos (martelo, estrela)
✅ Prefere padrões visuais claros
✅ Quer usar força F = M × A sem modificações
✅ Foca em rompimentos com confirmação
✅ Opera durante pregão (09:00 a 17:00)
✅ Quer simplicidade

RECOMENDADO PARA:
- Iniciantes
- Price Action puro
- Robôs baseados em força
- Estratégias de rompimento
- Padrões de candle
```

### Use RENKO SE:

```
⚠️ Quer filtrar ruído extremo
⚠️ Mercado está em forte tendência
⚠️ Quer focar apenas em movimento
⚠️ Tem experiência com Renko
⚠️ Quer menos sinais (melhor qualidade)

RECOMENDADO PARA:
- Traders avançados
- Tendências muito fortes
- Filtro de ruído
- Escalações de posição
- Breakouts puros
```

---

## 📊 COMPARAÇÃO PRÁTICA

```
CENÁRIO: Consolidação de 1 hora (70.000-70.100)

CANDLESTICK (60 min):
┌──────────────┐
│ Várias velas │ ← Muitas pequenas velas
│ Pequenas     │ ← Podem gerar sinais falsos
│ ░░░░░░░░░░  │
└──────────────┘
Resultado: Muitos "ruídos", possíveis sinais falsos

RENKO (100 pts):
┌──────────────┐
│ 1 vela       │ ← Uma vela limpinha
│ Só vai       │ ← Quando romper 70.100
│ Quando move  │
└──────────────┘
Resultado: Limpo, sem ruído, sinal verdadeiro
```

---

## 🎯 RECOMENDAÇÃO FINAL

### Para sua estratégia de Price Action Física:

```
MELHOR ESCOLHA: CANDLESTICK 60 MINUTOS ⭐

MOTIVOS:
✅ Força F = M × A funciona perfeitamente
✅ Padrões visuais muito claros
✅ Gradiente RGB faz sentido com tempo
✅ Price Action tradicional se aplica
✅ Fácil de parametrizar
✅ Compatível com todos os padrões
✅ Backtest mais confiável
✅ Padrão na indústria

CONFIGURAÇÃO IDEAL:
- Ativo: WIN B3 (ou WIN)
- Timeframe: 60 minutos
- Gradiente: Branco-Verde-Vermelho
- Padrões: Todos (rompimento, rejeição, etc)
- Validações: RRR ≥ 1.0, Força ≥ ±40%
- Saída: Horário 17:00
```

---

## 🔄 ALTERNATIVA COM RENKO

Se quiser experimentar Renko depois:

```
RENKO RECOMENDADO (Futuro):
- Ativo: WIN B3
- Brick Size: 100 pontos (começa com isso)
- Apenas para tendências fortes
- Não use força F = M × A (vai distorcer)
- Use apenas padrões (rompimento, rejeição)
```

---

## 📝 TEMPLATE DE INSTRUÇÃO

Use este formato para criar robôs:

```
"Crie um robô [NOME] com as seguintes características:

PADRÃO: [Rompimento / Martelo / Estrela / Rejeição / etc]
ATIVO: WIN B3
TIMEFRAME: 60 minutos

CORES: Gradiente branco-verde-vermelho
       Com Laranja para rejeição
       Com Amarelo para anomalia

VALIDAÇÕES: RRR ≥ 1.0
            Força ≥ +40% (compra) ou ≤ -40% (venda)
            Volume > 2x média

GESTÃO: SL = Range × 1.5
        TP = ATR × 2
        Saída: 17:00

INPUTS: VolumeMinimo(2000)
        CapitalConta(10000)
        RiscoPorcentagem(2.0)
        ATRMultiplicador(2.0)

OBSERVAÇÕES: [Qualquer detalhe especial]"
```

---

## ✅ CHECKLIST ANTES DE PEDIR ROBÔ

- [ ] Padrão definido?
- [ ] Ativo escolhido?
- [ ] Timeframe decidido (candlestick recomendado)?
- [ ] Cores especificadas?
- [ ] Validações listadas?
- [ ] Gestão de risco clara?
- [ ] Saída definida?
- [ ] Inputs ajustados?

---

## 🚀 EXEMPLO DE INSTRUÇÃO COMPLETA

```
"Crie um robô chamado 'Rompimento_Forte_v1' com:

PADRÃO: Rompimento com confirmação de força
ATIVO: WIN B3
TIMEFRAME: 60 minutos (candlestick)

CORES: Gradiente completo
- Verde para compra (F > +40%)
- Vermelho para venda (F < -40%)
- Laranja para rejeição forte
- Amarelo para anomalia volume

VALIDAÇÕES:
- RRR ≥ 1.2 (obrigatório)
- Força ≥ +50% para compra
- Força ≤ -50% para venda
- Volume > 2.5x média

GESTÃO:
- SL = Range × 1.5
- TP = ATR × 2
- Fechar às 17:00

INPUTS:
- VolumeMinimo(2000)
- CapitalConta(10000)
- RiscoPorcentagem(2.0)
- ATRMultiplicador(2.0)

Descrição: Robô que detecta rompimentos
validados por força forte e anomalia de volume."
```

---

## 📚 REFERÊNCIA RÁPIDA

### Para criar robô, especifique:

```
1. NOME
   "Crie robô chamado [NOME]"

2. PADRÃO
   "Baseado em [PADRÃO]"

3. ATIVO + TIMEFRAME
   "USE [ATIVO] em [TIMEFRAME]"
   → Recomendado: WIN B3 + 60 min

4. CORES
   "Aplique [TIPO DE CORES]"
   → Padrão: Branco-Verde-Vermelho

5. VALIDAÇÕES
   "Valide com [VALIDAÇÕES]"
   → Mínimo: RRR ≥ 1.0, Força

6. GESTÃO
   "SL = [FÓRMULA], TP = [FÓRMULA]"
   → Padrão: Range × 1.5, ATR × 2

7. INPUTS
   "Configure [PARÂMETROS]"
   → Padrão: VolumeMinimo, Capital, Risco

8. SAÍDA
   "Feche em [CONDIÇÃO]"
   → Padrão: 17:00
```

---

## 🎯 RESUMO FINAL

```
MELHOR CONFIGURAÇÃO PARA SEUS ROBÔS:

✅ Ativo: WIN B3
✅ Timeframe: 60 minutos (candlestick)
✅ Cores: Gradiente branco-verde-vermelho
✅ Validações: RRR ≥ 1.0, Força ≥ ±40-50%
✅ Gestão: SL = Range × 1.5, TP = ATR × 2
✅ Saída: 17:00
✅ Padrões: Todos (rompimento, rejeição, martelo, etc)

Renko? Deixe para depois quando tiver experiência avançada.
```

---

**Versão**: 1.0 - Guia completo de instruções  
**Status**: ✅ PRONTO PARA USAR