#estrutura pra armazenar dados
alunos = []

#cadastro do aluno
def cad_aluno(nome, matricula, data_nascimento, sexo, endereco, telefone, email):
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
    }
    alunos.append(aluno)
    return "Aluno cadastrado com sucesso!"

def listar_alunos():
    return alunos

