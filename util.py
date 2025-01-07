from aluno import cad_aluno
disciplinas = []
turmas = []

def cad_disciplina(nome, codigo, carga_horaria):
    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": None
    }
    disciplinas.append(disciplina)
    
def listar_disciplinas():
    return disciplinas

def cad_turma(nome, codigo, codigo_disciplina):
    turma = {
        "nome": nome,
        "codigo": codigo,
        "codigo_disciplina": codigo_disciplina,
        "professor": None,
        "alunos": []
    }
    turmas.append(turma)
    
def listar_turmas():
    return turmas

def aloc_prof_disc(codigo_disciplina, matricula_professor):
    for disciplina in disciplinas:
        if disciplina["codigo"] == codigo_disciplina:
            disciplina["professor"] = matricula_professor
            
def aloc_prof_tur(codigo_turma, matricula_professor):
    for turma in turmas:
        if turma["codigo"] == codigo_turma:
            turma["professor"] = matricula_professor
    
    
def mat_alu_tur(matricula_aluno, codigo_turma):
    for turma in turmas:
        if turma["codigo"] == codigo_turma:
            turma["alunos"].append(matricula_aluno)

