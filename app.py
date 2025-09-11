import streamlit as st
import uuid
import pandas as pd

# Classes (mesmas do projeto original)
class Gestor:
    def __init__(self, nome):
        self.id = str(uuid.uuid4())[:8]
        self.nome = nome

class Projeto:
    def __init__(self, nome, id_gestor):
        self.id = str(uuid.uuid4())[:8]
        self.nome = nome
        self.id_gestor = id_gestor

class Tarefa:
    def __init__(self, descricao, id_projeto, status="pendente"):
        self.id = str(uuid.uuid4())[:8]
        self.descricao = descricao
        self.id_projeto = id_projeto
        self.status = status

# Listas para armazenar os objetos
if 'gestores' not in st.session_state:
    st.session_state.gestores = []
if 'projetos' not in st.session_state:
    st.session_state.projetos = []
if 'tarefas' not in st.session_state:
    st.session_state.tarefas = []

# Funções CRUD para Gestor
def create_gestor(nome):
    gestor = Gestor(nome)
    st.session_state.gestores.append(gestor)
    st.success(f"Gestor criado: ID={gestor.id}, Nome={gestor.nome}")

def read_gestores():
    if not st.session_state.gestores:
        st.warning("Nenhum gestor cadastrado.")
        return
    df = pd.DataFrame([(g.id, g.nome) for g in st.session_state.gestores], columns=["ID", "Nome"])
    st.dataframe(df)

def update_gestor(id_gestor, novo_nome):
    for g in st.session_state.gestores:
        if g.id == id_gestor:
            g.nome = novo_nome
            st.success(f"Gestor atualizado: ID={g.id}, Nome={g.nome}")
            return
    st.error("Gestor não encontrado.")

def delete_gestor(id_gestor):
    st.session_state.gestores = [g for g in st.session_state.gestores if g.id != id_gestor]
    st.success(f"Gestor deletado: ID={id_gestor}")

# Funções CRUD para Projeto
def create_projeto(nome, id_gestor):
    projeto = Projeto(nome, id_gestor)
    st.session_state.projetos.append(projeto)
    st.success(f"Projeto criado: ID={projeto.id}, Nome={projeto.nome}, Gestor ID={projeto.id_gestor}")

def read_projetos():
    if not st.session_state.projetos:
        st.warning("Nenhum projeto cadastrado.")
        return
    df = pd.DataFrame([(p.id, p.nome, p.id_gestor) for p in st.session_state.projetos], columns=["ID", "Nome", "Gestor ID"])
    st.dataframe(df)

def update_projeto(id_projeto, novo_nome):
    for p in st.session_state.projetos:
        if p.id == id_projeto:
            p.nome = novo_nome
            st.success(f"Projeto atualizado: ID={p.id}, Nome={p.nome}")
            return
    st.error("Projeto não encontrado.")

def delete_projeto(id_projeto):
    st.session_state.projetos = [p for p in st.session_state.projetos if p.id != id_projeto]
    st.success(f"Projeto deletado: ID={id_projeto}")

# Funções CRUD para Tarefa
def create_tarefa(descricao, id_projeto):
    tarefa = Tarefa(descricao, id_projeto)
    st.session_state.tarefas.append(tarefa)
    st.success(f"Tarefa criada: ID={tarefa.id}, Descrição={tarefa.descricao}, Projeto ID={tarefa.id_projeto}, Status={tarefa.status}")

def read_tarefas():
    if not st.session_state.tarefas:
        st.warning("Nenhuma tarefa cadastrada.")
        return
    df = pd.DataFrame([(t.id, t.descricao, t.id_projeto, t.status) for t in st.session_state.tarefas], 
                      columns=["ID", "Descrição", "Projeto ID", "Status"])
    st.dataframe(df)

def update_tarefa(id_tarefa, novo_status):
    for t in st.session_state.tarefas:
        if t.id == id_tarefa:
            t.status = novo_status
            st.success(f"Tarefa atualizada: ID={t.id}, Status={t.status}")
            return
    st.error("Tarefa não encontrada.")

def delete_tarefa(id_tarefa):
    st.session_state.tarefas = [t for t in st.session_state.tarefas if t.id != id_tarefa]
    st.success(f"Tarefa deletada: ID={id_tarefa}")

# Interface Streamlit
st.title("Gestor de Projetos e Tarefas")

# Abas para cada entidade
tab1, tab2, tab3 = st.tabs(["Gestores", "Projetos", "Tarefas"])

# Aba Gestores
with tab1:
    st.header("Gerenciar Gestores")
    with st.form("form_gestor"):
        nome_gestor = st.text_input("Nome do Gestor")
        submit_gestor = st.form_submit_button("Criar Gestor")
        if submit_gestor and nome_gestor:
            create_gestor(nome_gestor)
    
    st.subheader("Listar Gestores")
    read_gestores()
    
    st.subheader("Atualizar Gestor")
    id_gestor_update = st.text_input("ID do Gestor para Atualizar")
    novo_nome_gestor = st.text_input("Novo Nome")
    if st.button("Atualizar Gestor"):
        if id_gestor_update and novo_nome_gestor:
            update_gestor(id_gestor_update, novo_nome_gestor)
    
    st.subheader("Deletar Gestor")
    id_gestor_delete = st.text_input("ID do Gestor para Deletar")
    if st.button("Deletar Gestor"):
        if id_gestor_delete:
            delete_gestor(id_gestor_delete)

# Aba Projetos
with tab2:
    st.header("Gerenciar Projetos")
    with st.form("form_projeto"):
        nome_projeto = st.text_input("Nome do Projeto")
        id_gestor_projeto = st.text_input("ID do Gestor")
        submit_projeto = st.form_submit_button("Criar Projeto")
        if submit_projeto and nome_projeto and id_gestor_projeto:
            create_projeto(nome_projeto, id_gestor_projeto)
    
    st.subheader("Listar Projetos")
    read_projetos()
    
    st.subheader("Atualizar Projeto")
    id_projeto_update = st.text_input("ID do Projeto para Atualizar")
    novo_nome_projeto = st.text_input("Novo Nome do Projeto")
    if st.button("Atualizar Projeto"):
        if id_projeto_update and novo_nome_projeto:
            update_projeto(id_projeto_update, novo_nome_projeto)
    
    st.subheader("Deletar Projeto")
    id_projeto_delete = st.text_input("ID do Projeto para Deletar")
    if st.button("Deletar Projeto"):
        if id_projeto_delete:
            delete_projeto(id_projeto_delete)

# Aba Tarefas
with tab3:
    st.header("Gerenciar Tarefas")
    with st.form("form_tarefa"):
        desc_tarefa = st.text_input("Descrição da Tarefa")
        id_projeto_tarefa = st.text_input("ID do Projeto")
        submit_tarefa = st.form_submit_button("Criar Tarefa")
        if submit_tarefa and desc_tarefa and id_projeto_tarefa:
            create_tarefa(desc_tarefa, id_projeto_tarefa)
    
    st.subheader("Listar Tarefas")
    read_tarefas()
    
    st.subheader("Atualizar Tarefa")
    id_tarefa_update = st.text_input("ID da Tarefa para Atualizar")
    novo_status_tarefa = st.text_input("Novo Status (ex: concluída)")
    if st.button("Atualizar Tarefa"):
        if id_tarefa_update and novo_status_tarefa:
            update_tarefa(id_tarefa_update, novo_status_tarefa)
    
    st.subheader("Deletar Tarefa")
    id_tarefa_delete = st.text_input("ID da Tarefa para Deletar")
    if st.button("Deletar Tarefa"):
        if id_tarefa_delete:
            delete_tarefa(id_tarefa_delete)