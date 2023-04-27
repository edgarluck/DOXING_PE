import requests
import time
import os
import git

username = input("Digite su usuario: ")
password = input("Digite su contraseña: ")

url = 'https://3259-179-7-192-223.ngrok-free.app/login'
data = {'username': username, 'password': password}
response = requests.post(url, json=data)
token = response.json().get('access_token')

time.sleep(2)

dni = input("Digite su dni: ")
print("\n")
url = f'https://3259-179-7-192-223.ngrok-free.app/data/{dni}'
headers = {'Authorization': f'Bearer {token}'}
response = requests.get(url, headers=headers)
data = response.json()

# Ordenar los campos alfabéticamente
data_ordenado = dict(sorted(data.items()))

# Imprimir los resultados ordenados
for campo, valor in data_ordenado.items():
    print(f"{campo}: {valor}")

input("\nPresione enter para salir")
