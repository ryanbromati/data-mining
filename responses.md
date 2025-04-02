# ENTENDIMENTO DOS DADOS
## Introdução à Mineração de Dados

### 1. Técnicas de Mineração de Dados

A Mineração de Dados (MD) engloba diferentes técnicas para identificar padrões úteis em grandes volumes de dados. Considerando o domínio de jogos online, podemos exemplificar:

- **Classificação**: Identificar se um jogador irá abandonar o jogo (churn prediction) com base em padrões de comportamento como tempo médio diário, taxa de vitória e comunicação por voz.
- **Regressão**: Prever o tempo médio que um jogador permanecerá ativo com base em suas características demográficas e estilo de jogo.
- **Clusterização**: Agrupar jogadores com comportamentos similares para identificar perfis como "competitivos", "casuais" e "colecionadores" baseado em suas estatísticas e preferências.
- **Associação**: Descobrir relações entre mapas favoritos, armas preferidas e desempenho no jogo (ex: jogadores que preferem o mapa Dust_II tendem a usar mais a AK-47 e têm maior taxa de headshot).
- **Detecção de anomalias**: Identificar jogadores com comportamentos suspeitos, como aqueles com estatísticas de desempenho inconsistentes que podem indicar uso de cheats.

### 2. Problema e Questões Analíticas (QAs)

**Problema:** Como aumentar a retenção de jogadores em CS:GO e maximizar o engajamento da base de usuários?

**QAs utilizando método SMART:**

1. **QA1**: Quais fatores específicos têm maior correlação com o abandono do jogo nos primeiros 30 dias após o registro? (Específica, Mensurável através de métricas de correlação, Atingível com os dados disponíveis, Relevante para retenção, Temporal - primeiros 30 dias)

2. **QA2**: Quais características de jogadores que aumentaram seu tempo médio diário em pelo menos 20% nos últimos 60 dias e que padrões podem ser identificados? (Específica, Mensurável pelo aumento percentual, Atingível via comparação temporal, Relevante para engajamento, Temporal - últimos 60 dias)

3. **QA3**: Que intervenções específicas podem aumentar a taxa de vitória em 15% para jogadores no quartil inferior de desempenho nos próximos 90 dias? (Específica, Mensurável pelo aumento da taxa, Atingível com implementação de suporte, Relevante para satisfação, Temporal - próximos 90 dias)

4. **QA4**: Como identificar jogadores com potencial competitivo e quais ações podem aumentar em 25% sua progressão para níveis mais altos em 120 dias? (Específica, Mensurável pela progressão de rank, Atingível via programa de treinamento, Relevante para desenvolvimento da comunidade, Temporal - 120 dias)

### 3. Processo de Mineração de Dados

O processo de mineração seguiu o modelo CRISP-DM, focando inicialmente no entendimento e preparação dos dados. O dataset contendo informações de 1.000 jogadores de CS:GO inclui dados demográficos, comportamentais e de desempenho, permitindo análises abrangentes sobre o comportamento dos jogadores e fatores que influenciam sua permanência e engajamento.

As atividades de entendimento e preparação dos dados incluíram:
- Análise exploratória para compreender a distribuição das variáveis
- Identificação de relações entre tempo de jogo, desempenho e retenção
- Engenharia de features para criar novas variáveis como "taxa_vitoria" e "potencial_competitivo"
- Transformação de variáveis categóricas como mapas e armas favoritas
- Normalização de métricas de desempenho para comparação adequada

Estas atividades foram direcionadas para responder às questões analíticas e fornecer insights acionáveis para melhorar a experiência do jogador e aumentar a retenção na plataforma.
