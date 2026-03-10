from database.connection import conectar

def consultas_por_medico():

    crm = input("CRM do médico: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT consultas.data, pacientes.nome
    FROM consultas
    JOIN pacientes ON consultas.cpf_paciente = pacientes.cpf
    WHERE crm_medico=?
    """, (crm,))

    resultados = cursor.fetchall()

    for r in resultados:
        print(f"{r[0]} - Paciente: {r[1]}")

    conn.close()
#
def historico_paciente():

    cpf = input("CPF do paciente: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT data, descricao
    FROM prontuarios
    WHERE cpf_paciente=?
    """, (cpf,))

    registros = cursor.fetchall()

    for r in registros:
        print(f"{r[0]} - {r[1]}")

    conn.close()
