'''
Update main.py
Library for installation: pip install requests

API used for the query: https://viacep.com.br/

'''

import requests, os

pause = input('Clique em qualquer tecla para continuar...')
clear = os.system('cls' if os.name == 'nt' else 'clear')

try:
    
    print('\nConsulta CEP\n\n\n')
    
    cep = input('CEP: ')
    url = f'viacep.com.br/ws/{cep}/json/'
    
    clear()
    
    data = requests.get(url).json
    
    print(f'Endereço: {data['logradouro']} - {data['bairro']} - {data['cidade']}/{data['uf']}')
    
    pause()
    clear()

except Exception as error:
    
    print(f'Erro: {error}')