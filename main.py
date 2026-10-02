import streamlit as st
import pandas as pd
import plotly.express as px


# streamlit run main.py

# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de vendas")

# seção de cadastro de vendas
# sidebar gera uma barra lateral
st.sidebar.write("## Cadastrar vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Mariana Alvez", "Bruno Alencar", "Flávia Matos"])
produto =  st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1) #o step define o número como inteiro
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar")

# lógica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) # pega o total da tabela
    tabela_vendas.loc[ultima_linha] = nova_venda # adicionar nova venda a ultima linha da tabela
    tabela_vendas.to_csv("vendas.csv", index = False) # transforma a tabela em arquivo csv e atualiza as vendas sem o indice do site
    st.success("Venda cadastrada !")

# seção de visualizar as vendas
st.write("## Vendas cadastradas")
st.dataframe(tabela_vendas) # tabela python

# seção de Dashboard
st.write("## Dashboard")

# card / métrica
faturamento = tabela_vendas["valor"].sum() # somar toda a coluna de valor da base de dados
st.metric("Faturamento Toral", f"R$ {faturamento}")# cria card com o faturamento

# gráfico de barra
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto") # criar gráfico e definir cor para produto
st.plotly_chart(grafico1) # exibir o gráfico


# gráfico de pizza
grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
st.plotly_chart(grafico2)