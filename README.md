# 🔐 Software Educacional RSA - P1 de Segurança da Informação

Este projeto é uma implementação autoral de um software educacional de criptografia assimétrica baseado no algoritmo RSA. O sistema foi desenvolvido para a disciplina de Segurança da Informação, cumprindo o requisito de execução modular e isolada.

## 👥 Equipe e Divisão de Tarefas
*   **Tamires de Sousa Bassi (RA): 2840482523039** Responsável por todo o projeto.

## 🎯 Objetivo e Arquitetura
O sistema atende à exigência estrita de que **os módulos devem ser executados separadamente**. Por isso, o software foi dividido em três executáveis independentes que se comunicam exclusivamente via arquivos de texto:

1. **Gerador de Chaves (`RSA_Keys.py`):** Gera números primos grandes (entre 10^80 e 10^96), valida a primalidade e cria os pares de chaves pública `(e, n)` e privada `(d, n)`, salvando-os no arquivo `RSA_Keys.txt`.
2. **Módulo A - Criptografar (`Cryptography.py`):** Recebe o texto claro do usuário, lê a chave pública do arquivo, converte a mensagem seguindo o padrão **UTF-8** usando inteiros grandes e exporta a cifra para o arquivo `Encrypted_Message.rsa`.
3. **Módulo B - Decifrar (`Decryption.py`):** Lê a mensagem cifrada e a chave privada dos arquivos gerados, realiza a operação matemática de descriptografia e devolve o texto claro legível na tela.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
De acordo com os requisitos técnicos, o uso de implementações RSA prontas foi evitado. Toda a matemática modular e lógica de criptografia foi construída do zero.

**Bibliotecas não-RSA utilizadas (e justificativas):**
*   `customtkinter`: Framework livre utilizado para criar a interface gráfica de usuário (GUI) independente para cada módulo.
*   `random`: Utilizada para gerar os números aleatórios e as bases na validação de primalidade.
*   `math`: Utilizada nativamente para o cálculo de Máximo Divisor Comum (MDC) durante a verificação do número de Euler e da chave pública.

**Algoritmos Matemáticos Adicionais:**
*   Para cumprir a exigência de utilizar **inteiros grandes** sem causar travamento de processamento, implementei o **Algoritmo de Miller-Rabin** para a validação rápida da primalidade de `p` e `q` gerados aleatoriamente.

## 🚀 Como Executar o Software

**Pré-requisitos:**
Certifique-se de ter o Python instalado. Abra o terminal e instale a biblioteca gráfica executando o comando:
> `pip install customtkinter`

**Passo a passo da execução:**
*Para garantir a integridade da regra de módulos separados, não criei um menu unificado. Execute os arquivos na seguinte ordem:*

1. Execute o `RSA_Keys.py`. Clique no botão para gerar as chaves e aguarde a mensagem de sucesso. Feche a janela.
2. Execute o `Cryptography.py`. Digite a mensagem desejada na caixa de texto e clique em Criptografar. O arquivo `.rsa` será gerado. Feche a janela.
3. Execute o `Decryption.py`. Clique no botão de decifrar para visualizar a mensagem original recuperada matematicamente.

## 📚 Referências
*   Documentação Oficial do Python: https://docs.python.org/3/
*   Documentação do CustomTkinter: https://customtkinter.tomschimansky.com/
*   Artigos sobre o Algoritmo de Miller-Rabin: https://gist.github.com/Ayrx/5884790
*   Video sobre o Algoritmo RSA: https://www.youtube.com/watch?v=yqo3Xa06tZc&t=82s