from aluno import cad_aluno
#estruturas de dados
disciplinas = []
turmas = []

#função pra cadastrar os dados de disciplinas
def cad_disciplina(nome, codigo, carga_horaria):
    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": None
    }
    disciplinas.append(disciplina)

#listagem, retorna a estrutura "disciplinas"
def listar_disciplinas():
    return disciplinas

#função de cadastro de turmas
def cad_turma(nome, codigo, codigo_disciplina):
    turma = {
        "nome": nome,
        "codigo": codigo,
        "codigo_disciplina": codigo_disciplina,
        "professor": None,
        "alunos": [] #uma lista vazia é obrigatória, já que podem existir vários alunos numa turma
    }
    turmas.append(turma)
    
#listagem, bla bla bla
def listar_turmas():
    return turmas

#função de alocação, rodando um for pra cada disciplina na estrutura e verificando de o codigo dela existe e alocando o professor na  disciplina
def aloc_prof_disc(codigo_disciplina, matricula_professor):
    for disciplina in disciplinas:
        if disciplina["codigo"] == codigo_disciplina:
            disciplina["professor"] = matricula_professor
            
#mesma coisa só que pra turma
def aloc_prof_tur(codigo_turma, matricula_professor):
    for turma in turmas:
        if turma["codigo"] == codigo_turma:
            turma["professor"] = matricula_professor
    
    
#mesma coisa só que pra aluno em turma
def mat_alu_tur(matricula_aluno, codigo_turma):
    for turma in turmas:
        if turma["codigo"] == codigo_turma:
            turma["alunos"].append(matricula_aluno)

