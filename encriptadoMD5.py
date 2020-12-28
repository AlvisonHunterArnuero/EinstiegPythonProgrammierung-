# MD5 (Message-Digest Algorithm 5) and SHA (Secure Hash Algorithm), BLAKE y SHAKE.
# -------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - December 28th, 2020
# Website: https://alvisonhunter.com/

import hashlib

def encryptMD5():
    # En donde el primer parámetro debe ser una cadena como «sha1», «md5», «sha224»
    # y el segundo cualquier tipo de cadena que queramos cifrar.
    h = hashlib.new("sha1", b"www.recursospython.com - Recursos Python")
    print(h.digest())
    # El método digest() retorna la cadena cifrada en binario. Para obtenerla en hexadecimal,
    # existe la función hexdigest().
    # Nótese que para los algoritmos SHAKE, los métodos digest() y hexdigest() requieren
    # como argumento la longitud de la cadena resultante (por ejemplo, 128 o 256).

    print(h.hexdigest())


encryptMD5()
