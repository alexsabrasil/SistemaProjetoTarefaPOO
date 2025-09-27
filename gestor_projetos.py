# Importamos para gerar IDs únicos 
import uuid

# Classe Gestor: Representa o gerente de projetos
class Gestor:
    def __init__(self, nome):
        self.id = str(uuid.uuid4())[:8]  # ID único curto
        self.nome = nome

# Classe Projeto: Representa um projeto gerenciado por um gestor
class Projeto:
    def __init__(self, nome, id_gestor):
        self.id = str(uuid.uuid4())[:8]  # ID único curto
        self.nome = nome
        self.id_gestor = id_gestor

# Classe Tarefa: Representa uma tarefa em um projeto
class Tarefa:
    def __init__(self, descricao, id_projeto, status="pendente"):
        self.id = str(uuid.uuid4())[:8]  # ID único curto
        self.descricao = descricao
        self.id_projeto = id_projeto
        self.status = status

# Listas para armazenar os objetos (banco de dados simples em memória)
gestores = []
projetos = []
tarefas = []

# Funções CRUD para Gestor
def create_gestor(nome):
    gestor = Gestor(nome)
    gestores.append(gestor)
    print(f"Gestor criado: ID={gestor.id}, Nome={gestor.nome}")

def read_gestores():
    if not gestores:
        print("Nenhum gestor cadastrado.")
    for g in gestores:
        print(f"ID={g.id}, Nome={g.nome}")

def update_gestor(id_gestor, novo_nome):
    for g in gestores:
        if g.id == id_gestor:
            g.nome = novo_nome
            print(f"Gestor atualizado: ID={g.id}, Nome={g.nome}")
            return
    print("Gestor não encontrado.")

def delete_gestor(id_gestor):
    global gestores
    gestores = [g for g in gestores if g.id != id_gestor]
    print(f"Gestor deletado: ID={id_gestor}")

# Funções CRUD para Projeto
def create_projeto(nome, id_gestor):
    projeto = Projeto(nome, id_gestor)
    projetos.append(projeto)
    print(f"Projeto criado: ID={projeto.id}, Nome={projeto.nome}, Gestor ID={projeto.id_gestor}")

def read_projetos():
    if not projetos:
        print("Nenhum projeto cadastrado.")
    for p in projetos:
        print(f"ID={p.id}, Nome={p.nome}, Gestor ID={p.id_gestor}")

def update_projeto(id_projeto, novo_nome):
    for p in projetos:
        if p.id == id_projeto:
            p.nome = novo_nome
            print(f"Projeto atualizado: ID={p.id}, Nome={p.nome}")
            return
    print("Projeto não encontrado.")

def delete_projeto(id_projeto):
    global projetos
    projetos = [p for p in projetos if p.id != id_projeto]
    print(f"Projeto deletado: ID={id_projeto}")

# Funções CRUD para Tarefa
def create_tarefa(descricao, id_projeto):
    tarefa = Tarefa(descricao, id_projeto)
    tarefas.append(tarefa)
    print(f"Tarefa criada: ID={tarefa.id}, Descrição={tarefa.descricao}, Projeto ID={tarefa.id_projeto}, Status={tarefa.status}")

def read_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    for t in tarefas:
        print(f"ID={t.id}, Descrição={t.descricao}, Projeto ID={t.id_projeto}, Status={t.status}")

def update_tarefa(id_tarefa, novo_status):
    for t in tarefas:
        if t.id == id_tarefa:
            t.status = novo_status
            print(f"Tarefa atualizada: ID={t.id}, Status={t.status}")
            return
    print("Tarefa não encontrada.")

def delete_tarefa(id_tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t.id != id_tarefa]
    print(f"Tarefa deletada: ID={id_tarefa}")

# Menu principal para interagir (exemplo de uso)
def menu():
    while True:
        print("\nMenu CRUD:")
        print("1. Criar Gestor")
        print("2. Listar Gestores")
        print("3. Atualizar Gestor")
        print("4. Deletar Gestor")
        print("5. Criar Projeto")
        print("6. Listar Projetos")
        print("7. Atualizar Projeto")
        print("8. Deletar Projeto")
        print("9. Criar Tarefa")
        print("10. Listar Tarefas")
        print("11. Atualizar Tarefa")
        print("12. Deletar Tarefa")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do gestor: ")
            create_gestor(nome)
        elif opcao == "2":
            read_gestores()
        elif opcao == "3":
            id_g = input("ID do gestor: ")
            novo_nome = input("Novo nome: ")
            update_gestor(id_g, novo_nome)
        elif opcao == "4":
            id_g = input("ID do gestor: ")
            delete_gestor(id_g)
        elif opcao == "5":
            nome = input("Nome do projeto: ")
            id_g = input("ID do gestor: ")
            create_projeto(nome, id_g)
        elif opcao == "6":
            read_projetos()
        elif opcao == "7":
            id_p = input("ID do projeto: ")
            novo_nome = input("Novo nome: ")
            update_projeto(id_p, novo_nome)
        elif opcao == "8":
            id_p = input("ID do projeto: ")
            delete_projeto(id_p)
        elif opcao == "9":
            desc = input("Descrição da tarefa: ")
            id_p = input("ID do projeto: ")
            create_tarefa(desc, id_p)
        elif opcao == "10":
            read_tarefas()
        elif opcao == "11":
            id_t = input("ID da tarefa: ")
            novo_status = input("Novo status (ex: concluída): ")
            update_tarefa(id_t, novo_status)
        elif opcao == "12":
            id_t = input("ID da tarefa: ")
            delete_tarefa(id_t)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

# Rodar o menu
if __name__ == "__main__":
    menu()