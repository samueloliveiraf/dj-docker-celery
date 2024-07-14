import random
import string

# Gerar um nome de arquivo aleatório
tamanho_nome = 10  # Tamanho do nome do arquivo
caracteres = string.ascii_letters + string.digits
nome_aleatorio = ''.join(random.choice(caracteres) for _ in range(tamanho_nome))

# Adicionar extensão .txt
nome_do_arquivo = nome_aleatorio + ".txt"

# Conteúdo que será escrito no arquivo
conteudo = "Este é um arquivo de texto criado pelo Python com nome aleatório."

# Abrir (ou criar) o arquivo em modo de escrita
with open(nome_do_arquivo, 'w') as arquivo:
    # Escrever o conteúdo no arquivo
    arquivo.write(conteudo)

print(f"Arquivo '{nome_do_arquivo}' criado com sucesso!")

