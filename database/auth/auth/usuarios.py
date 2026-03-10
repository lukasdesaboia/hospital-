import bcrypt
from database.connection import conectar


def registrar_usuario():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios VALUES (NULL, ?, ?)",
            (usuario, senha_hash)
        )
        conn.commit()
        print("Usuário registrado!")
    except:
        print("Usuário já existe")

    conn.close()


def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT senha FROM usuarios WHERE usuario=?",
        (usuario,)
    )

    resultado = cursor.fetchone()

    if resultado and bcrypt.checkpw(senha.encode(), resultado[0]):
        print("Login realizado!")
        return True

    print("Login inválido")
    return False
