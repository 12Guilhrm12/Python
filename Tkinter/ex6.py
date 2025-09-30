import tkinter as tk

window = tk.Tk();
window.geometry("300x200");
window.title('Exercício 6');

cliques = 0;

title = tk.Label(window, text=f"Cliques: {cliques}");
title.pack();

# entry = tk.Entry(window);
# entry.pack();

def aps():
    global cliques
    cliques += 1;
    title.config(text=f"Cliques: {cliques}")

button = tk.Button(window, text="Clique Aqui", command=aps);
button.pack();

window.mainloop();
