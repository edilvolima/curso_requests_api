import requests
import os

class DeletaRepositorios():
    
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.environ.get('REQUESTS_TOKEN')
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
        
    def deleta_repo(self, repo):
        url = f'{self.api_base_url}/repos/{self.owner}/{repo}'
        response = requests.delete(url, headers=self.headers)
        print(f'deletando repositorio: {repo}, status_code: {response.status_code}')
        
        
# Instancia repo
meu_repo = DeletaRepositorios('edilvolima')

meu_repo.deleta_repo('linguagens-utilizadas')
meu_repo.deleta_repo('linguagem-repositorio-empresas')