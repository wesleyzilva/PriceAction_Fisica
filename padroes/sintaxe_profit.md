# Sintaxe NTSL (Nelogica Trading System Language)

Este documento detalha a sintaxe, os padrões e as boas práticas para o desenvolvimento de estratégias em NTSL para a plataforma Profit.

---

## Guia de Sintaxe e Padrões para Robôs Profit

Este arquivo serve como referência para criação, documentação e padronização de robôs em NTSL.

### 1. Cabeçalho Básico

Todo robô deve iniciar com um bloco comentado, contendo obrigatoriamente:

- Nome do arquivo
- Grupo/conceito
- Descrição clara do objetivo
- Identificador único
- Timeframe(s)
- Ativo(s)
- Versão
- Autor e data

Exemplo:
{
Robo: mar_IDunicocomLetraeNumero_priceactionfisica_60min.ntsl
Grupo: IFR_RSI — Tier 1 (#01)
Descricao: Divergencia bullish/bearish de IFR confirmada por candle de rejeicao
(martelo para alta, estrela cadente para baixa).
Setup com maior taxa de acerto do grupo (referencia v4: ~90%).
Timeframe: 60min (principal), 30min
Ativo: WIN (minicontrato de indice)
Versao: 1.0 — marco/2026
Autor: Seu Nome
}

### 2. Estrutura Básica

```pascal
input
        parametro_exemplo(14); // Ex: Média de 14 períodos
var
        // Declaração de variáveis
begin
        // Lógica da estratégia
        if (condicao_compra) then
                buy at market;
end;
```

### 3. Template de Risco

Inclua parâmetros e lógica de gestão de risco:

```pascal
input
        SaldoConta(10000.0);
        RiscoDiaPct(1.5);
        RiscoSemanaPct(3.0);
        MaxStopsConsecutivos(3);
var
        fResultadoDia, fResultadoSemana : float;
        bBloqueioDia, bBloqueioSemana  : boolean;
begin
        // Cálculo dos limites
        fLimiteDia    := SaldoConta * (RiscoDiaPct / 100.0);
        fLimiteSemana := SaldoConta * (RiscoSemanaPct / 100.0);
        // Lógica de bloqueio
        if fResultadoDia <= -fLimiteDia then bBloqueioDia := true;
        if fResultadoSemana <= -fLimiteSemana then bBloqueioSemana := true;
        if iStopsConsec >= MaxStopsConsecutivos then bBloqueioDia := true;
end;
```

### 4. Convenção de Nomes de Arquivos

Siga o padrão:
`mar_IDunicocomLetraeNumero_priceactionfisica_60min.ntsl`
Componentes:

- mar: mês do ciclo
- IDunicocomLetraeNumero: identificador único
- priceactionfisica: grupo conceito
- 60min: timeframe
- .ntsl: extensão obrigatória
  Exemplo: mar_A1B2C3_priceactionfisica_60min.ntsl

### 5. Exemplo Completo de Robô

Veja um exemplo compilável:

```pascal
// mar_IFR_01_v1_divergencia_confirmada.ntsl
// Grupo: IFR_RSI — Tier 1 (#01)
// Descricao: Divergencia bullish/bearish de IFR confirmada por candle de rejeicao
// Setup com maior taxa de acerto do grupo (referencia v4: ~90%).
// Timeframe: 60min (principal), 30min
// Ativo: WIN (minicontrato de indice)
// Versao: 1.0 — marco/2026

input
    PeriodoIFR(9);
    LookbackDivergencia(12);
    DeltaIFRMinimo(2.0);
    MultiplicadorPavio(1.5);
    MaxPavioOpostoCorpo(1.2);
    UsarFiltroVolume(false);
    PeriodoMediaVol(20);
    FatorVolume(1.0);
    UsarSaidaIFR(true);
    NivelSaidaCompra(55);
    NivelSaidaVenda(45);
    UsarSaidaTempo(true);
    MaxBarrasPosicao(12);
    UsarGestaoRisco(true);
    UsarHardLock(true);
    SaldoConta(10000.0);
    RiscoDiaPct(1.5);
    RiscoSemanaPct(3.0);
    MaxStopsConsecutivos(3);
    ValorPorPonto(0.2);
    DiaSemanaReset(2);

var
    iBarrasEmPosicao : integer;
    fIFR, fMediaVol  : float;
    fRange, fCorpo, fPavioSup, fPavioInf : float;
    bMartelo, bEstrela, bVolumeOk        : boolean;
    bDivAlta, bDivBaixa                  : boolean;
    fPrecoEntrada, fResultadoDia, fResultadoSemana : float;
    fLimiteDia, fLimiteSemana, fResultadoPontos, fResultadoReais : float;
    bBloqueioDia, bBloqueioSemana  : boolean;
    iDirecaoPosicao, iStopsConsec  : integer;
    iDiaSemanaAtual                : integer;

begin
    if CurrentBar = 1 then
        Print("Robo ativo: mar_IFR_01_v1_divergencia_confirmada");

    if Date <> Date[1] then
    begin
        iBarrasEmPosicao := 0;
        fResultadoDia    := 0;
        bBloqueioDia     := false;
        iDiaSemanaAtual  := DayOfWeek(Date);
        if iDiaSemanaAtual = DiaSemanaReset then
        begin
            fResultadoSemana := 0;
            bBloqueioSemana  := false;
        end;
    end;

    if UsarGestaoRisco then
    begin
        fLimiteDia    := SaldoConta * (RiscoDiaPct / 100.0);
        fLimiteSemana := SaldoConta * (RiscoSemanaPct / 100.0);
        if (iDirecaoPosicao = 1) and (not IsBought) and (fPrecoEntrada > 0) then
        begin
            fResultadoPontos := Close - fPrecoEntrada;
            fResultadoReais  := fResultadoPontos * ValorPorPonto;
            fResultadoDia    := fResultadoDia + fResultadoReais;
            fResultadoSemana := fResultadoSemana + fResultadoReais;
            if fResultadoReais < 0 then iStopsConsec := iStopsConsec + 1 else iStopsConsec := 0;
            fPrecoEntrada := 0; iDirecaoPosicao := 0;
        end;
        if (iDirecaoPosicao = -1) and (not IsSold) and (fPrecoEntrada > 0) then
        begin
            fResultadoPontos := fPrecoEntrada - Close;
            fResultadoReais  := fResultadoPontos * ValorPorPonto;
            fResultadoDia    := fResultadoDia + fResultadoReais;
            fResultadoSemana := fResultadoSemana + fResultadoReais;
            if fResultadoReais < 0 then iStopsConsec := iStopsConsec + 1 else iStopsConsec := 0;
            fPrecoEntrada := 0; iDirecaoPosicao := 0;
        end;
        if UsarHardLock then
        begin
            if fResultadoDia <= -fLimiteDia then bBloqueioDia := true;
            if fResultadoSemana <= -fLimiteSemana then bBloqueioSemana := true;
            if iStopsConsec >= MaxStopsConsecutivos then bBloqueioDia := true;
        end;
    end;

    fIFR      := IFR(PeriodoIFR);
    fMediaVol := Media(PeriodoMediaVol, Volume);
    bVolumeOk := (not UsarFiltroVolume) or (Volume >= fMediaVol * FatorVolume);

    fRange    := High - Low;
    fCorpo    := Abs(Open - Close);
    fPavioSup := High - Max(Open, Close);
    fPavioInf := Min(Open, Close) - Low;

    bMartelo := (fRange > 0) and (fCorpo > 0)
                     and (fPavioInf >= fCorpo * MultiplicadorPavio)
                     and (fPavioSup <= fCorpo * MaxPavioOpostoCorpo);

    bEstrela := (fRange > 0) and (fCorpo > 0)
                     and (fPavioSup >= fCorpo * MultiplicadorPavio)
                     and (fPavioInf <= fCorpo * MaxPavioOpostoCorpo);

    bDivAlta  := (Low < Lowest(Low, LookbackDivergencia)[1])
                        and (fIFR > (Lowest(IFR(PeriodoIFR), LookbackDivergencia)[1] + DeltaIFRMinimo));
    bDivBaixa := (High > Highest(High, LookbackDivergencia)[1])
                        and (fIFR < (Highest(IFR(PeriodoIFR), LookbackDivergencia)[1] - DeltaIFRMinimo));

    if (not IsBought) and (not IsSold)
    and (not (UsarGestaoRisco and (bBloqueioDia or bBloqueioSemana))) then
    begin
        if bDivAlta and bMartelo and bVolumeOk then
        begin
            BuyAtMarket;
            fPrecoEntrada := Close; iDirecaoPosicao := 1;
        end
        else if bDivBaixa and bEstrela and bVolumeOk then
        begin
            SellShortAtMarket;
            fPrecoEntrada := Close; iDirecaoPosicao := -1;
        end;
    end;

    if IsBought or IsSold then iBarrasEmPosicao := iBarrasEmPosicao + 1
    else iBarrasEmPosicao := 0;

    if IsBought  and ((UsarSaidaIFR and (fIFR >= NivelSaidaCompra))
                                or  (UsarSaidaTempo and (iBarrasEmPosicao >= MaxBarrasPosicao))) then
        ClosePosition;

    if IsSold and ((UsarSaidaIFR and (fIFR <= NivelSaidaVenda))
                            or  (UsarSaidaTempo and (iBarrasEmPosicao >= MaxBarrasPosicao))) then
        ClosePosition;
end;
```

## Cabeçalho Básico do Robô

Todo robô deve iniciar com um cabeçalho comentado contendo:

// Nome do robô
// Objetivo principal
// Identificador único
// Timeframe
// Autor e data

Exemplo:

// priceactionfisica_A1B2C3_60min.ntsl
// Objetivo: Operar rompimentos com base em conceitos de física
// ID: A1B2C3
// Timeframe: 60min
// Autor: Seu Nome - 2026

## Estrutura Básica de uma Estratégia

```pascal
// Definição de parâmetros
input
    parametro_exemplo(14); // Ex: Média de 14 períodos

var
    // Declaração de variáveis

begin
    // Lógica da estratégia

    // Exemplo de condição de compra
    if (condicao_compra) then
        buy at market;

end;
```

## Template de Risco

_(Esta seção deve ser detalhada com o template de gerenciamento de risco padrão a ser incluído em cada robô)_

## Exemplos de Código

_(Adicionar exemplos práticos de robôs ou trechos de código relevantes)_

---

### Exemplo compilável: mar_IFR_01_v1_divergencia_confirmada

```pascal
// mar_IFR_01_v1_divergencia_confirmada.ntsl
// Grupo: IFR_RSI — Tier 1 (#01)
// Descricao: Divergencia bullish/bearish de IFR confirmada por candle de rejeicao
// Setup com maior taxa de acerto do grupo (referencia v4: ~90%).
// Timeframe: 60min (principal), 30min
// Ativo: WIN (minicontrato de indice)
// Versao: 1.0 — marco/2026

input
    PeriodoIFR(9);
    LookbackDivergencia(12);
    DeltaIFRMinimo(2.0);
    MultiplicadorPavio(1.5);
    MaxPavioOpostoCorpo(1.2);
    UsarFiltroVolume(false);
    PeriodoMediaVol(20);
    FatorVolume(1.0);
    UsarSaidaIFR(true);
    NivelSaidaCompra(55);
    NivelSaidaVenda(45);
    UsarSaidaTempo(true);
    MaxBarrasPosicao(12);
    UsarGestaoRisco(true);
    UsarHardLock(true);
    SaldoConta(10000.0);
    RiscoDiaPct(1.5);
    RiscoSemanaPct(3.0);
    MaxStopsConsecutivos(3);
    ValorPorPonto(0.2);
    DiaSemanaReset(2);

var
    iBarrasEmPosicao : integer;
    fIFR, fMediaVol  : float;
    fRange, fCorpo, fPavioSup, fPavioInf : float;
    bMartelo, bEstrela, bVolumeOk        : boolean;
    bDivAlta, bDivBaixa                  : boolean;
    fPrecoEntrada, fResultadoDia, fResultadoSemana : float;
    fLimiteDia, fLimiteSemana, fResultadoPontos, fResultadoReais : float;
    bBloqueioDia, bBloqueioSemana  : boolean;
    iDirecaoPosicao, iStopsConsec  : integer;
    iDiaSemanaAtual                : integer;

begin
    if CurrentBar = 1 then
        Print("Robo ativo: mar_IFR_01_v1_divergencia_confirmada");

    if Date <> Date[1] then
    begin
        iBarrasEmPosicao := 0;
        fResultadoDia    := 0;
        bBloqueioDia     := false;
        iDiaSemanaAtual  := DayOfWeek(Date);
        if iDiaSemanaAtual = DiaSemanaReset then
        begin
            fResultadoSemana := 0;
            bBloqueioSemana  := false;
        end;
    end;

    if UsarGestaoRisco then
    begin
        fLimiteDia    := SaldoConta * (RiscoDiaPct / 100.0);
        fLimiteSemana := SaldoConta * (RiscoSemanaPct / 100.0);
        if (iDirecaoPosicao = 1) and (not IsBought) and (fPrecoEntrada > 0) then
        begin
            fResultadoPontos := Close - fPrecoEntrada;
            fResultadoReais  := fResultadoPontos * ValorPorPonto;
            fResultadoDia    := fResultadoDia + fResultadoReais;
            fResultadoSemana := fResultadoSemana + fResultadoReais;
            if fResultadoReais < 0 then iStopsConsec := iStopsConsec + 1 else iStopsConsec := 0;
            fPrecoEntrada := 0; iDirecaoPosicao := 0;
        end;
        if (iDirecaoPosicao = -1) and (not IsSold) and (fPrecoEntrada > 0) then
        begin
            fResultadoPontos := fPrecoEntrada - Close;
            fResultadoReais  := fResultadoPontos * ValorPorPonto;
            fResultadoDia    := fResultadoDia + fResultadoReais;
            fResultadoSemana := fResultadoSemana + fResultadoReais;
            if fResultadoReais < 0 then iStopsConsec := iStopsConsec + 1 else iStopsConsec := 0;
            fPrecoEntrada := 0; iDirecaoPosicao := 0;
        end;
        if UsarHardLock then
        begin
            if fResultadoDia <= -fLimiteDia then bBloqueioDia := true;
            if fResultadoSemana <= -fLimiteSemana then bBloqueioSemana := true;
            if iStopsConsec >= MaxStopsConsecutivos then bBloqueioDia := true;
        end;
    end;

    fIFR      := IFR(PeriodoIFR);
    fMediaVol := Media(PeriodoMediaVol, Volume);
    bVolumeOk := (not UsarFiltroVolume) or (Volume >= fMediaVol * FatorVolume);

    fRange    := High - Low;
    fCorpo    := Abs(Open - Close);
    fPavioSup := High - Max(Open, Close);
    fPavioInf := Min(Open, Close) - Low;

    bMartelo := (fRange > 0) and (fCorpo > 0)
                     and (fPavioInf >= fCorpo * MultiplicadorPavio)
                     and (fPavioSup <= fCorpo * MaxPavioOpostoCorpo);

    bEstrela := (fRange > 0) and (fCorpo > 0)
                     and (fPavioSup >= fCorpo * MultiplicadorPavio)
                     and (fPavioInf <= fCorpo * MaxPavioOpostoCorpo);

    bDivAlta  := (Low < Lowest(Low, LookbackDivergencia)[1])
                        and (fIFR > (Lowest(IFR(PeriodoIFR), LookbackDivergencia)[1] + DeltaIFRMinimo));
    bDivBaixa := (High > Highest(High, LookbackDivergencia)[1])
                        and (fIFR < (Highest(IFR(PeriodoIFR), LookbackDivergencia)[1] - DeltaIFRMinimo));

    if (not IsBought) and (not IsSold)
    and (not (UsarGestaoRisco and (bBloqueioDia or bBloqueioSemana))) then
    begin
        if bDivAlta and bMartelo and bVolumeOk then
        begin
            BuyAtMarket;
            fPrecoEntrada := Close; iDirecaoPosicao := 1;
        end
        else if bDivBaixa and bEstrela and bVolumeOk then
        begin
            SellShortAtMarket;
            fPrecoEntrada := Close; iDirecaoPosicao := -1;
        end;
    end;

    if IsBought or IsSold then iBarrasEmPosicao := iBarrasEmPosicao + 1
    else iBarrasEmPosicao := 0;

    if IsBought  and ((UsarSaidaIFR and (fIFR >= NivelSaidaCompra))
                                or  (UsarSaidaTempo and (iBarrasEmPosicao >= MaxBarrasPosicao))) then
        ClosePosition;

    if IsSold and ((UsarSaidaIFR and (fIFR <= NivelSaidaVenda))
                            or  (UsarSaidaTempo and (iBarrasEmPosicao >= MaxBarrasPosicao))) then
        ClosePosition;
end;
```
