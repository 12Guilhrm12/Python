import tkinter as tk

window = tk.Tk();
window.geometry("300x200");
window.title('Exercício 3');

def aps():
    print('Botão Pressionado!');

title = tk.Label(window, text="Olá, Tkinter");
title.pack();

button = tk.Button(window, text="Clique Aqui", command=aps);
button.pack();

window.mainloop();
