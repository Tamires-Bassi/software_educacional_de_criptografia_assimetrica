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
# Generating  p e q
# ========================================

def generate_p_q():
    # Definindo os limites para a geração dos números primos
    min_value = 10**80
    max_value = 10**96

    # Avisando que p e q estão sendo gerados, pois isso pode levar algum tempo
    label_result.configure(text = 'Gerando números primos p e q...\nIsso pode levar alguns segundos.', text_color = "yellow")
    app.update() #Força a tela a atualizar a mensagem antes de travar para calcular os números primos

    p = generate_prime_number(min_value, max_value)
    q = generate_prime_number(min_value, max_value)

    # Verificar se p e q são distintos, caso contrário gerar um novo q
    while q == p:
        q = generate_prime_number(min_value, max_value)

    # Salvando as chaves em um arquivo
    with open('RSA_P_Q.txt', 'w') as f:
        f.write(f"- P = {p} \n")
        f.write(f"- Q = {q} \n")

    # Exibindo uma mensagem de sucesso na tela para o usuário
    label_result.configure(
        text = f"P e Q geradas com suceso e salvas em 'RSA_P_Q.txt'",
        text_color="green"
    )

# ========================================
# graphical interface
# ========================================

# Só executa a interface gráfica se este arquivo for executado diretamente, e não importado por outro módulo
if __name__ == "__main__":
    # Configuração da tela (Dark Mode) e cor dos botões
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Criando janela principal
    app = ctk.CTk()
    app.geometry("1240x600")
    app.title("Geração de P e Q (RSA)")

    # Elementos visuais da interface gráfica
    title = ctk.CTkLabel(app, text = "Gerador de P e Q (RSA)", font = ("Arial", 20, "bold"))
    title.pack(pady = 30)

    instruction = ctk.CTkLabel(app, text="Clique no botão abaixo para gerar P e Q\nP e Q serão salvos em um arquivo '.txt'.", font=("Arial", 14))
    instruction.pack(pady = 5)

    # Botão que dispara a geração
    generate_button = ctk.CTkButton(app, text = "Gerar P e Q", command = generate_p_q)
    generate_button.pack(pady = 15)

    # Label para exibir o resultado ou carregamento
    label_result = ctk.CTkLabel(app, text = "", font = ("Arial", 14))
    label_result.pack(pady = 10)

    # Mantém a janela rodando
    app.mainloop()