import hashlib

import base64

import urllib.request

# Função para decodificar os dados descriptografados usando base64

def decodificar_dados(dados_descriptografados):

    return base64.b64decode(dados_descriptografados).decode("utf-8")

# Solicita que o usuário insira a hash criptografada

hash_criptografada = input("Insira a hash criptografada: ")

# Identifica a criptografia usada na hash

if len(hash_criptografada) == 32:

    criptografia = "md5"

elif len(hash_criptografada) == 40:

    criptografia = "sha1"

elif len(hash_criptografada) == 64:

    criptografia = "sha256"

elif len(hash_criptografada) == 86:

    criptografia = "sha512"

else:

    print("Criptografia não reconhecida.")

    exit()

# Abre o arquivo para salvar os dados descriptografados

dados_file = open("dados.txt", "w")

# Faz o download da wordlist rockyou

urllib.request.urlretrieve("https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt", "rockyou.txt")

# Abre a wordlist rockyou

with open("rockyou.txt", "r", errors='ignore') as wordlist_file:

    # Itera sobre cada linha da wordlist

    for senha in wordlist_file:

        # Remove quebras de linha e codifica a senha em bytes

        senha = senha.strip().encode("utf-8")

        # Seleciona o módulo de descriptografia correto com base na criptografia

        if criptografia == "md5":

            hash_senha = hashlib.md5(senha).hexdigest()

        elif criptografia == "sha1":

            hash_senha = hashlib.sha1(senha).hexdigest()

        elif criptografia == "sha256":

            hash_senha = hashlib.sha256(senha).hexdigest()

        elif criptografia == "sha512":

            hash_senha = hashlib.sha512(senha).hexdigest()

        # Verifica se a hash da senha atual corresponde à hash criptografada

        if hash_senha == hash_criptografada:

            # Se a hash corresponder, a senha foi encontrada

            print("Senha encontrada: " + senha.decode("utf-8"))

            # Decodifica os dados descriptografados usando base64 e salva no arquivo de saída

            dados_file.write("Dados descriptografados: " + decodificar_dados("eHB5VmJhR3B3RWw4VmtjMldOM0RmVWlPbmxJcVlXVT0=") + "\n")

            # Termina o loop

            break

    else:

        # Se a hash da senha não corresponder a nenhuma da wordlist

        print("Senha não encontrada na wordlist.")

# Fecha o arquivo de saída

dados_file.close()
