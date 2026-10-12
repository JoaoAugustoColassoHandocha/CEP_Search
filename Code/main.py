'''
Update main.py
Library for installation: pip install requests

API used for the query: https://viacep.com.br/

'''

import requests, os

pause = input('Clique em qualquer tecla para continuar...')
clear = os.system('cls' if os.name == 'nt' else 'clear')

print('\nConsulta CEP\n\n\n')
