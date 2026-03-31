# 🎨 5 ROBÔS PRICE ACTION COM CORES RGB

**Status**: ✅ Com sistema de cores F = M × A  
**Data**: 12/03/2026  
**Versão**: 2.0 - Com Cores

---

## 🎨 SISTEMA DE CORES RGB

### Conceito Físico: F = M × A

```
F (Força) = Cor do Candle
M (Massa) = |Close - Open| / Range (deslocamento)
A (Aceleração) = Volume / Volume_Média (força volume)

Resultado: -100% a +100%
```

### Mapeamento de Cores

```
🟢 VERDE      RGB(0, 255, 0)       - F > +80% (Força máxima compra)
🔵 CIANO      RGB(0, 255, 255)     - F: +60% a +79% (Força compra)
🟨 AMARELO    RGB(255, 255, 0)     - F: +40% a +59% (Força fraca compra)
⚪ BRANCO     RGB(255, 255, 255)   - F: +20% a +39% (Transição positiva)
⚫ CINZA      RGB(128, 128, 128)   - F: -15% a +15% (Sem força)
🟫 MARROM     RGB(139, 69, 19)     - F: -40% a -59% (Força fraca venda)
🔴 VERMELHO   RGB(255, 0, 0)       - F < -80% (Força máxima venda)
```

---

## 🤖 ROBÔ 1: ROMPIMENTO COM CORES

**Arquivo**: `abr_ROM_V1_rompimento_cores.ntsl`

```ntsl
{
  Robo: abr_ROM_V1_rompimento_cores
  Descricao: Rompimento com sistema de cores RGB
  Ativo: WIN B3
  Timeframe: 60 minutos
  Versao: 2.0
  Status: 100% Compilavel com Cores
}

input
  VolumeMinimo(2000);
  PeriodoVolMedia(20);

var
  fMaxAnterior : float;
  fMinAnterior : float;
  fVolMedia : float;
  fCorpoCandle : float;
  fRangeCandle : float;
  fMassa : float;
  fAceleracao : float;
  fForca : float;
  iCorR : integer;
  iCorG : integer;
  iCorB : integer;
  bSinalCompra : boolean;
  bSinalVenda : boolean;

begin

  // ================================================
  // SEÇÃO A: CÁLCULO DE CORES (F = M × A)
  // ================================================
  
  fVolMedia := Volume[1];
  fCorpoCandle := Close - Open;
  fRangeCandle := High - Low;
  
  if fRangeCandle < 0.01 then
    fRangeCandle := 0.01;
  
  // M = Massa = |Close - Open| / Range
  fMassa := fCorpoCandle / fRangeCandle;
  
  // A = Aceleração = Volume / VolMedia
  if fVolMedia > 0 then
    fAceleracao := Volume / fVolMedia
  else
    fAceleracao := 1;
  
  // F = M × A × 100
  fForca := fMassa * fAceleracao * 100;
  
  // Clamp força entre -100 e +100
  if fForca > 100 then fForca := 100;
  if fForca < -100 then fForca := -100;
  
  // ================================================
  // SEÇÃO B: MAPEAMENTO RGB BASEADO EM F
  // ================================================
  
  iCorR := 128;
  iCorG := 128;
  iCorB := 128;
  
  // Verde: F > +80%
  if fForca > 80 then
  begin
    iCorR := 0;
    iCorG := 255;
    iCorB := 0;
  end;
  
  // Ciano: F: +60% a +79%
  if (fForca > 60) and (fForca <= 80) then
  begin
    iCorR := 0;
    iCorG := 255;
    iCorB := 255;
  end;
  
  // Amarelo: F: +40% a +59%
  if (fForca > 40) and (fForca <= 60) then
  begin
    iCorR := 255;
    iCorG := 255;
    iCorB := 0;
  end;
  
  // Branco: F: +20% a +39%
  if (fForca > 20) and (fForca <= 40) then
  begin
    iCorR := 255;
    iCorG := 255;
    iCorB := 255;
  end;
  
  // Vermelho: F < -80%
  if fForca < -80 then
  begin
    iCorR := 255;
    iCorG := 0;
    iCorB := 0;
  end;
  
  // Marrom: F: -40% a -59%
  if (fForca < -40) and (fForca >= -60) then
  begin
    iCorR := 139;
    iCorG := 69;
    iCorB := 19;
  end;

  // ================================================
  // SEÇÃO K: LÓGICA DE ROMPIMENTO
  // ================================================
  
  fMaxAnterior := High[1];
  fMinAnterior := Low[1];
  
  bSinalCompra := false;
  bSinalVenda := false;
  
  // Rompimento para cima
  if Close > fMaxAnterior then
  begin
    if Volume > VolumeMinimo then
    begin
      bSinalCompra := true;
    end;
  end;
  
  // Rompimento para baixo
  if Close < fMinAnterior then
  begin
    if Volume > VolumeMinimo then
    begin
      bSinalVenda := true;
    end;
  end;

  // ================================================
  // SEÇÃO L: EXECUÇÃO COM VALIDAÇÃO DE COR
  // ================================================
  
  // Exec*
