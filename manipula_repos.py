import requests
import base64
import os



class ManupulaRepositorios:
    
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.environ.get('REQUESTS_TOKEN')
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    
    def cria_repo(self, nome_repo):
        data = {
            'name': nome_repo,
            'description': 'Dados dos repositórios de algumas empresas',
            'private': False
        }
                
        response = requests.post(f'{self.api_base_url}/user/repos',
                                 headers=self.headers, json=data)
        
        print(f'status_code: {response.status_code},  criação do repositório: {nome_repo}')
    
    
    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        
        # Codificando o arquivo
        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)
        
        # Realizando o upload
        url = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'
        data = {
            'message': 'Adicionando um novo arquivo',
            'content': encoded_content.decode('utf-8')
        }
        
        response = requests.put(url, headers=self.headers, json=data)
        print(f'status_code: {response.status_code}, upload do arquivo: {nome_arquivo}')
        
# Instanciando um objeto
novo_repo = ManupulaRepositorios('edilvolima')

# Criando repositorio
nome_repo = 'linguagem-repositorio-empresas'
novo_repo.cria_repo(nome_repo)

# Adicionando arquivo 
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagem_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagem_spotify.csv', 'dados/linguagens_spotify.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_apple.csv', 'dados/linguagens_apple.csv')

