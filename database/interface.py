import tkinter as tk
from models.pacientes import cadastrar_paciente


def iniciar_interface():

    janela = tk.Tk()
    janela.title("Sistema Hospitalar")

    label = tk.Label(janela, text="Sistema Hospitalar")
    label.pack()

    btn = tk.Button(janela, text="Cadastrar Paciente", command=cadastrar_paciente)
    btn.pack()

    janela.mainloop()
  #
  from interface import iniciar_interface

iniciar_interface()
