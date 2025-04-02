# Questões Analíticas usando o método SMART para CS

## Problema: Otimização da experiência de jogo e retenção de jogadores no CS

### Específica
Qual é a taxa de abandono do jogo nos primeiros 30 dias após o registro e quais fatores de desempenho (K/D ratio, taxa de vitória, precisão de headshot) estão mais correlacionados com esse abandono?

### Mensurável
Como podemos aumentar o tempo médio diário de jogo em 15% nos próximos 3 meses através de recomendações personalizadas de mapas e armas baseadas no perfil de cada jogador?

### Atingível
Quais estratégias de jogo e preferências de armas podem aumentar a taxa de vitória em pelo menos 10% para jogadores com win rate abaixo de 45%, considerando seu nível atual de habilidade?

### Relevante
Como podemos identificar os 5% de jogadores com maior potencial competitivo e quais recursos de treinamento seriam mais eficazes para desenvolvê-los?

### Temporal
Qual a relação entre o tempo de inatividade dos jogadores e seu retorno ao jogo após atualizações de conteúdo (novos mapas, operações, eventos) nos últimos 6 meses?

---

# Entendimento e Preparação de Dados para CS

## Entendimento dos Dados
Na etapa de entendimento dos dados para o conjunto de dados de CS, analisei:

- **Estrutura dos dados**: O conjunto contém informações de 1000 jogadores com 23 variáveis, incluindo:
  - Dados demográficos (idade, gênero, país)
  - Estatísticas de jogo (K/D ratio, headshot percentage, taxa de vitória)
  - Preferências (mapas e armas favoritas)
  - Comportamento (tempo de jogo, comunicação)
- **Estatísticas descritivas**: Examinei as distribuições das variáveis como:
  - Tempo médio diário de jogo
  - Total de partidas jogadas
  - K/D ratio
  - Valor do inventário de skins
- **Valores ausentes**: O conjunto de dados gerado não apresenta valores ausentes.
- **Distribuição de classes**: Analisei a distribuição de ranks no jogo e a taxa de abandono (~25% dos jogadores pararam de jogar nos últimos 6 meses).
- **Relacionamentos entre variáveis**: Observei correlações importantes entre rank, K/D ratio, taxa de headshot e taxa de vitória, mostrando que jogadores de ranks mais altos tendem a apresentar melhores estatísticas de desempenho.

---

## Preparação dos Dados
Para a preparação dos dados de CS, realizei as seguintes atividades:

### Feature Engineering
- Converti datas para formato `datetime`
- Calculei `dias_desde_ultima_partida` para identificar jogadores inativos
- Criei `taxa_vitoria` dividindo vitórias pelo total de partidas
- Calculei `valor_medio_skin` para análise econômica
- Adicionei flag `abandono_precoce` para identificar jogadores que abandonaram nos primeiros 30 dias
- Criei categorização de nível de habilidade baseada no rank
- Transformei as strings de mapas e armas favoritas em colunas one-hot
- Criei categorias de tempo de jogo (Casual, Regular, Intenso)
- Adicionei indicador `potencial_competitivo` baseado em desempenho

### Normalização
- Apliquei `MinMaxScaler` às features numéricas como tempo de jogo, total de partidas e estatísticas de desempenho.

### Codificação de Variáveis Categóricas
- Utilizei **one-hot encoding** para variáveis como nível de habilidade e categoria de tempo de jogo.

### Seleção de Features
Removi colunas desnecessárias e criei conjuntos específicos para cada Questão Analítica:

- **QA1**: Features relacionadas ao abandono do jogo e fatores de desempenho
- **QA2**: Variáveis para análise do tempo de jogo e preferências de mapas/armas
- **QA3**: Dados de jogadores com baixa taxa de vitória
- **QA4**: Informações de jogadores com potencial competitivo

Estas etapas de preparação fornecem dados adequados para modelagem e análise aprofundada de cada uma das questões analíticas definidas, possibilitando a extração de insights valiosos para melhorar a experiência e retenção de jogadores no CS.

