import tkinter as tk
from tkinter import ttk

# Classes
class Disciplina:
    def __init__(self, descricao, tamanho_turma, hora_inicio, hora_fim):
        self.descricao = descricao
        self.tamanho_turma = tamanho_turma
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim

class Sala:
    def __init__(self, identificacao, capacidade):
        self.identificacao = identificacao
        self.capacidade = capacidade
        self.disciplinas = []

# Variável para armazenar as disciplinas não alocadas
disciplinasNaoAlocadas = []

# Função que converte uma string de hora no formato HH:MM para minutos
def hora_para_minutos(hora):
    # Tenta converter a string de hora para minutos
    try:
        h, m = map(int, hora.split(':'))
        return h * 60 + m
    # Se não for possível converter, lança uma exceção
    except ValueError:
        raise ValueError(f"Formato de hora inválido: {hora}. Use o formato HH:MM.")

# Função para ler as disciplinas de um arquivo .txt
def ler_disciplinas(arquivo):
    # Lista para armazenar as disciplinas
    disciplinas = []
    # Abre o arquivo .txt e lê as disciplinas e fecha o arquivo automaticamente após a leitura
    with open(arquivo, 'r', encoding='utf-8') as f:
        # Lê cada linha do arquivo e separa os dados da disciplina, e adiciona à lista
        for linha in f:
            partes = linha.strip().split(', ')
            descricao = partes[0]
            tamanho_turma = int(partes[1])
            hora_inicio = partes[2]
            hora_fim = partes[3]
            # Adiciona a disciplina à lista
            disciplinas.append(Disciplina(descricao, tamanho_turma, hora_inicio, hora_fim))
    # Retorna a lista de disciplinas        
    return disciplinas

# Função para ler as salas de um arquivo .txt
def ler_salas(arquivo):
    # Lista para armazenar as salas
    salas = []
    # Abre o arquivo .txt e lê as salas e fecha o arquivo automaticamente após a leitura
    with open(arquivo, 'r', encoding='utf-8') as f:
        # Lê cada linha do arquivo e separa os dados da sala, e adiciona à lista
        for linha in f:
            partes = linha.strip().split(', ')
            identificacao = partes[0]
            capacidade = int(partes[1])
            # Adiciona a sala à lista
            salas.append(Sala(identificacao, capacidade))
    # Retorna a lista de salas
    return salas

# Função para alocar as disciplinas nas salas
def alocar_disciplinas(disciplinas, salas):
    # Lista para acompanhar o tempo de término das últimas disciplinas alocadas em cada sala
    fim_salas = [0] * len(salas)

    # Para cada disciplina, tenta alocar em uma sala disponível
    for disciplina in disciplinas:
        # Converte os horários de início e fim da disciplina para minutos
        inicio_min = hora_para_minutos(disciplina.hora_inicio)
        fim_min = hora_para_minutos(disciplina.hora_fim)
        # Tenta alocar a disciplina na primeira sala disponível
        alocada = False
        for i, sala in enumerate(salas):
            # Verifica se a sala pode acomodar a turma e está disponível no horário necessário
            if sala.capacidade >= disciplina.tamanho_turma and fim_salas[i] <= inicio_min:
                # Se a sala puder acomodar a turma e estiver disponível, aloca a disciplina
                sala.disciplinas.append(disciplina)
                # Atualiza o tempo de término da última disciplina alocada na sala
                fim_salas[i] = fim_min
                # Disciplina alocada com sucesso
                alocada = True
                # Sai do loop interno
                break

        # Se não for possível alocar a disciplina em nenhuma sala, imprime uma mensagem de aviso
        if not alocada:
            disciplinasNaoAlocadas.append(disciplina)

    # Ordena as salas pelo identificador
    salas.sort(key=lambda x: x.identificacao)

    # Retrona as salas com as disciplinas alocadas
    return salas

def exibir_disciplinas_nao_alocadas():
    print("\nDisciplinas não alocadas:")
    for disciplina in disciplinasNaoAlocadas:
        print(f"{disciplina.descricao}\tTamanho: {disciplina.tamanho_turma}\tInício: {disciplina.hora_inicio}\tFim: {disciplina.hora_fim}")

# Leitura dos arquivos .txt com as disciplinas e salas
disciplinas = ler_disciplinas('disciplinas.txt')
salas = ler_salas('salas.txt')

# Ordena as disciplinas pelo horário de início e as salas pela capacidade de forma crescente
disciplinas.sort(key=lambda x: x.hora_fim)
salas.sort(key=lambda x: x.capacidade)

# Chama a função para alocar as disciplinas nas salas
disciplinasAlocadas = alocar_disciplinas(disciplinas, salas)

# Imprime os dados das salas com suas respectivas disciplinas alocadas
print("\n")
for sala in disciplinasAlocadas:
    print(f"{sala.identificacao}, Capacidade: {sala.capacidade}")
    for disciplina in sala.disciplinas:
        print(f"  Disciplina: {disciplina.descricao}\tTamanho: {disciplina.tamanho_turma}\tInício: {disciplina.hora_inicio}\tFim: {disciplina.hora_fim}")
    print("\n")

# Exibe as disciplinas não alocadas
exibir_disciplinas_nao_alocadas()

# Função para exibir a alocação na interface gráfica
def exibir_alocacao(disciplinasAlocadas, disciplinasNaoAlocadas):
    # Limpa a árvore
    for item in tree.get_children():
        tree.delete(item)

    # Adiciona os dados das salas na árvore
    for sala in disciplinasAlocadas:
        sala_id = tree.insert('', 'end', text=f"{sala.identificacao} ({sala.capacidade} alunos)", values=('', '', '', ''))
        for disciplina in sala.disciplinas:
            tree.insert(sala_id, 'end', values=(disciplina.descricao, disciplina.tamanho_turma, disciplina.hora_inicio, disciplina.hora_fim))
        tree.item(sala_id, open=True)

        # Adiciona uma linha de separação após cada sala
        tree.insert('', 'end', values=('', '', '', ''), tags=('separator'))

    # Adiciona uma linha de separação antes das disciplinas não alocadas
    tree.insert('', 'end', values=('', '', '', ''), tags=('separator'))

    # Adiciona as disciplinas não alocadas na árvore
    nao_alocadas_id = tree.insert('', 'end', text="Disciplinas Não Alocadas", values=('', '', '', ''))
    for disciplina in disciplinasNaoAlocadas:
        tree.insert(nao_alocadas_id, 'end', values=(disciplina.descricao, disciplina.tamanho_turma, disciplina.hora_inicio, disciplina.hora_fim))
    tree.item(nao_alocadas_id, open=True)

# Interface gráfica
root = tk.Tk()
root.title("Alocação Otimizada de Disciplinas em Salas de Aula")
root.geometry("960x540")

# Frame para a árvore
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='both', expand=True)

# Configura a árvore
columns = ('Disciplina', 'Tamanho da Turma', 'Início', 'Término')
tree = ttk.Treeview(frame, columns=columns, show='tree headings')
tree.pack(side='left', fill='both', expand=True)

# Barra de rolagem para a árvore
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')
tree.configure(yscrollcommand=scrollbar.set)

# Configuração das colunas
tree.heading('#0', text='Sala (Capacidade)')
tree.heading('Disciplina', text='Disciplina')
tree.heading('Tamanho da Turma', text='Tamanho da Turma')
tree.heading('Início', text='Início')
tree.heading('Término', text='Término')

tree.column('#0', width=80, anchor='w')
tree.column('Disciplina', width=200, anchor='w')
tree.column('Tamanho da Turma', width=80, anchor='center')
tree.column('Início', width=80, anchor='center')
tree.column('Término', width=80, anchor='center')

# Estilo da árvore
style = ttk.Style()
style.configure('Treeview', rowheight=25, font=('Roboto', 10))

# Exibir a alocação na interface gráfica com as listas de disciplinas alocadas e não alocadas
exibir_alocacao(disciplinasAlocadas, disciplinasNaoAlocadas)

# Inicia a aplicação
root.mainloop()