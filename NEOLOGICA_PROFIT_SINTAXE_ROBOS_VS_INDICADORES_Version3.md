# 🔧 NEOLOGICA PROFIT - SINTAXE: ROBÔS vs INDICADORES

**Status**: ✅ Corrigido - Diferenças reais  
**Data**: 12/03/2026  
**Versão**: FINAL

---

## ⚠️ DIFERENÇA CRÍTICA

### INDICADORES podem usar:
- `PaintBar(RGB(R, G, B))`
- `PlotText()`
- `Alert()`
- `DrawArrow()`
- `DrawLine()`
- `HighlightBar()`

### ROBÔS podem usar APENAS:
- `PaintBar(RGB(R, G, B))` ✅
- `BuyAtMarket` ✅
- `SellShortAtMarket` ✅
- `ClosePosition` ✅

---

## ❌ O QUE NÃO FUNCIONA EM ROBÔS

```
❌ SetCandleColor(R, G, B)      - Use PaintBar() ao invés
❌ DrawArrow()                  - Não funciona em robôs
❌ DrawLine()                   - Não funciona em robôs
❌ PlotText()                   - Não funciona em robôs
❌ Alert()                      - Não funciona em robôs
```

---

## ✅ O QUE FUNCIONA EM ROBÔS

### Colorir candle

```ntsl
PaintBar(RGB(0, 255, 0));       // Verde
PaintBar(RGB(255, 0, 0));       // Vermelho
PaintBar(RGB(105, 105, 105));   // Cinza padrão
```

### Executar ordem

```ntsl
BuyAtMarket;                    // Compra
SellShortAtMarket;              // Venda
ClosePosition;                  // Fecha tudo
```

### Condicional

```ntsl
if fForca > 80 then
begin
  PaintBar(RGB(0, 255, 0));
  BuyAtMarket;
end;
```

---

## 📊 TABELA COMPARATIVA

| Função | Robô | Indicador |
|--------|------|-----------|
| `PaintBar()` | ✅ | ✅ |
| `PlotText()` | ❌ | ✅ |
| `Alert()` | ❌ | ✅ |
| `DrawArrow()` | ❌ | ✅ |
| `DrawLine()` | ❌ | ✅ |
| `BuyAtMarket` | ✅ | ❌ |
| `SellShortAtMarket` | ✅ | ❌ |

---

## 🎯 WORKFLOW CORRETO

### Para INDICADOR (apenas visualização):

```ntsl
{
  Indicador: Meu_Indicador
}

var
  fForca : float;

begin
  fForca := ...;
  
  PaintBar(RGB(0, 255, 0));        // Colore
  PlotText("COMPRA", ...);         // Label
  Alert(RGB(0, 255, 0));           // Alerta
  DrawArrow(Time, Close, 1);       // Seta
end;
```

### Para ROBÔ (execução + cores):

```ntsl
{
  Robo: Meu_Robo
}

var
  fForca : float;
  bSinal : boolean;

begin
  fForca := ...;
  bSinal := fForca > 80;
  
  PaintBar(RGB(0, 255, 0));        // Colore
  // SEM PlotText, Alert, DrawArrow, DrawLine
  
  if bSinal then
  begin
    BuyAtMarket;                   // Executa ordem
  end;
end;
```

---

## 🔄 SOLUÇÃO: INDICADOR + ROBÔ

Para ter **visualização COMPLETA** (cores + labels + setas) + **execução automática**:

### 1️⃣ Crie INDICADOR com todas as cores/labels:

```ntsl
{
  Indicador: Forca_Completa
}

begin
  PaintBar(RGB(0, 255, 0));
  PlotText("COMPRA", RGB(0, 255, 0), 8, 0, Low);
  DrawArrow(Time, Close, 1);
end;
```

### 2️⃣ Crie ROBÔ com execução:

```ntsl
{
  Robo: Rompimento_Executa
}

begin
  PaintBar(RGB(0, 255, 0));
  
  if bSinal then
    BuyAtMarket;
  end;
end;
```

### 3️⃣ Use OS DOIS no mesmo gráfico:
- **Indicador** = visualização (cores, labels, setas)
- **Robô** = execução automática (ordens)

---

## ✅ ROBÔ FINAL CORRETO

```ntsl
{
  Robo: abr_ROM_V1_rompimento_cores
  Status: Com PaintBar CORRETO
}

input
  VolumeMinimo(2000);
  CapitalConta(10000);

var
  fForca : float;
  bSinalCompra : boolean;

begin

  fForca := (Close - Open) / (High - Low) * 100;
  
  // COLORIR (funciona em robô)
  if fForca > 80 then
    PaintBar(RGB(0, 255, 0))
  else if fForca < -80 then
    PaintBar(RGB(255, 0, 0))
  else
    PaintBar(RGB(105, 105, 105));
  
  // LÓGICA
  bSinalCompra := (Close > High[1]) and (Volume > VolumeMinimo) and (fForca > 40);
  
  // EXECUTAR (funciona em robô)
  if bSinalCompra and (not IsBought) then
    BuyAtMarket;
  
  if Time() >= 170000 then
    ClosePosition;

end;
```

---

## 🎯 RESUMO

### Para ROBÔS Neologica:

✅ Use `PaintBar(RGB())` para colorir candles  
✅ Use `BuyAtMarket`, `SellShortAtMarket`, `ClosePosition` para ordens  
✅ Estrutura: se-então com `begin...end`  

❌ NÃO use `DrawArrow`, `DrawLine`, `PlotText`, `Alert`  
❌ NÃO use `SetCandleColor`  

### Para INDICADORES Neologica:

✅ Use TUDO: `PaintBar`, `PlotText`, `Alert`, `DrawArrow`, `DrawLine`  
❌ NÃO use funções de ordem (`BuyAtMarket`)

---

## 📚 PRÓXIMOS PASSOS

1. **Robô**: Use apenas `PaintBar()` para cores
2. **Indicador**: Use `PlotText()`, `Alert()`, `DrawArrow()` para visualização
3. **Combine os dois** no mesmo gráfico para efeito completo

---

**Versão**: FINAL - Sintaxe corrigida  
**Status**: ✅ PRONTO