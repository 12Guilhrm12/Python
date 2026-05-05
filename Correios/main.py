# Libs
import tkinter as tk;
from tkinter import ttk;

from tkinter import messagebox;

screen = 0; 
# Estudando na internet (stack overflow)
# Vi uma forma de fazer FRAMES, telas diferentes,
# Usando OBJETOS. Para cada Tela, usamos objetos diferentes
# E no final indicamos qual queremos usar

# Função para limpar a tela
# Se não fizermos isso
# O frame anterior continua desenhado
def clearFrame():
    # Puxa o Frame

    # Pega todas os frames e deleta tudo
    for widget in frame.winfo_children():
        widget.destroy(); 
    
    # Da uma limpada no frame
    frame.pack_forget()

# Função que atualiza a tela
# Cada vez que é necessário.
# Limpa, e desenha a correspondente
def update_frame():
    global frame, screen

    clearFrame()  # Limpeza

    if screen == 0:
        frame = Menu(app)
    else:
        frame = Entregas(app)

    # Desenha
    frame.pack(fill="both", expand=True)

# Tela do Menu
class Menu(ttk.Frame):
    # Constructor 
    # Define a estrutura 
    # Do MENU
    def __init__(self, container):
        super().__init__(container); 
        
        self.title = ttk.Label(self, text='Correios', background='yellow', foreground='blue', font=('Busso', 36, 'bold')); 
        self.title.grid(row=0, column=0, padx=(250, 0), pady=(110, 0)); 

        # Login Section

        self.user_text = ttk.Label(self, text='User: '); 
        self.user_text.grid(row=2, column=0, pady=(50, 0), padx=(100, 0)); 

        self.login_entry = ttk.Entry(self); 
        self.login_entry.grid(row=2, column=0, pady=(50, 0), padx=(325, 0)); 

        self.pass_text = ttk.Label(self, text='Password: '); 
        self.pass_text.grid(row=3, column=0, pady=(12, 0), padx=(100, 0)); 

        self.pass_entry = ttk.Entry(self); 
        self.pass_entry.grid(row=3, column=0, pady=(12, 0), padx=(325, 0)); 

        self.button = ttk.Button(self, text='Login', command=self.login); 
        self.button.grid(row=4, column=0, pady=(12, 0), padx=(312, 0)); 
    
    # Função para fazer o Login
    def login(self):
        global screen;

        password = self.pass_entry.get(); 
        user = self.login_entry.get(); 

        if (password == 'correios12') and (user == 'Justin'):
            messagebox.showinfo(title='Correios', message='Sejá bem-vindo!'); 
            screen = 1; 
            update_frame(); 
        else:
            messagebox.showerror(title='Erro!', message='Usúario ou Senha incorretos!'); 

# Tela das Entregas
class Entregas(ttk.Frame):
    def __init__(self, container):
        super().__init__(container); 
        
        self.title = ttk.Label(self, text='Entregas', background='yellow', foreground='blue', font=('Busso', 36, 'bold')); 
        self.title.grid(row=0, column=0, padx=(250, 0), pady=(110, 0)); 

class App(tk.Tk):
    def __init__(self):
        super().__init__(); 
        self.title('Correios'); 
        self.geometry('720x460'); 

# Main Guard
if __name__ == "__main__":
    app = App(); 
    if (screen==0):
        frame = Menu(app); 
    else:
        frame = Entregas(app); 
    update_frame()
    app.mainloop(); 