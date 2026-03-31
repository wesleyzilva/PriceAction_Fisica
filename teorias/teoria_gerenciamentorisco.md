# Teoria do Gerenciamento de Risco

O gerenciamento de risco é o pilar mais importante para a sobrevivência e o sucesso no day trade. Nenhuma estratégia, por melhor que seja, é lucrativa sem um controle de risco rigoroso.

## Conceitos Chave

- **Stop Loss:** Ordem programada para fechar uma operação quando ela atinge um determinado nível de prejuízo. É a sua principal ferramenta de proteção. **Nunca opere sem stop loss.**

- **Stop Gain (Alvo):** Ordem para realizar o lucro quando a operação atinge uma meta pré-definida. Garante que você saia da operação com ganho antes que o mercado reverta.

- **Risco x Retorno:** Relação entre o potencial de perda (stop loss) e o potencial de ganho (alvo) de uma operação. Busque operações onde o retorno potencial seja significativamente maior que o risco (ex: 2:1, 3:1).

- **Tamanho da Posição (Position Sizing):** Definir quantos contratos operar com base no tamanho da sua conta e no seu risco máximo por operação. O objetivo é garantir que uma única perda não comprometa uma parte significativa do seu capital.

- **Risco Diário/Semanal:** Estabelecer um limite máximo de perda por dia e por semana. Se atingido, pare de operar. Isso protege seu capital e seu estado emocional.

## Aplicação no Projeto

Todos os robôs desenvolvidos neste projeto devem, obrigatoriamente, incluir parâmetros configuráveis para stop loss e stop gain. A lógica de gerenciamento de risco será documentada e validada nos backtests.
