import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import requests
import time

# --- Configuração da Página ---
st.set_page_config(layout="wide")

# --- CSS Personalizado ---
st.markdown(
    """
    <style>
    .header {
        font-size: 24px;
        font-weight: bold;
        color: #003366;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 18px;
        color: #003366;
        margin-bottom: 10px;
    }
    .metric-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #003366;
        color: white;
        border-radius: 5px;
        padding: 8px 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Título e Cabeçalho ---
st.markdown('<div class="header">IPEA</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Relatórios inteligentes IPEA</div>', unsafe_allow_html=True)

# --- Layout Principal (2 colunas) ---
col1, col2 = st.columns([2, 1])

# --- Coluna 1: Gráfico de Linhas ---
with col1:
    st.markdown('<div class="subheader">Gráfico</div>', unsafe_allow_html=True)
    
    # Simulação de dados da API do IPEA (substitua pela chamada real)
    data = {
        "Ano": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        "Valor": [5, 10, 8, 12, 15, 18, 20, 22, 25, 28, 30]
    }
    df = pd.DataFrame(data)
    
    fig, ax = plt.subplots()
    ax.plot(df["Ano"], df["Valor"], marker='o', color='#003366')
    ax.set_xlabel("Ano")
    ax.set_ylabel("Valor")
    ax.grid(True)
    st.pyplot(fig)

# --- Coluna 2: Velocímetro e Status da API ---
with col2:
    # --- Caixa de Status da API (Parte Superior) ---
    st.markdown('<div class="metric-box">Status da API</div>', unsafe_allow_html=True)
    
    # Simulação de conexão com a API
    api_status = st.empty()
    try:
        # Substitua pela chamada real à API do IPEA
        response = requests.get("https://www.ipea.gov.br/api/indicadores", timeout=5)
        if response.status_code == 200:
            api_status.success("✅ Conectado à API do IPEA")
        else:
            api_status.error("⚠️ API indisponível")
    except:
        api_status.error("❌ Falha na conexão com a API")
    
    # --- Velocímetro (Parte Inferior) ---
    st.markdown('<div class="subheader">Velocímetro</div>', unsafe_allow_html=True)
    
    # Criando um velocímetro com Plotly
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=75,  # Substitua pelo valor real da API
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Progresso"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#003366"},
            'steps': [
                {'range': [0, 50], 'color': 'lightgray'},
                {'range': [50, 100], 'color': 'gray'}
            ],
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

# --- Botão para Atualizar Dados ---
if st.button("Atualizar Dados"):
    with st.spinner("Atualizando..."):
        time.sleep(2)  # Simula uma chamada à API
        st.success("Dados atualizados!")