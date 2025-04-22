import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import random

st.set_page_config(page_title="Dashboard IPEA", layout="wide")

# Estilização externa
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📊 IPEA")
    st.text_input("🔍 Search for...")
    st.markdown("### 📂 Navegação")
    st.button(" 🟣 Dashboard")
    st.button("Relatórios")
    st.button("Alertas")
    st.button("Análises inteligentes")
    st.button("Dados")
    st.markdown("---")
    st.button("👤 User")
    st.button("⚙️ Configurações")

# Título
st.markdown("<h1 class='titulo'>Relatórios inteligentes IPEA</h1>", unsafe_allow_html=True)

# Métricas
col1, col2, col3 = st.columns(3)
col1.metric("📈 Total de Receitas", "50.8K", "28.4%")
col2.metric("📉 Total de Despesas", "23.6K", "-12.6%")
col3.metric("🔔 Alertas Ativos", "3", "3.1%")

st.markdown("## ")

# Gráfico e painel lateral
col4, col5 = st.columns([3, 2])

# Gráfico
df = pd.DataFrame({
    "Meses": pd.date_range("2023-01-01", periods=12, freq="M"),
    "Receitas": [random.randint(80, 240) for _ in range(12)],
    "Despesas": [random.randint(60, 180) for _ in range(12)],
})

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Meses"], y=df["Receitas"], name="Receitas", line=dict(color="#A020F0")))
fig.add_trace(go.Scatter(x=df["Meses"], y=df["Despesas"], name="Despesas", line=dict(color="#00CFFF")))
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

col4.plotly_chart(fig, use_container_width=True)

# Texto lateral e indicador
with col5:
    st.markdown(
        """
        <div class='painel'>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque urna mi, varius nec tincidunt sed.</p>
        <h2 class='valor-indicador'>23,648</h2>
        </div>
        """, unsafe_allow_html=True
    )
