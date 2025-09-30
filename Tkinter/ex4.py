import tkinter as tk

window = tk.Tk();
window.geometry("300x200");
window.title('Exercício 4');

title = tk.Label(window, text="Olá, Tkinter");
title.pack();

entry = tk.Entry(window);
entry.pack();

def aps():
    entry_value = entry.get();
    print(entry_value);

button = tk.Button(window, text="Clique Aqui", command=aps);
button.pack();

window.mainloop();
