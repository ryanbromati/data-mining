import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# Configurar o Faker
fake = Faker()
Faker.seed(42)
np.random.seed(42)

# Função para gerar dados de jogadores de CS:GO
def gerar_dados_csgo(num_jogadores=1000):
    dados = []
    
    # Lista de ranks no CS:GO
    ranks = ['Prata I', 'Prata II', 'Prata III', 'Prata IV', 'Prata Elite', 'Prata Elite Mestre',
             'Ouro I', 'Ouro II', 'Ouro III', 'Ouro IV', 'Mestre Guardião I', 'Mestre Guardião II',
             'Mestre Guardião Elite', 'Distinto Mestre Guardião', 'Águia Lendária', 'Águia Lendária Suprema',
             'Global Elite']
    
    # Lista de mapas
    mapas = ['Dust II', 'Mirage', 'Inferno', 'Nuke', 'Overpass', 'Vertigo', 'Ancient', 'Train', 'Cache', 'Cobblestone']
    
    # Lista de armas favoritas
    armas = ['AK-47', 'M4A4', 'M4A1-S', 'AWP', 'Desert Eagle', 'USP-S', 'Glock-18', 'P250', 'MP9', 'UMP-45', 'MAC-10']
    
    # Data de hoje menos 180 dias para simular dados de 6 meses
    data_final = datetime.now()
    data_inicial = data_final - timedelta(days=180)
    
    for i in range(num_jogadores):
        # Data de registro (aleatória nos últimos 6 meses)
        dias_atras = random.randint(1, 180)
        data_registro = data_final - timedelta(days=dias_atras)
        
        # Determinar se o jogador parou de jogar
        parou_de_jogar = random.random() < 0.25  # 25% de chance de parar de jogar
        
        if parou_de_jogar:
            data_ultima_partida = data_registro + timedelta(days=random.randint(1, min(60, dias_atras)))
            dias_ativos = (data_ultima_partida - data_registro).days
        else:
            data_ultima_partida = data_final - timedelta(days=random.randint(0, 7))  # Jogou nos últimos 7 dias
            dias_ativos = (data_final - data_registro).days
        
        # Mapas favoritos (1 a 4 mapas)
        num_mapas = random.randint(1, 4)
        mapas_favoritos = random.sample(mapas, num_mapas)
        
        # Armas favoritas (1 a 3 armas)
        num_armas = random.randint(1, 3)
        armas_favoritas = random.sample(armas, num_armas)
        
        # Rank atual (ponderado para ter mais jogadores em ranks intermediários)
        distribuicao_ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 10, 7, 4, 1]
        rank_idx = random.choices(range(len(ranks)), weights=distribuicao_ranks)[0]
        rank_atual = ranks[rank_idx]
        
        # Tempo médio diário (em minutos)
        if rank_idx > 10:  # Jogadores de rank alto tendem a jogar mais
            tempo_medio = random.randint(60, 240)
        else:
            tempo_medio = random.randint(30, 180)
        
        # KD Ratio (razão de abates/mortes)
        if rank_idx > 12:  # Jogadores melhores tendem a ter KD ratio melhor
            kd_ratio = round(random.uniform(1.0, 2.5), 2)
        elif rank_idx > 6:
            kd_ratio = round(random.uniform(0.8, 1.5), 2)
        else:
            kd_ratio = round(random.uniform(0.5, 1.1), 2)
        
        # Precisão de tiro (headshot percentage)
        if rank_idx > 12:
            headshot_percentage = random.randint(40, 70)
        elif rank_idx > 6:
            headshot_percentage = random.randint(30, 50)
        else:
            headshot_percentage = random.randint(15, 35)
        
        # Número de partidas jogadas
        partidas_por_dia = tempo_medio / 40  # Aproximadamente 40 minutos por partida
        num_partidas = int(partidas_por_dia * dias_ativos)
        
        # Vitórias
        if rank_idx > 12:
            taxa_vitoria = random.uniform(0.55, 0.65)
        elif rank_idx > 6:
            taxa_vitoria = random.uniform(0.48, 0.55)
        else:
            taxa_vitoria = random.uniform(0.4, 0.5)
            
        vitorias = int(num_partidas * taxa_vitoria)
        
        # Jogador
        jogador = {
            'jogador_id': i + 1000,
            'idade': random.randint(14, 35),
            'genero': random.choice(['M', 'F', 'Outro']),
            'pais': fake.country(),
            'possui_prime': random.choice([True, False]),
            'horas_totais': random.randint(50, 5000),
            'data_registro': data_registro.strftime('%Y-%m-%d'),
            'parou_de_jogar': parou_de_jogar,
            'data_ultima_partida': data_ultima_partida.strftime('%Y-%m-%d'),
            'dias_ativos': dias_ativos,
            'mapas_favoritos': ','.join(mapas_favoritos),
            'armas_favoritas': ','.join(armas_favoritas),
            'rank_atual': rank_atual,
            'tempo_medio_diario_min': tempo_medio,
            'total_partidas': num_partidas,
            'vitorias': vitorias,
            'kd_ratio': kd_ratio,
            'headshot_percentage': headshot_percentage,
            'comunicacao_por_voz': random.randint(0, 100),  # % do tempo que usa comunicação por voz
            'reportes_recebidos': random.randint(0, 20),
            'amigos_no_jogo': random.randint(0, 50),
            'skins_possuidas': random.randint(0, 200),
            'valor_inventario_usd': round(random.uniform(0, 1000), 2)
        }
        
        dados.append(jogador)
    
    return pd.DataFrame(dados)

# Gerar dados brutos
df_csgo = gerar_dados_csgo(1000)

# Entendimento dos Dados
print("ENTENDIMENTO DOS DADOS:")
print(f"Dimensões do dataset: {df_csgo.shape}")
print("\nPrimeiras 5 linhas:")
print(df_csgo.head())

print("\nInformações do dataset:")
print(df_csgo.info())

print("\nEstatísticas descritivas:")
print(df_csgo.describe())

print("\nValores ausentes por coluna:")
print(df_csgo.isnull().sum())

print("\nDistribuição de ranks:")
print(df_csgo['rank_atual'].value_counts())

print("\nTaxa de jogadores inativos:")
print(df_csgo['parou_de_jogar'].value_counts(normalize=True) * 100)

# Preparação dos Dados
print("\nPREPARAÇÃO DOS DADOS:")

# 1. Tratar valores ausentes
df_limpo = df_csgo.copy()
# Não temos valores ausentes neste dataset gerado

# 2. Criar novas características (feature engineering)
# Converter strings de data para datetime
df_limpo['data_registro'] = pd.to_datetime(df_limpo['data_registro'])
df_limpo['data_ultima_partida'] = pd.to_datetime(df_limpo['data_ultima_partida'])

# Calcular quantos dias desde a última partida
df_limpo['dias_desde_ultima_partida'] = (datetime.now() - df_limpo['data_ultima_partida']).dt.days

# Calcular taxa de vitória
df_limpo['taxa_vitoria'] = df_limpo['vitorias'] / df_limpo['total_partidas']

# Calcular valor médio de skin
df_limpo['valor_medio_skin'] = df_limpo['valor_inventario_usd'] / df_limpo['skins_possuidas'].replace(0, 1)

# Identificar jogadores que pararam nos primeiros 30 dias
df_limpo['abandono_precoce'] = (df_limpo['parou_de_jogar'] == True) & (df_limpo['dias_ativos'] <= 30)

# Classificar jogadores por nível de habilidade baseado no rank
def classificar_nivel(rank):
    if rank in ['Prata I', 'Prata II', 'Prata III', 'Prata IV', 'Prata Elite', 'Prata Elite Mestre']:
        return 'Iniciante'
    elif rank in ['Ouro I', 'Ouro II', 'Ouro III', 'Ouro IV']:
        return 'Intermediário'
    elif rank in ['Mestre Guardião I', 'Mestre Guardião II', 'Mestre Guardião Elite', 'Distinto Mestre Guardião']:
        return 'Avançado'
    else:
        return 'Elite'

df_limpo['nivel_habilidade'] = df_limpo['rank_atual'].apply(classificar_nivel)

# Converter mapas_favoritos de string para lista
df_limpo['lista_mapas'] = df_limpo['mapas_favoritos'].str.split(',')

# Criar colunas one-hot para cada mapa
for mapa in ['Dust II', 'Mirage', 'Inferno', 'Nuke', 'Overpass', 'Vertigo', 'Ancient', 'Train', 'Cache', 'Cobblestone']:
    df_limpo[f'mapa_{mapa.replace(" ", "_")}'] = df_limpo['mapas_favoritos'].str.contains(mapa).astype(int)

# Criar colunas one-hot para cada arma favorita
for arma in ['AK-47', 'M4A4', 'M4A1-S', 'AWP', 'Desert Eagle', 'USP-S', 'Glock-18']:
    df_limpo[f'arma_{arma.replace("-", "_").replace(" ", "_")}'] = df_limpo['armas_favoritas'].str.contains(arma).astype(int)

# Criar categorias para tempo de jogo
def categorizar_tempo(minutos):
    if minutos < 60:
        return 'Casual'
    elif minutos < 120:
        return 'Regular'
    else:
        return 'Intenso'

df_limpo['categoria_tempo'] = df_limpo['tempo_medio_diario_min'].apply(categorizar_tempo)

# Identificar potenciais jogadores competitivos
df_limpo['potencial_competitivo'] = ((df_limpo['kd_ratio'] > 1.2) & 
                                   (df_limpo['headshot_percentage'] > 40) &
                                   (df_limpo['taxa_vitoria'] > 0.55)).astype(int)

# 3. Normalizar features numéricas para análise
from sklearn.preprocessing import MinMaxScaler

features_para_normalizar = [
    'tempo_medio_diario_min', 'total_partidas', 'kd_ratio',
    'headshot_percentage', 'comunicacao_por_voz', 'valor_inventario_usd'
]

scaler = MinMaxScaler()
df_limpo[features_para_normalizar] = scaler.fit_transform(df_limpo[features_para_normalizar])

# 4. Codificar variáveis categóricas
df_limpo = pd.get_dummies(df_limpo, columns=['nivel_habilidade', 'categoria_tempo'])

# 5. Remover colunas desnecessárias para modelagem
colunas_para_remover = ['mapas_favoritos', 'armas_favoritas', 'lista_mapas', 'data_registro', 
                        'data_ultima_partida', 'jogador_id', 'pais', 'rank_atual']
df_modelagem = df_limpo.drop(columns=colunas_para_remover)

# Mostrar o resultado final
print("\nDataset preparado para modelagem (primeiras 5 linhas):")
print(df_modelagem.head())

print("\nNovas características criadas:")
novas_features = ['dias_desde_ultima_partida', 'taxa_vitoria', 'valor_medio_skin', 'abandono_precoce',
                 'potencial_competitivo'] + \
                 [col for col in df_modelagem.columns if col.startswith('mapa_')] + \
                 [col for col in df_modelagem.columns if col.startswith('arma_')] + \
                 [col for col in df_modelagem.columns if col.startswith('nivel_habilidade_')] + \
                 [col for col in df_modelagem.columns if col.startswith('categoria_tempo_')]
print(novas_features)

# Preparar dados para cada uma das questões analíticas (QA)
print("\nPreparação específica para as Questões Analíticas:")

# QA1: Fatores que influenciam o abandono do jogo
qa1_data = df_limpo[['parou_de_jogar', 'abandono_precoce', 'tempo_medio_diario_min', 
                     'kd_ratio', 'headshot_percentage', 'taxa_vitoria', 'reportes_recebidos'] + 
                    [col for col in df_limpo.columns if col.startswith('mapa_')] +
                    [col for col in df_limpo.columns if col.startswith('nivel_habilidade_')]]
print("\nQA1 - Dados para análise de fatores de abandono do jogo:")
print(qa1_data.head())

# QA2: Aumento do tempo de jogo através de recomendações de mapas e armas
qa2_data = df_limpo[['tempo_medio_diario_min', 'parou_de_jogar', 'dias_desde_ultima_partida'] + 
                    [col for col in df_limpo.columns if col.startswith('mapa_')] +
                    [col for col in df_limpo.columns if col.startswith('arma_')]]
print("\nQA2 - Dados para análise de aumento de tempo de jogo:")
print(qa2_data.head())

# QA3: Análise de jogadores com baixa taxa de vitória
qa3_data = df_limpo[df_limpo['taxa_vitoria'] < 0.45]
qa3_features = ['parou_de_jogar', 'kd_ratio', 'headshot_percentage', 'comunicacao_por_voz'] + \
               [col for col in df_limpo.columns if col.startswith('arma_')] + \
               [col for col in df_limpo.columns if col.startswith('nivel_habilidade_')]
qa3_data = qa3_data[qa3_features]
print("\nQA3 - Dados para análise de jogadores com baixa taxa de vitória:")
print(qa3_data.head())

# QA4: Identificação de jogadores com potencial competitivo
qa4_data = df_limpo[df_limpo['possui_prime'] == True]
qa4_features = ['potencial_competitivo', 'kd_ratio', 'headshot_percentage', 'taxa_vitoria',
                'tempo_medio_diario_min', 'comunicacao_por_voz'] + \
               [col for col in df_limpo.columns if col.startswith('arma_')]
qa4_data = qa4_data[qa4_features]
print("\nQA4 - Dados p"
"ara identificação de jogadores com potencial competitivo:")
print(qa4_data.head())