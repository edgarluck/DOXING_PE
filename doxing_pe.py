import os
import subprocess
import urllib.request
import time
import requests

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
    current_version = "1.1"
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
    
def doxing():
    username = input("Digite su usuario: ")
    password = input("Digite su contraseña: ")

    url = 'https://82b3-179-7-192-223.ngrok-free.app/login'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    token = response.json().get('access_token')

    time.sleep(2)

    dni = input("Digite su dni: ")
    print("\n")
    url = f'https://82b3-179-7-192-223.ngrok-free.app/data/{dni}'
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
