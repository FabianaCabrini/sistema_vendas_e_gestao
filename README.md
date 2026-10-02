[readme_md.md](https://github.com/user-attachments/files/32980669/readme_md.md)
# 📊 Sistema de Vendas e Gestão de Produtos

Este é um projeto interativo em Python para **gestão de vendas e visualização de dados em tempo real**, desenvolvido com a biblioteca **Streamlit**. O sistema permite cadastrar novas vendas, visualizar a base de dados atualizada e acompanhar métricas estratégicas por meio de um dashboard dinâmico.

🔗 **Acesse a aplicação rodando online:** [https://ourmanagement.streamlit.app/](https://ourmanagement.streamlit.app/)

---

## 🚀 Funcionalidades

- **📝 Cadastro de Vendas (Barra Lateral):**
  - Entrada de data, vendedor, produto, quantidade e valor.
  - Registro dinâmico salvo diretamente na base de dados (`vendas.csv`).

- **📋 Tabela de Vendas:**
  - Exibição interativa de todas as vendas cadastradas na base de dados.

- **📈 Dashboard Interativo:**
  - **Métrica de Faturamento Total:** Cálculo automático do faturamento acumulado.
  - **Gráfico de Vendas por Vendedor:** Gráfico de barras indicando o volume de vendas por vendedor e produto.
  - **Gráfico de Participação de Produtos:** Gráfico de pizza mostrando a representatividade de cada produto no faturamento total.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **[Streamlit](https://streamlit.io/):** Criação da interface web interativa.
- **[Pandas](https://pandas.pydata.org/):** Manipulação e leitura da base de dados CSV.
- **[Plotly Express](https://plotly.com/python/plotly-express/):** Criação de gráficos interativos.

---

## 📂 Estrutura do Projeto

```text
├── main.py          # Código principal da aplicação em Streamlit
├── vendas.csv        # Base de dados em formato CSV contendo o histórico de vendas
└── README.md        # Documentação do projeto
```

---

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos
Certifique-se de ter o **Python** instalado em sua máquina.

### 1. Clonar o repositorio
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instalar as dependencias
Execute o comando abaixo no terminal para instalar as bibliotecas necessárias:

```bash
pip install streamlit pandas plotly
```

### 3. Executar a aplicação
Com o arquivo `vendas.csv` na mesma pasta do projeto, execute:

```bash
streamlit run main.py
```

A aplicação abrirá automaticamente no seu navegador padrão no endereço `http://localhost:8501`.

---

## 🌐 Deploy

O projeto está publicado e disponível para uso através do Streamlit Community Cloud:  
👉 [https://ourmanagement.streamlit.app/](https://ourmanagement.streamlit.app/)
