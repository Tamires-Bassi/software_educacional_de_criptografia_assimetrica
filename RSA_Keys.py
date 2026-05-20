import math # para calcular o mdc e o inverso multiplicativo
import random
import customtkinter as ctk

from P_Q import is_prime # Importando a função is_prime do arquivo P_Q.py para verificar se os números p e q são primos

# ========================================
# Generating Keys
# ========================================

# Definir o expoente público e
def generate_e(phi_n):
    while True:
        e = random.randint(2, phi_n - 1)
        #Verificar se e é coprimo com phi_n
        if math.gcd(e, phi_n) == 1:
            return e

# Função para gerar p e q e as chaves RSA
def generate_rsa_keys():
    try: 
        # Lendo p e q do arquivo RSA_P_Q.txt
        with open('RSA_P_Q.txt', 'r') as f:
            lines = f.readlines()
            p = int(lines[0].split('=')[1])
            q = int(lines[1].split('=')[1])

        # Verificando se p e q são primos, caso contrário exibe uma mensagem de erro para o usuário
        if not (is_prime(p) and is_prime(q)):
            label_result.configure(text="ERROR: Os números p e q no arquivo 'RSA_P_Q.txt' não são primos!\n\nGere novos números primos para p e q.", text_color="red")
            return
        
        # Calcular o módulo n
        n = p * q

        # Calculara função totiente de Euler
        phi_n = (p -1) * (q - 1)

        e = generate_e(phi_n)
            
        # Calcular o expoente privado d usando o inverso multiplicativo modular
        d = pow(e, -1, phi_n)

        # Salvando as chaves em um arquivo
        with open('RSA_Keys.txt', 'w') as f:
            f.write(f"- Chave publica: (e = {e}, n = {n}) \n")
            f.write(f"- Chave privada: (d = {d}, n = {n}) \n")

        # Exibindo uma mensagem de sucesso na tela para o usuário
        label_result.configure(
            text = f"Chaves geradas com suceso e salvas em 'RSA_Keys.txt'", 
            text_color="green"
        )

    except FileNotFoundError:
        label_result.configure(text="ERROR: Arquivos 'RSA_P_Q.txt' não encontrado!", text_color="red")
    except Exception as e:
        # Se o arquivo de p e q for corrompido, exibe uma mensagem de erro para o usuário
        label_result.configure(text="Erro de autenticação: O arquivo 'RSA_P_Q.txt' foi corrompido.", text_color="red")

# ========================================
# graphical interface
# ========================================

# Configuração da tela (Dark Mode) e cor dos botões
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Criando janela principal
app = ctk.CTk()
app.geometry("1240x600")
app.title("Geração de Chaves (RSA)")

# Elementos visuais da interface gráfica
title = ctk.CTkLabel(app, text = "Gerador de Chaves RSA", font = ("Arial", 20, "bold"))
title.pack(pady = 30)

instruction = ctk.CTkLabel(app, text="Clique no botão abaixo para gerar as chaves RSA\nAs chaves serão salvas em um arquivo '.txt'.", font=("Arial", 14))
instruction.pack(pady = 5)

# Botão que dispara a geração
generate_button = ctk.CTkButton(app, text = "Gerar Chaves RSA", command = generate_rsa_keys)
generate_button.pack(pady = 15)

# Label para exibir o resultado ou carregamento
label_result = ctk.CTkLabel(app, text = "", font = ("Arial", 14))
label_result.pack(pady = 10)

# Mantém a janela rodando
app.mainloop()