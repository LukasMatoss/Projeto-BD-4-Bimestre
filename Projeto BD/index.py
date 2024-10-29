from pymongo import MongoClient
import hashlib

#Conectando ao mongo DB
uri = "mongodb+srv://gluiz6128:123@cluster0.u5pyu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)

db = client ['meu_banco']
colecao = db ['usuarios']

def gerar_hash(valor):
    #Usando SHA-256
    hash_obj = hashlib.sha256 (valor.encode())
    return hash_obj.hexdigest()


# Armazenando usurio e hash da senha
def armazenar_usuario (usuario, hash_numero_cartao, hash_CVV, hash_vencimento):
    colecao.insert_one({'usuario': usuario, 'numero': hash_numero_cartao, 'CVV': hash_CVV, 'vencimento': hash_vencimento})
# Exemplo de uso



def verificar_senha (usuario, senha):
    usuario_encontrado = colecao.find_one({'usuario': usuario})
    if usuario_encontrado:
        hash_senha_inserida = gerar_hash(senha)
        if usuario_encontrado ['hash_senha'] == hash_senha_inserida:
            return True
    return False

 #As criptografa antes de armazenar !!!!!!!!!
numero_cartao = (input("Digite o número do Cartão:"))
hash_numero_cartao = gerar_hash(numero_cartao)
CVV = (input("Digite o número CVV do cartão"))
hash_CVV = gerar_hash(CVV)
vencimento = (input("Digite a data de vencimento do cartão (xx/yy):"))
hash_vencimento = gerar_hash(vencimento)

print (f"hash nº Cartão: {hash_numero_cartao}")
print (f"hash CVV: {hash_CVV}")
print (f"hash vencimento: {hash_vencimento}")

armazenar_usuario ('bruno', hash_numero_cartao, hash_CVV, hash_vencimento) #armazenando os dados do usuario
