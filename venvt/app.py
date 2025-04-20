import streamlit as st


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