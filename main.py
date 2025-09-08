from assets import encrypAES, local_db
import base64

def main():
    key = encrypAES.getKey(32)  # 256-bit
    iv_b64, ct_b64 = encrypAES.encode(key, "Xeoz vamos a sacar una mac")
    key_b64 = base64.b64encode(key).decode("utf-8")

    paquete = {
        "iv_b64": iv_b64,
        "ciphertext_b64": ct_b64,
        "key_b64": key_b64  # Solo fines académicos
    }

    local_db.save(paquete, "mensaje_oculto.json")
    print("Listo: mensaje_oculto.json generado.")

if __name__ == "__main__":
    main()

