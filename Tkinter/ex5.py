import tkinter as tk

window = tk.Tk();
window.geometry("300x200");
window.title('Exercício 5');

title = tk.Label(window, text="Olá, Tkinter");
title.pack();

# entry = tk.Entry(window);
# entry.pack();

def aps():
    title.config(text="Texto alterado")

button = tk.Button(window, text="Clique Aqui", command=aps);
button.pack();

window.mainloop();
