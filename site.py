import streamlit as st

# Título da página
st.title('CRUD de Produtos')

# Barra lateral para seleção de ações
opcao = st.sidebar.selectbox('Selecione uma ação', ('Adicionar Produto', 'Listar Produtos'))

# Dicionário simulando uma base de dados de produtos
produtos = [
    {'id': 1, 'nome': 'Produto 1', 'preco': 19.99},
    {'id': 2, 'nome': 'Produto 2', 'preco': 29.99},
    {'id': 3, 'nome': 'Produto 3', 'preco': 39.99},
]

# Função para listar produtos
def listar_produtos():
    st.subheader('Lista de Produtos')
    for produto in produtos:
        st.write(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}")

# Função para adicionar produto
def adicionar_produto():
    st.subheader('Adicionar Produto')
    nome = st.text_input('Nome do Produto')
    preco = st.number_input('Preço do Produto')
    if st.button('Adicionar'):  # Correção na função
        novo_produto = {'id': len(produtos) + 1, 'nome': nome, 'preco': preco}
        produtos.append(novo_produto)
        st.success('Produto adicionado com sucesso!')

# Lógica para as opções selecionadas na barra lateral
if opcao == 'Adicionar Produto':
    adicionar_produto()
elif opcao == 'Listar Produtos':
    listar_produtos()
