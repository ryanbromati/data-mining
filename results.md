# ENTENDIMENTO DOS DADOS

## Dimensões do dataset
- Registros: 1.000
- Variáveis: 23

## Amostra dos dados

### Primeiras 5 linhas

| jogador_id | idade | genero | pais | possui_prime | horas_totais | data_registro | parou_de_jogar | ... | vitorias | kd_ratio | headshot_percentage | comunicacao_por_voz | reportes_recebidos | amigos_no_jogo | skins_possuidas | valor_inventario_usd |
|------------|-------|--------|------|--------------|--------------|---------------|----------------|-----|----------|----------|---------------------|---------------------|-------------------|----------------|-----------------|----------------------|
| 1000 | 29 | Outro | Northern Mariana Islands | True | 4769 | 2025-02-05 | True | ... | 93 | 1.33 | 43 | 28 | 9 | 44 | 182 | 481.73 |
| 1001 | 23 | M | Bouvet Island (Bouvetoya) | True | 2328 | 2024-11-27 | False | ... | 128 | 1.08 | 25 | 79 | 6 | 43 | 121 | 733.09 |
| 1002 | 28 | Outro | Anguilla | False | 1544 | 2025-03-11 | True | ... | 16 | 0.96 | 23 | 3 | 4 | 46 | 142 | 696.29 |
| 1003 | 35 | M | Saint Vincent and the Grenadines | False | 4326 | 2025-01-17 | False | ... | 159 | 1.59 | 60 | 17 | 1 | 25 | 39 | 574.49 |
| 1004 | 29 | M | Falkland Islands (Malvinas) | False | 829 | 2024-12-31 | False | ... | 153 | 1.68 | 64 | 44 | 13 | 37 | 189 | 911.61 |

## Informações do dataset

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 23 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   jogador_id              1000 non-null   int64  
 1   idade                   1000 non-null   int64  
 2   genero                  1000 non-null   object 
 3   pais                    1000 non-null   object 
 4   possui_prime            1000 non-null   bool   
 5   horas_totais            1000 non-null   int64  
 6   data_registro           1000 non-null   object 
 7   parou_de_jogar          1000 non-null   bool   
 8   data_ultima_partida     1000 non-null   object 
 9   dias_ativos             1000 non-null   int64  
 10  mapas_favoritos         1000 non-null   object 
 11  armas_favoritas         1000 non-null   object 
 12  rank_atual              1000 non-null   object 
 13  tempo_medio_diario_min  1000 non-null   int64  
 14  total_partidas          1000 non-null   int64  
 15  vitorias                1000 non-null   int64  
 16  kd_ratio                1000 non-null   float64
 17  headshot_percentage     1000 non-null   int64  
 18  comunicacao_por_voz     1000 non-null   int64  
 19  reportes_recebidos      1000 non-null   int64  
 20  amigos_no_jogo          1000 non-null   int64  
 21  skins_possuidas         1000 non-null   int64  
 22  valor_inventario_usd    1000 non-null   float64
dtypes: bool(2), float64(2), int64(12), object(7)
memory usage: 166.1+ KB
```

## Estatísticas descritivas

| Estatística | jogador_id | idade | horas_totais | dias_ativos | tempo_medio_diario_min | total_partidas | vitorias | kd_ratio | headshot_percentage | comunicacao_por_voz | reportes_recebidos | amigos_no_jogo | skins_possuidas | valor_inventario_usd |
|-------------|------------|-------|--------------|-------------|------------------------|----------------|----------|----------|---------------------|---------------------|-------------------|----------------|-----------------|----------------------|
| count | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 | 1000.00 |
| mean | 1499.50 | 24.55 | 2476.71 | 75.44 | 122.04 | 227.64 | 118.98 | 1.19 | 39.05 | 49.45 | 10.27 | 24.68 | 98.21 | 509.42 |
| std | 288.82 | 6.24 | 1433.64 | 54.31 | 53.37 | 204.43 | 112.12 | 0.42 | 12.11 | 28.86 | 6.03 | 14.49 | 57.46 | 289.26 |
| min | 1000.00 | 14.00 | 52.00 | 1.00 | 30.00 | 1.00 | 0.00 | 0.50 | 15.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.16 |
| 25% | 1249.75 | 19.00 | 1227.00 | 27.00 | 79.00 | 69.00 | 34.00 | 0.91 | 32.00 | 24.00 | 5.00 | 12.00 | 50.00 | 254.26 |
| 50% | 1499.50 | 25.00 | 2437.50 | 63.00 | 119.00 | 162.50 | 83.00 | 1.13 | 39.00 | 50.00 | 10.00 | 24.00 | 102.00 | 521.53 |
| 75% | 1749.25 | 30.00 | 3684.00 | 119.25 | 160.00 | 334.00 | 173.25 | 1.38 | 46.25 | 74.00 | 16.00 | 37.00 | 146.00 | 765.13 |
| max | 1999.00 | 35.00 | 4990.00 | 180.00 | 240.00 | 1053.00 | 647.00 | 2.50 | 70.00 | 100.00 | 20.00 | 50.00 | 200.00 | 999.83 |

## Análise de dados ausentes
Não há valores ausentes em nenhuma coluna do dataset.

## Distribuição de ranks

| Rank | Contagem |
|------|----------|
| Mestre Guardião Elite | 122 |
| Mestre Guardião II | 109 |
| Mestre Guardião I | 99 |
| Distinto Mestre Guardião | 93 |
| Ouro IV | 92 |
| Ouro III | 91 |
| Prata Elite | 55 |
| Ouro I | 52 |
| Águia Lendária | 51 |
| Ouro II | 50 |
| Prata Elite Mestre | 50 |
| Prata IV | 42 |
| Águia Lendária Suprema | 32 |
| Prata II | 22 |
| Prata III | 21 |
| Global Elite | 13 |
| Prata I | 6 |

## Taxa de jogadores inativos

| Status | Porcentagem |
|--------|-------------|
| Ativos | 74.8% |
| Inativos | 25.2% |

# PREPARAÇÃO DOS DADOS

## Dataset transformado

### Primeiras 5 linhas após transformação

| idade | genero | possui_prime | horas_totais | parou_de_jogar | dias_ativos | ... | nivel_habilidade_Elite | nivel_habilidade_Iniciante | nivel_habilidade_Intermediário | categoria_tempo_Casual | categoria_tempo_Intenso | categoria_tempo_Regular |
|-------|--------|--------------|--------------|----------------|-------------|-----|------------------------|----------------------------|--------------------------------|------------------------|-------------------------|-------------------------|
| 29 | Outro | True | 4769 | True | 51 | ... | False | False | False | False | True | False |
| 23 | M | True | 2328 | False | 126 | ... | False | True | False | False | False | True |
| 28 | Outro | False | 1544 | True | 10 | ... | False | True | False | False | True | False |
| 35 | M | False | 4326 | False | 75 | ... | False | False | False | False | True | False |
| 29 | M | False | 829 | False | 92 | ... | True | False | False | False | False | True |

## Novas características criadas

- dias_desde_ultima_partida
- taxa_vitoria
- valor_medio_skin
- abandono_precoce
- potencial_competitivo
- mapa_Dust_II, mapa_Mirage, mapa_Inferno, mapa_Nuke, mapa_Overpass, mapa_Vertigo, mapa_Ancient, mapa_Train, mapa_Cache, mapa_Cobblestone
- arma_AK_47, arma_M4A4, arma_M4A1_S, arma_AWP, arma_Desert_Eagle, arma_USP_S, arma_Glock_18
- nivel_habilidade_Avançado, nivel_habilidade_Elite, nivel_habilidade_Iniciante, nivel_habilidade_Intermediário
- categoria_tempo_Casual, categoria_tempo_Intenso, categoria_tempo_Regular

# DADOS PREPARADOS PARA QUESTÕES ANALÍTICAS

## QA1 - Fatores de abandono do jogo

| parou_de_jogar | abandono_precoce | tempo_medio_diario_min | kd_ratio | headshot_percentage | taxa_vitoria | ... | nivel_habilidade_Intermediário |
|----------------|------------------|-----------------------|----------|---------------------|--------------|-----|--------------------------------|
| True | False | 0.519048 | 0.415 | 0.509091 | 0.525424 | ... | False |
| False | False | 0.314286 | 0.290 | 0.181818 | 0.423841 | ... | False |
| True | True | 0.557143 | 0.230 | 0.145455 | 0.444444 | ... | False |
| False | False | 0.480952 | 0.545 | 0.818182 | 0.648980 | ... | False |
| False | False | 0.385714 | 0.590 | 0.890909 | 0.600000 | ... | False |

## QA2 - Análise de aumento de tempo de jogo

| tempo_medio_diario_min | parou_de_jogar | dias_desde_ultima_partida | mapa_Dust_II | mapa_Mirage | ... | arma_Glock_18 |
|------------------------|-----------------|-----------------------------|--------------|-------------|-----|--------------|
| 0.519048 | True | 5 | 1 | 0 | ... | 0 |
| 0.314286 | False | 0 | 0 | 0 | ... | 0 |
| 0.557143 | True | 12 | 0 | 0 | ... | 0 |
| 0.480952 | False | 4 | 1 | 0 | ... | 1 |
| 0.385714 | False | 2 | 0 | 0 | ... | 0 |

## QA3 - Jogadores com baixa taxa de vitória

| parou_de_jogar | kd_ratio | headshot_percentage | comunicacao_por_voz | arma_AK_47 | ... | nivel_habilidade_Intermediário |
|----------------|----------|---------------------|---------------------|------------|-----|--------------------------------|
| False | 0.290 | 0.181818 | 0.79 | 0 | ... | False |
| True | 0.230 | 0.145455 | 0.03 | 1 | ... | False |
| False | 0.055 | 0.254545 | 0.30 | 1 | ... | False |
| False | 0.000 | 0.054545 | 0.09 | 0 | ... | True |
| False | 0.235 | 0.000000 | 0.28 | 0 | ... | True |

## QA4 - Jogadores com potencial competitivo

| potencial_competitivo | kd_ratio | headshot_percentage | taxa_vitoria | tempo_medio_diario_min | comunicacao_por_voz | arma_AK_47 | arma_M4A4 | arma_M4A1_S | arma_AWP | arma_Desert_Eagle | arma_USP_S | arma_Glock_18 |
|------------------------|----------|---------------------|--------------|------------------------|---------------------|------------|-----------|-------------|----------|-------------------|------------|--------------|
| 0 | 0.415 | 0.509091 | 0.525424 | 0.519048 | 0.28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0.290 | 0.181818 | 0.423841 | 0.314286 | 0.79 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0.300 | 0.327273 | 0.487654 | 0.500000 | 0.78 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 0.055 | 0.254545 | 0.416667 | 0.628571 | 0.30 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0.570 | 0.690909 | 0.623711 | 0.614286 | 0.53 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |