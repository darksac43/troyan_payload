# troyan_payload
# Troyan Payload Generator

Este repositorio contiene una herramienta creada por [Dark_sac](https://github.com/darksac43) que permite generar payloads maliciosos cifrados en Python. La herramienta genera un archivo ejecutable que se conecta de vuelta a una dirección IP y un puerto especificados, lo que permite obtener acceso remoto a la máquina objetivo.

## Características

- **Generación de Payloads:** La herramienta permite crear un payload cifrado con una clave generada al azar utilizando la biblioteca `cryptography`.
- **Reverse Shell:** El payload generado establece una conexión de vuelta a la dirección IP y puerto especificados, permitiendo la ejecución remota de comandos en la máquina objetivo.
- **Cifrado del Código:** El código del payload se cifra utilizando el algoritmo Fernet para protegerlo contra análisis estáticos.
- **Compilación a .exe:** La herramienta utiliza `PyInstaller` para compilar el payload a un archivo ejecutable .exe.

## Instalación

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/darksac43/troyan_payload.git
    cd troyan_payload
    ```

2. **Instala las dependencias necesarias:**
    ```bash
    pip install -r cryptography
    pip install -r requests
    pip install -r pyinstaller

    ```

3. **Genera un payload:**
    - Ejecuta el script principal y sigue las instrucciones para generar un payload malicioso.
    ```bash
    python troyan_payload.py
    ```

## Dependencias

- `cryptography`: Utilizada para el cifrado del código.
- `socket`: Para la comunicación de red del reverse shell.
- `subprocess`: Para ejecutar comandos en la máquina objetivo.
- `PyInstaller`: Para compilar el payload en un archivo ejecutable.

## Uso

Después de ejecutar el script principal, se generará un archivo `payload.py` cifrado que podrás compilar a un archivo ejecutable .exe utilizando `PyInstaller`.

```bash
pyinstaller --onefile --noconsole payload.py
```

El archivo payload.exe generado puede ser ejecutado en la máquina objetivo, estableciendo una conexión de vuelta a tu máquina y permitiendo el control remoto.

## Disclaimer

Advertencia: Esta herramienta ha sido desarrollada con fines educativos y de investigación. No me hago responsable del uso indebido que se le pueda dar. Utiliza esta herramienta únicamente en entornos controlados y con el consentimiento explícito del propietario del sistema. El uso de este tipo de herramientas en sistemas sin autorización es ilegal y puede tener consecuencias graves
