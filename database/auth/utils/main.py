from database.connection import criar_tabelas
from auth.usuarios import login, registrar_usuario
from utils.menu import menu


def main():

    criar_tabelas()

    registrar_usuario()

    if login():
        menu()


if __name__ == "__main__":
    main()
