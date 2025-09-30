import tkinter as tk
from tkinter import messagebox

window = tk.Tk();
window.geometry("300x200");
window.title('Exercício 9');

title = tk.Label(window, text="Olá, Tkinter");
title.pack();

title = tk.Label(window, text="User");
title.pack();

login = tk.Entry(window);
login.pack();

title = tk.Label(window, text="Password");
title.pack();

password = tk.Entry(window);
password.pack();


def aps():
    password_value = password.get();
    user_value = login.get();
    if (password_value == "1234") and (user_value == "admin"):
        messagebox.showinfo(message="Login bem-sucedido")
    else:
        messagebox.showerror(message="Usuário ou Senha inválidos")

button = tk.Button(window, text="Clique Aqui", command=aps);
button.pack();

window.mainloop();
