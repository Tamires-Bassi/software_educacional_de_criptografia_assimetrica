import customtkinter as ctk

# ========================================
# Cryptography
# ========================================

def encrypt_message():
    # Receber mensagem do usuários
    message = text_box.get("1.0", "end-1c")

    # caso o usuário tente criptografar sem digitar uma mensagem
    if not message:
        label_result.configure(text = "ERROR: Por favor, digite uma mensagem primeiro!", text_color = "red" )
        return

    # Tentando criptografar a mensagem e lidar com possíveis erros
    try:
        # Lendo a chave pública do arquivo RSA_Keys.txt
        with open('RSA_Keys.txt', 'r') as f:
            lines = f.readlines()
            e = int(lines[0].split('=') [1].split(',') [0].strip())
            n = int(lines[0].split('=')[2].replace(')', '').strip())

        # Converter a mensagempara um número inteiro usando a codificação UTF-8
        message_int = int.from_bytes(message.encode('utf-8'), 'big')

        # Criptografar a mensagem
        c = pow(message_int, e, n)

        # Salvando a mensagem criptografada em um arquivo
        with open('Encrypted_Message.rsa', 'w') as f:
            f.write(str((f"Mensagem criptografada: {c}")))
        
        # Exibindo uma mensagem de sucesso na tela oara o usuário
        label_result.configure(
            text = f"Mensagem criptografada com sucesso e salva no arquivo 'Encrypted_Message.rsa'\n\nMensagem criptografada:\n\n{c}",
            text_color = "green"
        )
    except FileNotFoundError:
        label_result.configure(text = "ERROR: O arquivo 'RSA_Keys.txt' não foi encontrado!\n\nGere as chaves RSA primeiro para criptografar uma mensagem!", text_color = "red")

# ========================================
# graphical interface
# ========================================

# Configuração da tela (Dark Mode) e cor dos botões
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Criando janela principal
app = ctk.CTk()
app.geometry("1240x600")
app.title("Módulo A - Criptografia (RSA)")

# Elementos visuais da interface gráfica
title = ctk.CTkLabel(app, text = "Criptografar Mensagem com RSA", font = ("Arial", 20, "bold"))
title.pack(pady = 30)

instruction = ctk.CTkLabel(app, text="Digite a mensagem em texto claro abaixo:", font=("Arial", 14))
instruction.pack(pady = 5)

# Caixa de testo para o usuário digitar
text_box = ctk.CTkTextbox(app, width = 600, height = 100)
text_box.pack(pady = 10)

# Botão que, ao ser clicado, aciona a função encrypt_message
encrypt_button = ctk.CTkButton(app, text = "Criptografar Mensagem", command = encrypt_message)
encrypt_button.pack(pady = 10)

# Texto vazio que vai mudar de cor e texto dependendo do sucesso ou erro na criptografia
label_result = ctk.CTkLabel(app, text = "", font = ("Arial", 14))
label_result.pack(pady = 10)

# Mantém a janela aberta e funcionando
app.mainloop()
