import tkinter as tk

window = tk.Tk();
window.geometry("300x200");
window.title('Exercício 10');

title = tk.Label(window, text="Calculadora +");
title.grid();

sum1 = tk.Entry(window);
sum1.grid(row=2, column=0);
sum2 = tk.Entry(window);
sum2.grid(row=2, column=1);

def somar():
    s1 = int(sum1.get());
    s2 = int(sum2.get());
    s3 = s1 + s2;
    title.config(text=f"{s3}")

button = tk.Button(window, text="Clique Aqui", command=somar);
button.grid();

window.mainloop();