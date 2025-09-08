import os, json, base64
from dotenv import load_dotenv   # pip install python-dotenv
from assets import encrypAES

load_dotenv()  # carga .env en variables de entorno

with open("mensaje_oculto_recibido.json","r",encoding="utf-8") as f:
    pkg = json.load(f)
# La parte de donde se extrae la llave del json no deberia estar, pero es solo para fines academicos
# En un caso real, la llave no debe estar en el mismo lugar que el mensaje cifrado, ni siquiera en el mismo servidor
# En este caso metemos como una variable de entorclno que podemos decir que es un metodo "seguro" de tener la llave en un proyecto 
# Con el manejo debido en el .gitignore, no deberiamos filtrar la llave en un repositorio publico
key_b64 = os.getenv("KEY_B64") or pkg["key_b64"]  
iv_b64 = pkg["iv_b64"]
ct_b64 = pkg["ciphertext_b64"]

key = base64.b64decode(key_b64)
print("El mensaje encriptado es:", encrypAES.decode(key, iv_b64, ct_b64))
