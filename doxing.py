import requests
import os

BASE_URL = "http://apidev.ddns.net:5000"

# Función para mostrar el banner
def mostrar_banner():
    banner = """
  ____     ___   __  __  ___   _   _    ____           ____    _____ 
 |  _ \   / _ \  \ \/ / |_ _| | \ | |  / ___|         |  _ \  | ____|
 | | | | | | | |  \  /   | |  |  \| | | |  _          | |_) | |  _|  
 | |_| | | |_| |  /  \   | |  | |\  | | |_| |         |  __/  | |___ 
 |____/   \___/  /_/\_\ |___| |_| \_|  \____|  _____  |_|     |_____|
                                              |_____|    
                         ¡Bienvenido a DOXING_PE!
    """
    print(banner)

# Función para registrar un nuevo usuario
def register():
    print("\n--- Registro de Usuario ---")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    email = input("Correo electrónico: ")

    url = f"{BASE_URL}/register"
    payload = {
        'username': username,
        'password': password,
        'email': email
    }
    response = requests.post(url, json=payload)

    if response.status_code == 201:
        print("¡Usuario registrado exitosamente!")
    else:
        print(f"Error al registrar usuario: {response.json()}")

# Función para iniciar sesión y obtener el token
def login():
    print("\n--- Iniciar Sesión ---")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    url = f"{BASE_URL}/login"
    payload = {
        'username': username,
        'password': password
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("¡Iniciado sesión correctamente!")
        token = response.json()['access_token']
        print(f"Token JWT recibido: {token}")
        return token
    else:
        print(f"Error al iniciar sesión: {response.json()}")
        return None

# Función para consultar DNI
def consultar_dni(token):
    dni = input("Ingresa el número de DNI a consultar: ")
    url = f"{BASE_URL}/consulta_dni?dni={dni}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"Datos del DNI {dni}: {response.json()}")
    else:
        print(f"Error al consultar DNI: {response.json()}")

# Función para comprar créditos
def comprar_creditos(token):
    cantidad = int(input("Cantidad de créditos a comprar: "))
    url = f"{BASE_URL}/comprar_creditos"
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'cantidad': cantidad}
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("¡Créditos comprados exitosamente!")
    else:
        print(f"Error al comprar créditos: {response.json()}")

# Función para consultar los créditos
def consultar_creditos(token):
    url = f"{BASE_URL}/consultar_creditos"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"Tus créditos disponibles: {response.json()['creditos']}")
    else:
        print(f"Error al consultar créditos: {response.json()}")

# Función principal para mostrar el menú
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
    mostrar_banner()

    while True:
        print("\n--- Menú de Opciones ---")
        print("1) Iniciar sesión")
        print("2) Registrarse")
        print("3) Comprar créditos")
        print("4) Consultar créditos")
        print("5) Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            token = login()
            if token:
                while True:
                    print("\nOpciones después de iniciar sesión:")
                    print("1) Consultar créditos")
                    print("2) Consultar DNI")
                    print("3) Regresar al menú principal")
                    subopcion = input("Selecciona una opción: ")

                    if subopcion == '1':
                        consultar_creditos(token)
                    elif subopcion == '2':
                        consultar_dni(token)
                    elif subopcion == '3':
                        break
                    else:
                        print("Opción inválida, por favor intenta nuevamente.")

        elif opcion == '2':
            register()

        elif opcion == '3':
            token = input("Por favor ingresa tu token de acceso: ")
            comprar_creditos(token)

        elif opcion == '4':
            token = input("Por favor ingresa tu token de acceso: ")
            consultar_creditos(token)

        elif opcion == '5':
            print("¡Gracias por usar DOXING_PE!")
            break
        else:
            print("Opción inválida, por favor intenta nuevamente.")

# Ejecución del menú
if __name__ == "__main__":
    menu()
