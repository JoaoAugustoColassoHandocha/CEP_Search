'''
Update main.py
Library for installation: pip install requests

API used for the query: https://viacep.com.br/

'''

import requests, os

os.system('cls' if os.name == 'nt' else 'clear')

try:
    
    print('\nConsulta CEP\n\n\n')
    
    cep = str(input('CEP: '))
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    data = requests.get(url).json()
    
    print(f'Endereço: {data["logradouro"]} - {data["bairro"]} - {data["localidade"]}/{data["uf"]}')
    
    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')

except Exception as error:
    
    print(f'\nErro: {error}\n')
    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')