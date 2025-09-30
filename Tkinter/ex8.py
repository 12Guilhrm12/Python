import tkinter as tk
from tkinter import messagebox

window = tk.Tk();
window.geometry("300x200");
window.title('Exercício 8');

def aps():
    messagebox.showinfo(message="Você clicou no botão");

title = tk.Label(window, text="Olá, Tkinter");
title.pack();

button = tk.Button(window, text="Clique Aqui", command=aps);
button.pack();

window.mainloop();