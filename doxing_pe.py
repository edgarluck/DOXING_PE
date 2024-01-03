import os
import subprocess
import urllib.request
import time
import requests
import socket
import telegram
import asyncio
import hashlib


# Calcular el hash del archivo original
with open('hash_comprobar.py', 'rb') as f:
    original_hash = hashlib.sha256(f.read()).hexdigest()

# Calcular el hash del archivo en ejecución
with open(__file__, 'rb') as f:
    current_hash = hashlib.sha256(f.read()).hexdigest()

# Comparar los hashes y tomar acción si son diferentes
if original_hash != current_hash:
    print("¡El archivo ha sido modificado!")
    exit()

def clear_screen():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_updates():
    """Comprueba si hay actualizaciones disponibles."""
    clear_screen()
    print("[+] Comprobando actualizaciones ...")
    time.sleep(0.5)
    print("[+] Comprobando actualizaciones ...")
    time.sleep(0.5)
    if os.path.isfile("version.txt"):
        os.remove("version.txt")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/version.txt", "version.txt")
    time.sleep(0.5)
    clear_screen()
    version = open("version.txt").read().strip()
    current_version = "1.1.18"
    if version == current_version:
        print("[+] La API está actualizada.")
        time.sleep(1)
        return
    else:
        print(f"[+] Nueva versión disponible: {version}")
        time.sleep(0.5)
        print("[+] Actualizando ...")
        time.sleep(0.5)
        update()

def update():
    """Actualiza el repositorio y ejecuta el script actualizado."""
    clear_screen()
    print(f"[+] Descargando cambios ...")
    time.sleep(0.5)
    subprocess.run("cd $HOME && rm -rf DOXING_PE && git clone https://github.com/edgarluck/DOXING_PE && cd DOXING_PE", shell=True)
    clear_screen()
    print("[+] Los cambios se han descargado correctamente.")
    time.sleep(0.5)
    print("[+] Pulsa cualquier tecla para continuar...")
    input()
    subprocess.run("cd $HOME && cd DOXING_PE && chmod +x doxing_pe.py && python doxing_pe.py", shell=True)
    

def check_ip_blocked():
    """Comprueba si la IP del host está bloqueada."""
    blocked_ips = requests.get('https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/blocked_ips.txt').text.splitlines()
    #hostname = socket.gethostname()
    #ip_address = socket.gethostbyname(hostname)
    ip_address = requests.get('https://api.ipify.org').text
    if ip_address not in blocked_ips:
        print("[+] La IP no está bloqueada en el servidor.")
        asyncio.run(send_notification(f"La IP {ip_address} no está bloqueada."))
        return False
    print("[-] La IP está bloqueada.")
    #send_notification(f"La IP {ip_address} está bloqueada.")
    return True

async def send_notification(message):
    """Envía una notificación a Telegram con el mensaje especificado."""
    bot_token = '5912880474:AAHmWnir1DrjBoyxGgy0hQWRdWyPFPcXVEs'
    chat_id = '1373934283'
    bot = telegram.Bot(bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
    

def doxing():
    if check_ip_blocked():
        #send_notification(f"La IP {ip_address} está bloqueada.")
        return

    username = input("Digite su usuario: ")
    password = input("Digite su contraseña: ")

    url = 'https://e764-190-237-172-226.ngrok-free.app/login'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    token = response.json().get('access_token')
    if 'access_token' in response.json():
        token = response.json().get('access_token')
        print(f"Token de acceso: {token}")
    else:
        message = response.json().get('message')
        print(f"Error: {message}")
    time.sleep(2)

    dni = input("Digite su dni: ")
    print("\n")
    url = f'https://e764-190-237-172-226.ngrok-free.app/data/{dni}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    data = response.json()

    # Ordenar los campos alfabéticamente
    data_ordenado = dict(sorted(data.items()))

    # Imprimir los resultados ordenados
    for campo, valor in data_ordenado.items():
        print(f"{campo}: {valor}")
    print("\n")   
    input("Presione enter para salir\n")

def main():
    """Función principal que comprueba las actualizaciones y las aplica si es necesario."""
    clear_screen()
    check_updates()
    doxing()

if __name__ == '__main__':
    main()
