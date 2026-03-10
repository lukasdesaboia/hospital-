import sqlite3

def conectar():
    return sqlite3.connect("hospital.db")


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        senha TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        cpf TEXT PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicos (
        crm TEXT PRIMARY KEY,
        nome TEXT,
        especialidade TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf_paciente TEXT,
        crm_medico TEXT,
        data TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prontuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf_paciente TEXT,
        data TEXT,
        descricao TEXT
    )
    """)

    conn.commit()
    conn.close()
