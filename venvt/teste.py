import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(layout="wide", page_title="Relatórios IPEA", initial_sidebar_state="expanded")


with st.sidebar:
    st.title("IPEA")
    st.text_input("Search for...")
    st.markdown("### 📊 Dashboard")
    st.markdown("### 📁 Relatórios")
    st.markdown("### 🚨 Alertas")
    st.markdown("### 🧠 Análises inteligentes")
    st.markdown("### 📂 Dados")
    st.markdown("---")
    st.markdown("### 👤 User")
    st.markdown("### ⚙️ Configurações")


st.markdown("<h1 style='color: white;'>Relatórios inteligentes IPEA</h1>", unsafe_allow_html=True)


np.random.seed(42)
meses = pd.date_range(start="2024-01-01", end="2024-12-31", freq="M")
receitas = np.random.randint(50, 150, len(meses))
despesas = np.random.randint(30, 120, len(meses))
df = pd.DataFrame({"Mês": meses, "Receitas": receitas, "Despesas": despesas})

# --- Métricas ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="📈 Total de Receitas", value="50.8K", delta="24.8%")
with col2:
    st.metric(label="📉 Total de Despesas", value="23.6K", delta="-12.6%")
with col3:
    st.metric(label="✅ Alertas Ativos", value="3", delta="+1")

# --- Gráfico de Linhas ---
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Mês"], y=df["Receitas"], mode='lines+markers', name='Receitas'))
fig.add_trace(go.Scatter(x=df["Mês"], y=df["Despesas"], mode='lines+markers', name='Despesas'))

fig.update_layout(
    title="Resumo gerado por IA",
    xaxis_title="Mês",
    yaxis_title="Valor (K)",
    legend_title="Legenda",
    template="plotly_dark"
)

col4, col5 = st.columns([2, 1])
with col4:
    st.plotly_chart(fig, use_container_width=True)

with col5:
    st.markdown("""
    <div style='padding: 10px; background-color: #1c1c3c; color: white; border-radius: 10px;'>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ultricies ex sed sapien finibus.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- Velocímetro (Gauge) ---
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=23648,
        title={'text': "Total Processado"},
        gauge={'axis': {'range': [0, 50000]}},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))
    gauge.update_layout(template="plotly_dark", height=300)
    st.plotly_chart(gauge, use_container_width=True)
