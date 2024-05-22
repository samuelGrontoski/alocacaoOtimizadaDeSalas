# Classes
class Disciplina:
    def __init__(self, descricao, tamanho_turma, inicio, fim):
        self.descricao = descricao
        self.tamanho_turma = tamanho_turma
        self.inicio = inicio
        self.fim = fim

class Sala:
    def __init__(self, identificacao, capacidade):
        self.identificacao = identificacao
        self.capacidade = capacidade
        self.disciplinas = []

# Função para alocar as disciplinas nas salas
def alocar_disciplinas(disciplinas, salas):
    # Ordenar as disciplinas pelo horário de término
    disciplinas.sort(key=lambda x: x.fim)
    # Ordenar as salas pela capacidade
    salas.sort(key=lambda x: x.capacidade)

    # Lista para acompanhar o tempo de término de cada sala
    fim_salas = [0] * len(salas)

    for disciplina in disciplinas:
        # Tenta alocar a disciplina na primeira sala disponível
        alocada = False
        for i, sala in enumerate(salas):
            # Verifica se a sala pode acomodar a turma e está disponível no horário necessário
            if sala.capacidade >= disciplina.tamanho_turma and fim_salas[i] <= disciplina.inicio:
                sala.disciplinas.append(disciplina)
                fim_salas[i] = disciplina.fim
                alocada = True
                break

        # Se não for possível alocar a disciplina em nenhuma sala, adicionar nova sala (se permitido)
        if not alocada:
            print("Não foi possível alocar a disciplina:", disciplina.descricao)

    # Ordenar as salas pelo identificador
    salas.sort(key=lambda x: x.identificacao)
    # Retrona as salas com as disciplinas alocadas
    return salas

# Exemplo de uso
disciplinas = [
    Disciplina("Matemática", 30, 9, 11),
    Disciplina("Física", 20, 12, 14),
    Disciplina("Química", 20, 10, 12),
    Disciplina("Biologia", 35, 9, 10),
    Disciplina("Inglês", 15, 12, 14),
    Disciplina("Alg1", 20, 14, 16),
    Disciplina("Alg2", 25, 8, 10),
    Disciplina("Cálculo 1", 40, 10, 12),
    Disciplina("Cálculo 2", 30, 9, 11),
    Disciplina("Cálculo 3", 25, 11, 13),
    Disciplina("Cálculo Numérico", 15, 10, 12),
]

salas = [
    Sala("Sala A", 30),
    Sala("Sala B", 40),
    Sala("Sala C", 20),
    Sala("Sala D", 20),
]

# Chama a função para alocar as disciplinas nas salas
salas_alocadas = alocar_disciplinas(disciplinas, salas)

# Imprime os dados das salas e disciplinas alocadas
for sala in salas_alocadas:
    print(f"{sala.identificacao}, Capacidade: {sala.capacidade}")
    for disciplina in sala.disciplinas:
        print(f"  Disciplina: {disciplina.descricao}, Tamanho: {disciplina.tamanho_turma}, Início: {disciplina.inicio}, Fim: {disciplina.fim}")
