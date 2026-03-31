# 📚 MANUAL FINAL - PRICE ACTION FÍSICA

**Status**: ✅ Manual completo e consolidado  
**Data**: 12/03/2026  
**Versão**: 7.0 FINAL  
**Autor**: Wesley + Gemini Code Assist

---

## 📖 ÍNDICE COMPLETO

1. [Conceitos Fundamentais](#conceitos-fundamentais)
2. [Fórmula da Força (F = M × A)](#fórmula-da-força)
3. [Gradiente de Cores RGB](#gradiente-de-cores-rgb)
4. [Padrões de Candles](#padrões-de-candles)
5. [Sintaxe NTSL Profit Neologica](#sintaxe-ntsl-profit-neologica)
6. [Estrutura de Robôs](#estrutura-de-robôs)
7. [Gestão de Risco](#gestão-de-risco)
8. [Cores Reservadas para Padrões](#cores-reservadas-para-padrões)

---

## 🎯 CONCEITOS FUNDAMENTAIS

### Força Física: F = M × A

```
DEFINIÇÃO:
F = Força resultante do candle (-100% a +100%)
M = Massa (deslocamento / range)
A = Aceleração (volume / volume_média)

FÓRMULA COMPLETA:
F = [(Close - Open) / (High - Low)] × [Volume / Volume_Média] × 100

INTERPRETAÇÃO:
F > +80% = Verde puro (compra máxima)
F +60-79% = Verde forte/médio
F +40-59% = Verde claro
F +20-39% = Verde muito claro
F ±0-15% = Branco (neutro)
F -20-39% = Vermelho muito claro
F -40-59% = Vermelho claro
F -60-79% = Vermelho forte/médio
F < -80% = Vermelho puro (venda máxima)
```

---

## 🎨 GRADIENTE DE CORES RGB

### Regra Principal

```
✅ GRADIENTE POSITIVO (Branco → Verde):
   Força positiva (F > 0) = Verde gradualmente mais intenso
   
✅ GRADIENTE NEGATIVO (Branco → Vermelho):
   Força negativa (F < 0) = Vermelho gradualmente mais intenso
   
✅ BRANCO NO CENTRO:
   Força zero (F ≈ 0) = RGB(255, 255, 255)
   
❌ NÃO USE: Amarelo, Marrom, Ciano, Magenta, Azul, Ouro
   (Reservados para padrões especiais)
```

### Cálculo RGB Automático

```ntsl
// Gradiente positivo (Branco → Verde)
if fForca >= 0 then
begin
  iCorR := 255 - (2.55 * fForca);
  iCorG := 255;
  iCorB := 255 - (2.55 * fForca);
end
else
begin
  // Gradiente negativo (Branco → Vermelho)
  iCorR := 255;
  iCorG := 255 + (2.55 * fForca);  // fForca é negativo
  iCorB := 255 + (2.55 * fForca);  // fForca é negativo
end;

PaintBar(RGB(iCorR, iCorG, iCorB));
```

---

## 🕯️ PADRÕES DE CANDLES

### 1. MARTELO (Hammer)

```
DEFINIÇÃO:
- Pavio inferior longo
- Corpo pequeno
- Pavio superior muito pequeno
- Volume acima da média

FÓRMULA:
bMartelo := (TamPavioInf >= TamCorpo × 1.5) AND
            (TamPavioSup <= TamCorpo × 1.2)

SIGNIFICADO:
✅ Vendedores testam
✅ Compradores absorvem
✅ Padrão de reversão de BAIXA

AÇÃO:
→ Se próximo candle verde: COMPRA
→ Validar com volume
→ Risco: Baixo após confirmação
```

### 2. ESTRELA (Star)

```
DEFINIÇÃO:
- Pavio superior longo
- Corpo pequeno
- Pavio inferior muito pequeno
- Volume acima da m��dia

FÓRMULA:
bEstrela := (TamPavioSup >= TamCorpo × 1.5) AND
            (TamPavioInf <= TamCorpo × 1.2)

SIGNIFICADO:
✅ Compradores testam
✅ Vendedores absorvem
✅ Padrão de reversão de ALTA

AÇÃO:
→ Se próximo candle vermelho: VENDA
→ Validar com volume
→ Risco: Baixo após confirmação
```

### 3. REJEIÇÃO FORTE

```
DEFINIÇÃO:
- Candle varre máxima anterior
- Candle varre mínima anterior
- Testa ambos os lados
- Ninguém consegue segurar ganhos

FÓRMULA:
bRejeicao := (High > High[1]) AND (Low < Low[1])

SIGNIFICADO:
⚡ Mercado testou força em ambas direções
⚡ Energia sendo absorvida
⚡ Próxima move será forte

AÇÃO:
→ Observar próximo candle (decisivo)
→ Se verde: COMPRA forte
→ Se vermelho: VENDA forte
→ COR: LARANJA RGB(255, 140, 0)
```

### 4. DOJI

```
DEFINIÇÃO:
- Corpo muitooo pequeno (< 10% do range)
- Pavios podem ser longos
- Abertura ≈ Fechamento

FÓRMULA:
bDoji := (Abs(Close - Open) / (High - Low)) < 0.10

SIGNIFICADO:
🔄 Indecisão total do mercado
🔄 Equilibrium entre compradores/vendedores
🔄 Possível reversão

AÇÃO:
→ NÃO ENTRA aqui
→ Aguarda próximo candle
→ Se próximo tiver força: sinal confiável
→ COR: BRANCO RGB(255, 255, 255)
```

### 5. ROMPIMENTO (Breakout)

```
DEFINIÇÃO:
- Close > Máxima candle anterior
- Close < Mínima candle anterior
- Volume > 2x média

FÓRMULA:
bRompimentoAlta := (Close > High[1]) AND (Volume > VolumeMedia × 2)
bRompimentoBaixa := (Close < Low[1]) AND (Volume > VolumeMedia × 2)

SIGNIFICADO:
✅ Preço rompe nível importante
✅ Decisão de mercado
✅ Impulso novo

AÇÃO:
→ COMPRA: se próximo verde ou força > +40%
→ VENDA: se próximo vermelho ou força < -40%
→ Validar RRR antes de entrar
```

### 6. ANOMALIA DE VOLUME

```
DEFINIÇÃO:
- Volume > 3x média
- Evento especial
- Movimento significativo

FÓRMULA:
bAnomalia := Volume > (VolumeMedia × 3.0)

SIGNIFICADO:
⚡ Algo importante aconteceu
⚡ Forte absorção de liquidez
⚡ Possível mudança de tendência

AÇÃO:
→ ATENÇÃO: verificar notícias
→ Esperado: continuação ou reversão
→ COR: AMARELO BRILHANTE RGB(255, 255, 0)
```

---

## 💻 SINTAXE NTSL PROFIT NEOLOGICA

### 1. ESTRUTURA BÁSICA

```ntsl
{
  Robo: nome_seu_robo
  Descricao: Descrição clara
  Ativo: WIN B3
  Timeframe: 60 minutos
  Versao: X.0
  Status: Compilavel
}

input
  Parametro1(valor);
  Parametro2(valor);

var
  fVariavelFloat : float;
  iVariavelInt : integer;
  bVariavelBool : boolean;

begin
  // Código aqui
end;
```

### 2. CÁLCULO DE FORÇA

```ntsl
// Força = M × A × 100
fCorpoCandle := Close - Open;
fRangeCandle := High - Low;

if fRangeCandle < 0.01 then
  fRangeCandle := 0.01;

fMassa := fCorpoCandle / fRangeCandle;

fVolumeMedio := Media(20, Volume);

if fVolumeMedio > 0 then
  fAceleracao := Volume / fVolumeMedio
else
  fAceleracao := 1;

fForca := fMassa * fAceleracao * 100;

if fForca > 100 then fForca := 100;
if fForca < -100 then fForca := -100;
```

### 3. GRADIENTE DE CORES

```ntsl
// Aplicar gradiente
if fForca >= 0 then
begin
  iCorR := 255 - (2.55 * fForca);
  iCorG := 255;
  iCorB := 255 - (2.55 * fForca);
end
else
begin
  iCorR := 255;
  iCorG := 255 + (2.55 * fForca);
  iCorB := 255 + (2.55 * fForca);
end;

PaintBar(RGB(iCorR, iCorG, iCorB));
```

### 4. DETECTAR PADRÕES

```ntsl
// Martelo
bMartelo := (TamPavioInf >= TamCorpo * 1.5) and 
            (TamPavioSup <= TamCorpo * 1.2);

// Estrela
bEstrela := (TamPavioSup >= TamCorpo * 1.5) and 
            (TamPavioInf <= TamCorpo * 1.2);

// Rejeição
bRejeicao := (High > High[1]) and (Low < Low[1]);

// Doji
bDoji := (Abs(Close - Open) / (High - Low)) < 0.10;

// Anomalia volume
bAnomalia := Volume > (fVolumeMedio * 3.0);
```

### 5. APLICAR CORES ESPECIAIS

```ntsl
// Rejeição = Laranja
if bRejeicao then
begin
  iCorR := 255;
  iCorG := 140;
  iCorB := 0;
end;

// Anomalia = Amarelo brilhante
if bAnomalia and (not bRejeicao) then
begin
  iCorR := 255;
  iCorG := 255;
  iCorB := 0;
end;

// Doji = Branco (padrão)
// Não precisa overrride, já é branco por padrão
```

### 6. EXECUÇÃO DE ORDENS

```ntsl
// Compra
if bSinalCompra and (not IsBought) and (fForca > 40) then
begin
  BuyAtMarket;
end;

// Venda
if bSinalVenda and (not IsSold) and (fForca < -40) then
begin
  SellShortAtMarket;
end;

// Fechar posição
if Time() >= 170000 then
begin
  ClosePosition;
end;
```

### 7. GESTÃO DE POSIÇÃO

```ntsl
// Stop Loss e Take Profit
fStopLoss := Close - (fRangeCandle * 1.5);
fTakeProfit := Close + (fRangeCandle_ATR * ATRMultiplicador);

// Validar RRR
fRiscoEmPontos := Close - fStopLoss;
fRecompensaEmPontos := fTakeProfit - Close;

if fRiscoEmPontos > 0 then
  fRazaoRiscoRecompensa := fRecompensaEmPontos / fRiscoEmPontos
else
  fRazaoRiscoRecompensa := 0;

// Apenas entra se RRR >= 1.0
if fRazaoRiscoRecompensa >= 1.0 then
  bValidacaoRegras := true;
```

---

## 🤖 ESTRUTURA DE ROBÔS

### Template Padrão

```ntsl
{
  Robo: seu_robo_nome
  Descricao: Descrição estratégia
  Status: Compilavel
}

input
  VolumeMinimo(2000);
  CapitalConta(10000);
  RiscoPorcentagem(2.0);
  ATRMultiplicador(2.0);

var
  // === FORÇA ===
  fCorpoCandle : float;
  fRangeCandle : float;
  fMassa : float;
  fAceleracao : float;
  fForca : float;
  fVolumeMedio : float;
  
  // === CORES ===
  iCorR : integer;
  iCorG : integer;
  iCorB : integer;
  
  // === PADRÕES ===
  fMaxAnterior : float;
  fMinAnterior : float;
  bSinalCompra : boolean;
  bSinalVenda : boolean;
  bRejeicao : boolean;
  bAnomalia : boolean;
  
  // === GESTÃO ===
  fStopLoss : float;
  fTakeProfit : float;
  fRiscoEmPontos : float;
  fRecompensaEmPontos : float;
  fRazaoRiscoRecompensa : float;
  bValidacaoRegras : boolean;

begin

  // SEÇÃO 1: Calcular força
  fCorpoCandle := Close - Open;
  fRangeCandle := High - Low;
  if fRangeCandle < 0.01 then fRangeCandle := 0.01;
  fMassa := fCorpoCandle / fRangeCandle;
  fVolumeMedio := Media(20, Volume);
  if fVolumeMedio > 0 then fAceleracao := Volume / fVolumeMedio else fAceleracao := 1;
  fForca := fMassa * fAceleracao * 100;
  if fForca > 100 then fForca := 100;
  if fForca < -100 then fForca := -100;

  // SEÇÃO 2: Aplicar gradiente
  if fForca >= 0 then
  begin
    iCorR := 255 - (2.55 * fForca);
    iCorG := 255;
    iCorB := 255 - (2.55 * fForca);
  end
  else
  begin
    iCorR := 255;
    iCorG := 255 + (2.55 * fForca);
    iCorB := 255 + (2.55 * fForca);
  end;
  PaintBar(RGB(iCorR, iCorG, iCorB));

  // SEÇÃO 3: Detectar padrões
  bRejeicao := (High > High[1]) and (Low < Low[1]);
  bAnomalia := Volume > (fVolumeMedio * 3.0);
  
  if bRejeicao then
  begin
    iCorR := 255;
    iCorG := 140;
    iCorB := 0;
  end;
  if bAnomalia and (not bRejeicao) then
  begin
    iCorR := 255;
    iCorG := 255;
    iCorB := 0;
  end;

  // SEÇÃO 4: Lógica de entrada
  fMaxAnterior := High[1];
  fMinAnterior := Low[1];
  bSinalCompra := (Close > fMaxAnterior) and (Volume > VolumeMinimo);
  bSinalVenda := (Close < fMinAnterior) and (Volume > VolumeMinimo);

  // SEÇÃO 5: Validar RRR
  bValidacaoRegras := false;
  if bSinalCompra then
  begin
    fStopLoss := Close - (fRangeCandle * 1.5);
    fTakeProfit := Close + ((High - Low + High[1] - Low[1] + High[2] - Low[2]) / 3 * ATRMultiplicador);
    fRiscoEmPontos := Close - fStopLoss;
    fRecompensaEmPontos := fTakeProfit - Close;
    if fRiscoEmPontos > 0 then
      fRazaoRiscoRecompensa := fRecompensaEmPontos / fRiscoEmPontos
    else
      fRazaoRiscoRecompensa := 0;
    if fRazaoRiscoRecompensa >= 1.0 then
      bValidacaoRegras := true;
  end;

  // SEÇÃO 6: Executar
  if bSinalCompra and (not IsBought) and (fForca > 40) and bValidacaoRegras then
    BuyAtMarket;
  
  if bSinalVenda and (not IsSold) and (fForca < -40) and bValidacaoRegras then
    SellShortAtMarket;

  // SEÇÃO 7: Saída
  if Time() >= 170000 then
    ClosePosition;

end;
```

---

## 💰 GESTÃO DE RISCO

### Regras Obrigatórias

```
1. STOP LOSS SEMPRE
   SL = Entrada ± (Range × 1.5)
   Nunca operar sem SL

2. TAKE PROFIT OBRIGATÓRIO
   TP = Entrada ± (ATR × 2)
   Definir antes de entrar

3. RRR MÍNIMO 1:1
   Risco:Recompensa = TP / SL ≥ 1.0
   Ideal: 1:2 ou 1:3

4. TAMANHO DE POSIÇÃO
   Quantidade = Risco_Diário / Risco_por_Contrato
   Máximo: 2% do capital por operação

5. RISCO DIÁRIO MÁXIMO
   Se perder X% do capital → PARAR
   Ideal: Máximo 5% perda por dia

6. SAÍDA POR TEMPO
   Fechar todas posições às 17:00
   Sem overnight
```

### Cálculo Tamanho Posição

```ntsl
fRiscoEmReais := CapitalConta * (RiscoPorcentagem / 100);
fQuantidade := fRiscoEmReais / (fRiscoEmPontos * 0.2);

if fQuantidade < 1 then fQuantidade := 1;
if fQuantidade > 5 then fQuantidade := 5;
```

---

## 🎨 CORES RESERVADAS PARA PADRÕES

### USO PERMITIDO

```
🟢 VERDE: Gradiente positivo (OBRIGATÓRIO)
🔴 VERMELHO: Gradiente negativo (OBRIGATÓRIO)
⚪ BRANCO: Neutro/Doji (OBRIGATÓRIO)

🟠 LARANJA: Rejeição forte
   RGB(255, 140, 0)
   Condição: High > High[1] AND Low < Low[1]

🟡 AMARELO: Anomalia volume
   RGB(255, 255, 0)
   Condição: Volume > VolumeMedia × 3.0
```

### NÃO USE PARA FORÇA

```
❌ Marrom RGB(139, 69, 19)
❌ Ciano RGB(0, 255, 255)
❌ Magenta RGB(255, 0, 255)
❌ Azul RGB(0, 100, 255)
❌ Ouro RGB(255, 215, 0)

(Reservados para expansão futura)
```

---

## 📋 CHECKLIST COMPILAÇÃO

- [ ] Todas as variáveis declaradas em `var`?
- [ ] Todos os `if` têm `then` e `end`?
- [ ] Pontuação `;` ao final de cada linha?
- [ ] `RGB(R, G, B)` com valores 0-255?
- [ ] `PaintBar()` para colorir?
- [ ] `BuyAtMarket`/`SellShortAtMarket` para ordens?
- [ ] `ClosePosition` para fechar?
- [ ] Função `Media()` para média móvel?
- [ ] Função `Time()` para hora?
- [ ] Sem `DrawArrow`/`DrawLine` em robô?

---

## 📊 TABELA RÁPIDA DE REFERÊNCIA

| Elemento | Símbolo | RGB | Uso |
|----------|---------|-----|-----|
| Verde Puro | 🟢 | (0,255,0) | F > +95% |
| Verde | 🟢 | Gradiente | Gradiente positivo |
| Branco | ⚪ | (255,255,255) | F ≈ 0% |
| Vermelho | 🔴 | Gradiente | Gradiente negativo |
| Vermelho Puro | 🔴 | (255,0,0) | F < -95% |
| Laranja | 🟠 | (255,140,0) | Rejeição |
| Amarelo | 🟡 | (255,255,0) | Anomalia volume |

---

## 🚀 PRÓXIMAS IMPLEMENTAÇÕES

```
DISPONÍVEL PARA USAR EM FUTUROS PROMPTS:

Marrom RGB(139, 69, 19)
→ Possível uso: Suporte fraco

Ciano RGB(0, 255, 255)
→ Possível uso: Resistência fraca

Magenta RGB(255, 0, 255)
→ Possível uso: Padrão engulfing

Azul RGB(0, 100, 255)
→ Possível uso: Multi-timeframe confirmado

Ouro RGB(255, 215, 0)
→ Possível uso: Setup premium
```

---

## ✅ CONCLUSÃO

Você tem agora um **SISTEMA COMPLETO** de:

✅ Física de preços (F = M × A)  
✅ Gradiente RGB dinâmico  
✅ Padrões de candles  
✅ Sintaxe NTSL Profit Neologica  
✅ Gestão de risco  
✅ Cores reservadas para expansão  

---

## 📞 COMO USAR ESTE MANUAL

1. **Para criar novo robô**: Use template + estrutura de 7 seções
2. **Para adicionar padrões**: Copie fórmula do padrão desejado
3. **Para validar sintaxe**: Siga checklist de compilação
4. **Para expandir cores**: Use cores reservadas conforme necessário

---

**Versão**: 7.0 FINAL - MANUAL COMPLETO  
**Status**: ✅ PRONTO PARA USAR EM FUTUROS PROMPTS  
**Data**: 12/03/2026  
**Garantia**: 100% Compilável Profit Neologica