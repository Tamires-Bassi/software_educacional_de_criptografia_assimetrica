import customtkinter as ctk

# ========================================
# Decryption
# ========================================

def decrypt_message():
    try: 
        # Lendo a chave privada do arquivo RSA_Keys.txt
        with open('RSA_Keys.txt', 'r') as f:
            lines = f.readlines()
            d = int(lines[1].split('=') [1].split(',') [0].strip())
            n = int(lines[1].split('=')[2].replace(')', '').strip())

        # Lendo a mensagem criptografada do arquivo Encrypted_Message.rsa
        with open('Encrypted_Message.rsa', 'r') as f:
            lines = f.readlines()
            c = int(lines[0].split(':') [1].strip())

        # Muda o status da tela
        label_status.configure(text="Decifrando a mensagem... Isso pode levar alguns segundos.", text_color="yellow")
        app.update() #Força a tela a atualizar a mensagem antes de travar para calcular

        # Descriptografar a mensagem usando a chave privada
        m = pow(c, d, n)

        # Convertendo o número inteiro de volta para a mensagem original usando a codificação UTF-8
        message_decrypted = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode('utf-8')

        # Exibindo a mensagem decifrada na tela para o usuário
        label_status.configure(
            text = f"Mensagem decifrada com sucesso!",
            text_color = "green"
        )

        # Habilita a caixa de texto, insere a mensagem secreta e bloqueia de novo (somente leitura)
        label_result.configure(state = "normal") # Habilita a caixa de texto para inserir a mensagem decifrada
        label_result.delete("1.0", "end") # Limpa a caixa de texto antes de inserir a mensagem
        
        label_result.insert("1.0", message_decrypted) # Insere a mensagem decifrada
        label_result.configure(state="disabled") # Bloqueia a caixa de texto para que o usuário não possa escrever nela
    
    except FileNotFoundError:
        label_status.configure(text="ERROR: Arquivos 'RSA_Keys.txt' ou 'Encrypted_Message.rsa' não encontrados!", text_color="red")
    except Exception as e:
        # Se as chaves não baterem ou o arquivo de chaves for corrompido, exibe uma mensagem de erro para o usuário
        label_status.configure(text="Erro de autenticação: As chaves não coincidem ou arquivo foi corrompido.", text_color="red")
    

# ========================================
# graphical interface
# ========================================

# Configuração da tela (Dark Mode) e cor dos botões
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Criando janela principal
app = ctk.CTk()
app.geometry("1240x600")
app.title("Módulo B - Descriptografia (RSA)")

# Elementos visuais da interface gráfica
title = ctk.CTkLabel(app, text = "Descriptografar Mensagem com RSA", font = ("Arial", 20, "bold"))
title.pack(pady = 30)

instruction = ctk.CTkLabel(app, text="Clique no botão abaixo para descriptografar a mensagem com RSA.", font=("Arial", 14))
instruction.pack(pady = 5)

# Botão para iniciar a descriptografia
decryption_button = ctk.CTkButton(app, text = "Descriptografar mensagem", command = decrypt_message)
decryption_button.pack(pady = 15)

# Label para avisar se houve sucesso ou erro na descriptografia
label_status = ctk.CTkLabel(app, text="", font=("Arial", 14))
label_status.pack(pady=5)

# Caixa de texto estática para exibir a mensagem original recuperada
label_result = ctk.CTkTextbox(app, width = 600, height = 100)
label_result.pack(pady=10)

# Começa bloqueada para o usuário não conseguir digitar nela, afinal é só para exibir o resultado
label_result.configure(state="disabled") 

# Mantém a janela aberta e funcionando
app.mainloop()