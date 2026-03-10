from models.pacientes import cadastrar_paciente, listar_pacientes
from models.medicos import cadastrar_medico, listar_medicos
from models.consultas import agendar_consulta, listar_consultas
from models.prontuarios import adicionar_prontuario


def menu():
    while True:
        print("""
1 - Cadastrar paciente
2 - Listar pacientes
3 - Cadastrar médico
4 - Listar médicos
5 - Agendar consulta
6 - Listar consultas
7 - Atualizar prontuário
8 - Sair
""")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_paciente()
        elif op == "2":
            listar_pacientes()
        elif op == "3":
            cadastrar_medico()
        elif op == "4":
            listar_medicos()
        elif op == "5":
            agendar_consulta()
        elif op == "6":
            listar_consultas()
        elif op == "7":
            adicionar_prontuario()
        elif op == "8":
            break
