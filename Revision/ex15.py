try:
    with open("meu_arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read(); 
        print(conteudo); 
except FileNotFoundError:
    print("O arquivo não foi encontrado."); 
except Exception as e:
    print(f"Ocorreu um erro: {e}") [5]; 