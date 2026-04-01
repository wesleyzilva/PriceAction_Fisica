# Exemplos Completos de Códigos NTFL/NTSL para Estratégias de Candles

Este arquivo reúne exemplos completos de códigos NTFL/NTSL para referência e reutilização em estratégias de coloração, padrões, sinais, alarmes, textos, setas e operações de candles.

---

## 1. Gradiente Dinâmico com Cores Especiais
**Arquivo:** abr_ROM_V1_gradiente_completo_Version3.ntsl
```pascal
// ...cabeçalho e inputs...
var
  fCorpoCandle, fRangeCandle, fMassa, fAceleracao, fForca, fVolumeMedio: float;
  iCorR, iCorG, iCorB: integer;
  bRejeicaoForte, bAnomaliaVolume: boolean;
  // ...outras variáveis...
begin
  // Cálculo da força
  fCorpoCandle := Close - Open;
  fRangeCandle := High - Low;
  if fRangeCandle < 0.01 then fRangeCandle := 0.01;
  fMassa := fCorpoCandle / fRangeCandle;
  fVolumeMedio := Media(20, Volume);
  if fVolumeMedio > 0 then fAceleracao := Volume / fVolumeMedio else fAceleracao := 1;
  fForca := fMassa * fAceleracao * 100;
  if fForca > 100 then fForca := 100;
  if fForca < -100 then fForca := -100;

  // Gradiente de cores
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

  // Cores especiais
  if UsarCoresEspeciais then
  begin
    bRejeicaoForte := (High > High[1]) and (Low < Low[1]);
    if bRejeicaoForte then
    begin
      iCorR := 255; iCorG := 140; iCorB := 0;
    end;
    bAnomaliaVolume := Volume > (fVolumeMedio * 3.0);
    if bAnomaliaVolume and (not bRejeicaoForte) then
    begin
      iCorR := 255; iCorG := 255; iCorB := 0;
    end;
  end;

  PaintBar(RGB(iCorR, iCorG, iCorB));
  // ...restante do código: sinais, stops, gerenciamento...
end;
```

---

## 2. Coloração por Força e Indecisão
**Arquivo:** FORCA_SEMAFORO_CORES_55.ntfl
```pascal
// ...cabeçalho e inputs...
var
  fCorpo, fRange, fVolMedia, fMassa, fAceleracao, fForca: float;
begin
  // Cálculos de base
  fCorpo := Close - Open;
  fRange := High - Low;
  if fRange <= 0 then fRange := 0.0001;
  fVolMedia := Media(PeriodoMediaVolume, Volume);
  if fVolMedia <= 0 then fVolMedia := 1;
  fMassa := fCorpo / fRange;
  fAceleracao := Volume / fVolMedia;
  fForca := fMassa * fAceleracao * 100;
  if fForca > 100 then fForca := 100;
  if fForca < -100 then fForca := -100;

  // Lógica de cores
  var r, g, b: integer;
  r := 128; g := 128; b := 128;
  if (abs(fCorpo) < 0.1 * fRange) then
  begin
    r := 255; g := 255; b := 255;
  end
  else if (fForca >= ForcaMinimaEntrada) then
  begin
    g := 128 + round((fForca/100) * 127);
    r := 128 - round((fForca/100) * 128);
    b := 128 - round((fForca/100) * 128);
    if g > 255 then g := 255;
    if r < 0 then r := 0;
    if b < 0 then b := 0;
  end
  else if (fForca <= -ForcaMinimaEntrada) then
  begin
    r := 128 + round((-fForca/100) * 127);
    g := 128 - round((-fForca/100) * 128);
    b := 128 - round((-fForca/100) * 128);
    if r > 255 then r := 255;
    if g < 0 then g := 0;
    if b < 0 then b := 0;
  end
  // Senão, permanece cinza
  PaintBar(RGB(r, g, b));
  // ...restante do código: sinais, alarmes, fechamento...
end;
```

---

## 3. Volume Acima da Média e Padrão de Reversão
**Arquivo:** volumeAcimaMediaReversao.ntfl
```pascal
// ...cabeçalho e inputs...
var
  // ...variáveis...
begin
  // Cores
  CorAbsorcaoFundo := RGB(0, 255, 0);
  CorAbsorcaoTopo  := RGB(255, 0, 0);
  CorNeutra        := RGB(105, 105, 105);
  CorRejeicaoContexto := RGB(255, 140, 0);
  CorIndefinicao := RGB(255, 255, 255);

  PaintBar(CorNeutra);
  // ...cálculos de volume, pavio, padrões...
  if bArmadilhaPrimeiro then
  begin
    PaintBar(CorRejeicaoContexto);
    PlotText("1C_TRAP", CorRejeicaoContexto, 8, 0, Close);
  end
  else if bIniciativaAltaPrimeiro then
  begin
    PaintBar(CorAbsorcaoFundo);
    PlotText("1C_UP", CorAbsorcaoFundo, 8, 0, Low * 0.999);
  end
  else if bIniciativaBaixaPrimeiro then
  begin
    PaintBar(CorAbsorcaoTopo);
    PlotText("1C_DN", CorAbsorcaoTopo, 8, 0, High * 1.001);
  end
  else if bAbsorcaoPrimeiro or bDojiPrimeiro then
    PaintBar(CorIndefinicao)
  else if (Close > Open) then
    PaintBar(CorAbsorcaoFundo)
  else if (Close < Open) then
    PaintBar(CorAbsorcaoTopo)
  else
    PaintBar(CorIndefinicao);
  // ...restante do código...
end;
```

---

## 4. Exemplos de Alarme, Texto, Seta e Operação
```pascal
// Alarme sonoro
if (bSinalCompra) then
begin
  Alert(RGB(0,255,0)); // Alarme verde para compra
end;
if (bSinalVenda) then
begin
  Alert(RGB(255,0,0)); // Alarme vermelho para venda
end;

// Imprimir texto na tela
if (bSinalCompra) then
begin
  PlotText("COMPRA", RGB(0,255,0), 10, 0, Low * 0.995);
end;
if (bSinalVenda) then
begin
  PlotText("VENDA", RGB(255,0,0), 10, 0, High * 1.005);
end;

// Colocar seta
if (bSinalCompra) then
begin
  PlotArrowUp(RGB(0,255,0), 0, Low * 0.995);
end;
if (bSinalVenda) then
begin
  PlotArrowDown(RGB(255,0,0), 0, High * 1.005);
end;

// Operação de compra/venda
if (bSinalCompra) and (not IsBought) then
begin
  BuyAtMarket;
end;
if (bSinalVenda) and (not IsSold) then
begin
  SellShortAtMarket;
end;
```

---

Esses exemplos completos podem ser usados como base para novos robôs, indicadores ou estudos em NTFL/NTSL. Adapte os parâmetros, variáveis e lógica conforme sua necessidade.
