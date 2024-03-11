import os
import shutil
import subprocess
from git import Repo
import requests

VERSION = "1.1.27"
REPO_URL = "https://github.com/edgarluck/DOXING_PE.git"
TARGET_DIRECTORY = "DOXING_PE"


def download_update(repo_url, target_directory):
    # Clonar el repositorio
    Repo.clone_from(repo_url, target_directory)
    print("Actualización descargada correctamente.")

def install_update(target_directory):
    # Ejecutar el programa Python después de la actualización
    os.chdir(target_directory)
    subprocess.call(["python", "doxing_pe.py"])
    print("Programa ejecutado después de la actualización.")

def update_application(repo_url, target_directory):
    if os.path.exists(target_directory):
        shutil.rmtree(target_directory)
    download_update(repo_url, target_directory)
    install_update(target_directory)

def check_for_update():
    response = requests.get("https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/latest_version.txt")
    latest_version = response.text.strip()
    if latest_version != VERSION:
        return True
    else:
        return False

def main():
    if check_for_update():
        update_application(REPO_URL, TARGET_DIRECTORY)
        return

    opcion = menu()
    while opcion != '3':
        if opcion == '1':
            dni = input("Ingrese el DNI a buscar: ")
            consultar_dni(dni)
        elif opcion == '2':
            nombres = input("Ingrese los nombres a buscar: ")
            apellido_paterno = input("Ingrese el apellido paterno: ")
            apellido_materno = input("Ingrese el apellido materno: ")
            consultar_nombres(nombres, apellido_paterno, apellido_materno)
        else:
            print("Opción inválida")
        opcion = menu()

def menu():
    print("Seleccione una opción:")
    print("1. Consultar por DNI")
    print("2. Consultar por Nombres")
    print("3. Salir")
    opcion = input("Opción: ")
    return opcion

def consultar_dni(dni):
    response = requests.get(f'https://628b-132-184-131-222.ngrok-free.app/api/personas?dni={dni}')
    if response.status_code == 200:
        print(response.text)
    else:
        print("Error:", response.text)

def consultar_nombres(nombres, apellido_paterno, apellido_materno):
    response = requests.get(f'https://628b-132-184-131-222.ngrok-free.app/api/personas?nombres={nombres}&apellidoPaterno={apellido_paterno}&apellidoMaterno={apellido_materno}')
    if response.status_code == 200:
        print(response.text)
    else:
        print("Error:", response.text)

if __name__ == '__main__':
    main()


