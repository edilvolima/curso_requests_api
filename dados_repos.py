import requests
import pandas as pd
import os

class DadosRepositorios:
    
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.environ.get('REQUESTS_TOKEN')
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
        
    def lista_repositorios(self):
        repos_list = []
        
        page_num = 1
        while True:
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos = response.json()

                if len(repos) == 0:
                    break
                
                repos_list.append(repos)
                page_num +=1
            except Exception as err:
                repos_list.append(None)
                print(err)

        return repos_list
        
        
    def nomes_repos(self, repositorios):
        
        repos_name = []

        for page in repositorios:
            for repo in page:
                repos_name.append(repo['name'])
        
        return repos_name
    
    
    def nomes_linguagens(self, repositorios):   
        
        repos_language = []

        for page in repositorios:
            for repo in page:
                repos_language.append(repo['language'])
                
        return repos_language
    
    
    def cria_df_linguagens(self):
        
        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)
        
        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens
        
        return dados
    
    
# Criando os dataframes de cada owner
amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()
#print(ling_mais_usadas_amzn)

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

apple_rep = DadosRepositorios('apple')
ling_mais_usadas_apple = apple_rep.cria_df_linguagens()

# Salvando os dados
ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv')
ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')
ling_mais_usadas_apple.to_csv('dados/linguagens_apple.csv')
