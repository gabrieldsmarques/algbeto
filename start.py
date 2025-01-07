'''
- Crie um sistema escolar que permita cadastrar alunos, professores, disciplinas e turmas.
- Alunos: nome, matrícula, data de nascimento, sexo, endereço, telefone, email.
- Professores: nome, matrícula, data de nascimento, sexo, endereço, telefone, email, disciplina.
- Disciplinas: nome, código (a1234), carga horária, professor.
- Turmas: nome, código (a1234), disciplina, professor, alunos (lista-matrícula).

- O sistema deve permitir a filtragem de professores por disciplina.
- O sitema deve permitir a matrícula de alunos em turmas.
- O sistema deve permitir a alocação de professores em disciplinas
- O sistema deve permitir a alocação de disciplinas em turmas.
- O sistema deve permitir a consulta de alunos matriculados em turmas.
- O sistema deve permitir a consulta de professores alocados em disciplinas.
- O sistema deve permitir a consulta de disciplinas alocadas em turmas.

exemplo

nome = beto
matricula = 123456-A
data_nascimento = 12/12/1990
sexo = M
endereco = rua 1
telefone = 123456
email = beto@ifms.edu.br

nome = algoritmos
codigo = A1234
carga_horaria = 80
professor = beto

'''

from aluno import cad_aluno, listar_alunos
from professor import cad_professor, listar_professores
from util import (
    cad_disciplina,
    listar_disciplinas,
    cad_turma,
    listar_turmas,
    aloc_prof_disc,
    aloc_prof_tur,
    mat_alu_tur
)

def menu():
    print("\n--- Sistema Escolar ---")
    print("1. Cadastrar aluno")
    print("2. Cadastrar professor")
    print("3. Cadastrar disciplina")
    print("4. Cadastrar turma")
    print("5. Alocar professor em disciplina")
    print("6. Alocar professor em turma")
    print("7. Matricular aluno em turma")
    print("8. Listar alunos")
    print("9. Listar professores")
    print("10. Listar disciplinas")
    print("11. Listar turmas")
    print("0. Sair")


while True:
    menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        matricula = input("Matricula: ")
        data_nascimento = input("Data de nascimento (DD-MM-AAAA): ")
        sexo = input("Sexo: ")
        endereco = input("Endereco: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        cad_aluno(nome, matricula, data_nascimento, sexo, endereco, telefone, email)
        print("Aluno cadastrado com sucesso!")
        
    elif opcao == "2":
        nome = input("Nome: ")
        matricula = input("Matricula: ")
        data_nascimento = input("Data de nascimento (DD-MM-AAAA): ")
        sexo = input("Sexo: ")
        endereco = input("Endereco: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        cad_professor(nome, matricula, data_nascimento, sexo, endereco, telefone, email)
        print("Professor cadastrado com sucesso!")
        
    elif opcao == "3": 
        nome = input("Nome da disciplina: ")
        codigo = input("Codigo: ")
        carga_horaria = int(input("Carga horaria: "))
        cad_disciplina(nome, codigo, carga_horaria)
        print("Disciplina cadastrada com sucesso!")
    elif opcao == "4":
        nome = input("Nome da turma: ")
        codigo = input("Codigo: ")
        codigo_disciplina = input("Codigo da disciplina: ")
        cad_turma(nome, codigo, codigo_disciplina)
        print("Turma cadastrada com sucesso!")
        
    elif opcao == "5":
        codigo_disciplina = input("Codigo da disciplina: ")
        matricula_professor = input("Matricula do professor: ")
        aloc_prof_disc(codigo_disciplina, matricula_professor)
        print("Professor alocado na disciplina com sucesso!")
        
    elif opcao == "6":
        codigo_turma = input("Codigo da turma: ")
        matricula_professor = input("Matricula do professor: ")
        aloc_prof_tur(codigo_turma, matricula_professor)
        print("Professor alocado na turma com sucesso!")
        
    elif opcao == "7":
        codigo_turma = input("Codigo da turma: ")
        matricula_aluno = input("Matricula do aluno: ")
        mat_alu_tur(codigo_turma, matricula_aluno)
        print("Aluno matriculado na turma com sucesso!")
        
    elif opcao == "8":
        alunos = listar_alunos()
        if alunos:
            print("Alunos cadastrados:")
            for aluno in alunos:
                print(f"Nome: {aluno['nome']}, Matricula: {aluno['matricula']}")
        else:
            print("Nenhum aluno cadastrado.")
            
    elif opcao == "9":
        professores = listar_professores()
        if professores:
            print("Professores cadastrados:")
            for professor in professores:
                print(f"Nome: {professor['nome']}, Matricula: {professor['matricula']}")
        else:
            print("Nenhum professor cadastrado.")
            
    elif opcao == "10":
        disciplinas = listar_disciplinas()
        if disciplinas:
            print("Disciplinas cadastradas:")
            for disciplina in disciplinas:
                print(f"Nome: {disciplina['nome']}, Codigo: {disciplina['codigo']}")
        else:
            print("Nenhuma disciplina cadastrada.")
            
    elif opcao == "11":
        turmas = listar_turmas()
        if turmas:
            print("Turmas cadastradas:")
            for turma in turmas:
                print(f"Nome: {turma['nome']}, Codigo: {turma['codigo']}")
        else:
            print("Nenhuma turma cadastrada.")
            
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opcao invalida, tente novamente.")
