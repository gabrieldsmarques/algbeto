professores = []

def cad_professor(nome, matricula, data_nascimento, sexo, endereco, telefone, email):
    professor = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
    }
    professores.append(professor)
    
def listar_professores():
    return professores