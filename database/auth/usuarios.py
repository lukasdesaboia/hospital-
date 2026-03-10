from database.connection import conectar

def registrar_usuario():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios VALUES (NULL, ?, ?)",
            (usuario, senha)
        )
        conn.commit()
        print("Usuário registrado!")
    except:
        print("Usuário já existe.")

    conn.close()


def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario=? AND senha=?",
        (usuario, senha)
    )

    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        print("Login realizado!")
        return True
    else:
        print("Login inválido")
        return False
