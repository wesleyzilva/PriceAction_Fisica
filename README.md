📘 Instruções – PriceAction_Fisica 📍 Repositório oficial: PriceAction_Fisica no GitHub

🎯 Objetivo Relacionar conceitos da Física com Price Action.

Aplicar em operações intraday no WIN B3.

Estrutura organizada em Markdown para reduzir requests premium.

Robôs e backtests documentados para facilitar replicação e análise.

📂 Estrutura de Pastas plaintext PriceAction_Fisica/ │ ├── teorias/ │ ├── teoria_fisica.md │ ├── teoria_priceaction.md │ ├── teorias_priceaction_fisica.md │ ├── teoria_backtest.md │ ├── teoria_gerenciamentorisco.md │ └── teoria_onlineVsatraso.md │ ├── robos/ │ ├── instrucao_robos.md │ └── instrucao_backtest.md │ ├── resultados_backtest/ │ ├── anotacao/ │ └── aula_20260312.txt │ ├── padroes/ │ ├── sintaxe_profit.md │ └── convencao_nomes_arquivos.md │ └── PriceAction_Fisica.code-workspace 🔬 Conceitos de Física aplicados ao Price Action Física Fórmula Interpretação no Mercado Força 𝐹
𝑀 ⋅ 𝐴 Cor do candle (RGB) Massa — Deslocamento do preço Velocidade média 𝑣
Δ 𝑠 Δ 𝑡 Variação do preço em intervalo Velocidade instantânea 𝑣
𝑑 𝑠 𝑑 𝑡 Rapidez em ticks/candles curtos Velocidade relativa — Comparação entre ativos/timeframes Aceleração 𝑎
Δ 𝑣 Δ 𝑡 Mudança da velocidade (momentum) Aceleração positiva — Tendência ganhando força Aceleração negativa — Tendência perdendo força Impulso 𝐼
𝐹 ⋅ Δ 𝑡 Rompimentos com volume concentrado Energia Cinética 𝐸
1 2 𝑀 𝑉 2 Intensidade da tendência Potência 𝑃
𝐹 ⋅ 𝑉 Velocidade do deslocamento Inércia — Consolidação/lateralização Atrito — Suportes e resistências Gravidade — Pressão vendedora recorrente Oscilações — Ciclos intraday, ondas Momentum 𝑝
𝑀 ⋅ 𝑉 Força da tendência 📊 Aplicações práticas no intraday WIN B3 Velocidade média → medir deslocamento em intervalos fixos.

Velocidade instantânea → detectar explosões rápidas de preço.

Velocidade relativa → comparar WIN B3 com outros ativos ou ciclos anteriores.

Aceleração positiva → confirma tendência em fortalecimento.

Aceleração negativa → sinaliza exaustão ou reversão.

Impulso → identificar rompimentos com força concentrada.

Energia Cinética → avaliar intensidade de tendências longas.

Potência → medir deslocamento rápido com volume.

Inércia → mapear consolidações (candles pretos).

Atrito → suportes e resistências fortes.

Gravidade → quedas recorrentes após tentativas de alta.

Oscilações → padrões cíclicos intraday.

Momentum → confirmar continuidade de tendência.

🎨 Paleta de Cores (RGB) Candle neutro (inicial): Cinza → (128,128,128)

Compra: Verde → (0,255,0)

Venda: Vermelho → (255,0,0)

Consolidação: Preto → (0,0,0)

Extras:

Cyan → (0,255,255)

Fucsia → (255,0,255)

Marrom → (165,42,42)

Branco → (255,255,255)

📘 Padrões e Convenções Sintaxe NTSL Documentada em sintaxe_profit.md.

Deve incluir template de risco e exemplos de código.

Convenção de nomes de arquivos Estrutura:

Código mar_IDunicocomLetraeNumero_priceactionfisica_60min.ntsl Componentes:

mar → mês do ciclo

IDunicocomLetraeNumero → identificador único (mistura de letras e números, ex: A1B2C3)

priceactionfisica → grupo conceito

60min → timeframe

.ntsl → extensão obrigatória

✅ Exemplos válidos mar_A1B2C3_priceactionfisica_60min.ntsl

abr_X9Y8Z7_priceactionfisica_15min.ntsl

mai_KL45MN_priceactionfisica_5min.ntsl

📂 Workspace VS Code Arquivo PriceAction_Fisica.code-workspace:

json { "folders": [ { "path": "teorias" }, { "path": "robos" }, { "path": "resultados_backtest" }, { "path": "anotacao" }, { "path": "padroes" } ], "settings": { "files.exclude": { "/.git": true, "/.DS_Store": true }, "editor.tabSize": 2, "editor.wordWrap": "on" } }
