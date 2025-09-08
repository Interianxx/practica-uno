# Práctica: Cifrado y descifrado AES‑CBC (Python)

Sistema educativo de cifrado simétrico usando **AES en modo CBC** con **padding PKCS7**, basado en **PyCryptodome**. Incluye generación de paquete (`iv_b64`, `ciphertext_b64`) y descifrado con una clave en **Base64** cargada desde `.env`.

---

## Objetivos
- Cifrar un mensaje con **AES‑CBC** y padding **PKCS7**.
- Generar y usar **IV aleatorio** de 16 bytes.
- Codificar binarios en **Base64**.
- Separar **clave** de los datos (práctica segura).

> Nota: Para simplificar, el equipo puede consensuar un JSON que incluya `key_b64`. En producción eso **no** se hace.

---

## Requisitos
- Python 3.10+
- Paquetes: `pycryptodome`, `python-dotenv`

```bash
# opcional: entorno virtual
python -m venv .venv
# activar: Windows PowerShell
.venv\\Scripts\\Activate.ps1
# activar: Linux/Mac
source .venv/bin/activate

pip install pycryptodome python-dotenv
```

---

## Estructura del proyecto
```
practica-uno/
  .env                 # NO subir a git
  .gitignore
  decoder.py
  main.py
  mensaje_oculto.json  # paquete iv/ciphertext (opcional: también key_b64 en modo “todo en uno”)
  assets/
    encrypAES.py       # utilidades AES (getKey, encode, decode)
    local_db.py        # helpers para guardar/cargar JSON
```

---

## Variables de entorno
Crear `.env` en la raíz:
```
KEY_B64=PEGA_AQUI_TU_LLAVE_BASE64
```
Asegura que `.env` está ignorado:
```
# .gitignore
.env
```

---

## Uso rápido

### 1) Cifrar y generar el paquete
Ejecuta:
```bash
python main.py
```
Salida: `mensaje_oculto.json` con:
```json
{
  "iv_b64": "IV_EN_BASE64",
  "ciphertext_b64": "CIPHERTEXT_EN_BASE64"
}
```

> Variante “todo en uno” para fines académicos: incluir también `key_b64` en el JSON.

### 2) Descifrar
Coloca la clave en `.env`:
```
KEY_B64=PEGA_AQUI_TU_LLAVE_BASE64
```
Ejecuta:
```bash
python decoder.py
```
Salida: **texto plano** en consola.

---

## Flujo sugerido de equipo (yo cifro, tú descifras)
1. **Persona A** ejecuta `main.py` y obtiene `mensaje_oculto.json` + **key_b64** (en Base64).
2. Envía **paquete** y **clave** por **canales distintos** (ej.: JSON por correo, clave por WhatsApp).
3. **Persona B** pone la clave en `.env` y ejecuta `python decoder.py`.

> Si el profesor exige practicidad sobre seguridad, se puede mandar un único JSON con `iv_b64`, `ciphertext_b64`, `key_b64`.

---

## Seguridad básica
- **CBC** requiere IV único por cifrado. El IV puede viajar en claro.
- **PKCS7** para alinear a bloques de 16 bytes.
- **CBC no autentica** el mensaje. Para integridad se agrega HMAC sobre `IV||ciphertext` o se usa **AES‑GCM**. No es necesario para esta práctica.

---

## Ejemplos

### `mensaje_oculto.ejemplo.json` (seguro, sin clave)
```json
{
  "iv_b64": "IV_EN_BASE64",
  "ciphertext_b64": "CIPHERTEXT_EN_BASE64"
}
```

### `mensaje_oculto.ejemplo.json` (todo en uno, sólo academia)
```json
{
  "iv_b64": "IV_EN_BASE64",
  "ciphertext_b64": "CIPHERTEXT_EN_BASE64",
  "key_b64": "CLAVE_EN_BASE64"
}
```

---

## Comandos útiles
```bash
# generar paquete
python main.py
# descifrar
python decoder.py
# comprobar que KEY_B64 se cargó
python -c "import os;from dotenv import load_dotenv;load_dotenv();print(os.getenv('KEY_B64'))"
```

---

## Problemas comunes
- `ModuleNotFoundError: dotenv` → instalar `python-dotenv`.
- `ValueError: Padding inválido` → clave incorrecta o `KEY_B64` mal copiada.
- No imprime texto → `.env` no cargó. Verificar con el comando de comprobación.

---

## Rúbrica sugerida (para evaluación)
- [ ] Usa **AES‑CBC** con **IV** aleatorio de 16 bytes.
- [ ] Aplica **PKCS7** para padding.
- [ ] Codifica binarios con **Base64**.
- [ ] Separa **clave** de `mensaje_oculto.json` (recomendado) o justifica el modo “todo en uno”.
- [ ] Incluye README con pasos reproducibles.
- [ ] Código claro y ejecutable.

---

## Integrantes de la actividad
Trabajo académico. 
Interian Pech Jose Alejandro
Fernando Gamaliel Rodriguez

