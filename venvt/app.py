import streamlit as st
import pandas as pd
import numpy as np


#Textos
st.header('Minha dashboard')
st.write("Meu texto com st.write()")
#se eu quiser criar uma sidebar 
st.sidebar.text("Escolha o elemento que deseja filtrar")
#qualquer elemento que quiser colocar na sidebar dem que colocar o .sidebar no st
st.markdown("# Meu titulo")
#da pra ultilizar markdown 

st.caption("Minha legenda")

#formato de legenda, mais claro 

pessoas = [
    {'Nome': 'Eduarda', 'Idade': '19'},
    {'Nome': 'Rony', 'Idade': '11'}
]

st.write("## Pessoas", pessoas)

#Exibição de dados

#Principalmente com panda 
#Instalar Panda 
#instalar nunpy, ferramenta do python que trabalha com algebra linear e matemática, criando dados e vetores atravez do python  


df = pd.DataFrame(
    np.random.rand(10, 3), #3 é a quatidade de parametros que vão ter as colunas, e 10 as linhas
    columns= ['Preço', 'Taxa de ocupação', 'Taxa de Inadimplencia']

    
)