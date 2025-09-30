import tkinter as tk

window = tk.Tk();
window.geometry("300x200");
window.title('Exercício 2');

title = tk.Label(window, text="Olá, Tkinter");
title.pack();

window.mainloop();
