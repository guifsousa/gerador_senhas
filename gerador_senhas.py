import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Informe um tamanho válido para a senha.")
        return

    caracteres = ""

    if var_maiusculas.get():
        caracteres += string.ascii_uppercase
    if var_minusculas.get():
        caracteres += string.ascii_lowercase
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showwarning("Aviso", "Selecione pelo menos um tipo de caractere.")
        return

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)

def copiar_senha():
    senha = entry_resultado.get()
    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência.")

# Janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("350x320")
janela.resizable(False, False)

# Tamanho da senha
tk.Label(janela, text="Tamanho da senha:").pack(pady=5)
entry_tamanho = tk.Entry(janela, justify="center")
entry_tamanho.pack()

# Opções
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)

tk.Checkbutton(janela, text="Letras maiúsculas (A-Z)", variable=var_maiusculas).pack(anchor="w", padx=40)
tk.Checkbutton(janela, text="Letras minúsculas (a-z)", variable=var_minusculas).pack(anchor="w", padx=40)
tk.Checkbutton(janela, text="Números (0-9)", variable=var_numeros).pack(anchor="w", padx=40)
tk.Checkbutton(janela, text="Símbolos (!@#$)", variable=var_simbolos).pack(anchor="w", padx=40)

# Botão gerar
tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)

# Resultado
entry_resultado = tk.Entry(janela, width=30, justify="center")
entry_resultado.pack(pady=5)

# Botão copiar
tk.Button(janela, text="Copiar Senha", command=copiar_senha).pack()

# Loop principal
janela.mainloop()