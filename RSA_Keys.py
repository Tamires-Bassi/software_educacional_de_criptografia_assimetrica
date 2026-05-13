import math # para calcular o mdc e o inverso multiplicativo
import random # para gerar múmeros aleatórios
import customtkinter as ctk

# ========================================
# Generating prime numbers
# ========================================

# função auxiliar para verificar se um número é primo (Algoritmo de Miller-Rabin)
def is_prime(n, k = 5):
    # Números menores ou iguais a 1 não são primos
    if n <= 1:
        return False

    # Os números 2 e 3 são primos verdadeiros
    if n <= 3:
        return True
    
    # O número 4 é composto, pois é divisível por 2. Rejeitar o número 4 explicitamente para evitar confusão, já que é um caso especial.
    if n == 4:
        return False
    
    # Rejeitar números pares maiores que 2
    if n % 2 == 0:
        return False
    
    # Fatorar as poteências de 2
    # Encontrar um número 'd' umpar tal que n - 1 = d * 2^r
    d = n - 1
    r = 0

    while d % 2 == 0:
        d //= 2 # Divisão inteira por 2
        r += 1 #Contar quantas vezes a divisão por 2 foi feita

    # teste de Primalidade
    # O loop repete 'k' vezes para garantir a pecisão do teste. Quanto maior o 'k', maior a certeza de que o  número é primo
    for _ in range(k):
        # escolhe uma base 'a' aleatória entre 2 e n - 2
        a = random.randint(2, n - 2)
        # Faz a exponenciação modular
        x = pow(a, d, n)
        # Se x for 1 ou (n - 1), o npumero passou nessa rodade do teste. Vamos para o próximo 'k'
        if x == 1 or x == n - 1:
            continue

        # Elevar ao quadrado consecutivamente
        for _ in range(r - 1):
            x = pow(x, 2, n)

            # Se x atingir n - 1, o teste passou e interrompe este loop interno
            if x == n - 1:
                break

        else:
            # Se x nunca atingiu n - 1, o número é composto
            return False
    
    # Se o número sobreviveu a todas as 'k' rodadas de testes, ele é considerado primo
    return True

# Função para gerar um número primo aleatório
def generate_prime_number(min_value, max_value):

    while True:
        # Gerar um número aleatório dentro de um limite especifico
        num = random.randint(min_value, max_value)

        # Garantir que o número seja ímpar, pois números pares maiores que 2 não são primos
        if num % 2 == 0:
            num += 1

        #Verificar se o número é primo
        if is_prime(num):
            return num

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
    # Avisando que p e q estão sendo gerados, pois isso pode levar algum tempo
    label_result.configure(text = 'Gerando números primos p e q...\nIsso pode levar alguns segundos.', text_color = "yellow")
    app.update() #Força a tela a atualizar a mensagem antes de travar para calcular os números primos

    # Definindo os limites para a geração dos números primos
    min_value = 10**80
    max_value = 10**96

    # Gerar os números primos p e q
    p = generate_prime_number(min_value, max_value)
    q = generate_prime_number(min_value, max_value)

    # Verificar se p e q são distintos, caso contrário gerar um novo q
    while q == p:
        q = generate_prime_number(min_value, max_value)


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
        text = f"Chaves geradas com suceso e salvas em 'RSA_Keys.txt'\n\nChave publica: (e = {e},\n n = {n})\n\nChave privada: (d = {d},\n n = {n})", 
        text_color="green"
    )

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