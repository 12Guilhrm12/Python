import tkinter as tk

window = tk.Tk();
window.geometry("300x200");
window.title('Exercício 7');

def red():
    window.config(bg="red")
def blue():
    window.config(bg="blue")
def green():
   window.config(bg="green")

# title = tk.Label(window, text="Olá, Tkinter");
# title.pack();

button = tk.Button(window, text="Azul", command=blue);
button.pack();
button1 = tk.Button(window, text="Vermelho", command=red);
button1.pack();
button2 = tk.Button(window, text="Verde", command=green);
button2.pack();

window.mainloop();