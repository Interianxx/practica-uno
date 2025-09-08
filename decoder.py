import os, json, base64
from dotenv import load_dotenv   # pip install python-dotenv
from assets import encrypAES

load_dotenv()  # carga .env en variables de entorno

with open("mensaje_oculto.json","r",encoding="utf-8") as f:
    pkg = json.load(f)

key_b64 = os.getenv("KEY_B64")
iv_b64 = pkg["iv_b64"]
ct_b64 = pkg["ciphertext_b64"]

key = base64.b64decode(key_b64)
print(encrypAES.decode(key, iv_b64, ct_b64))
