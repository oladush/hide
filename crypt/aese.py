import os
import rsa
import pyaes

# 128 bit, 192 bit and 256 bit keys
key_256 = os.urandom(32)
data = b"very very very match data"

pub = b'-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAljZIP9zkFqH5a8Z0GKTdm9VYOkr+vCmx7Atjs3aEtK6PisCe/QLv\n45SNyUcVVbAVe3mH4+CR9aJoK5UnIibONbQFmBQr19+wbir8jq28AS92daMD5M9x\nVEvkMXhin6iJJnr1sEX65WXzQMSe2EsWFssyCjhk8sv37n8U52clGzSNFhwUwnRM\nUcE3YiDwpf//SOIVc+cBxOH5BYZtLbjAG+Yy2D8akoH2J/aUZkIHguPMcPBlr+gr\n0+h+iA3XZZVJsu2n2c0MjiWbg/7INBvx67FqEAqOHOmJA4gvj7edht5jhb+cYJ/X\nlzWOnSCjCbDETKhlYLJuJxfnQvkH+WXUjQIDAQAB\n-----END RSA PUBLIC KEY-----\n'
priv = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEqQIBAAKCAQEAljZIP9zkFqH5a8Z0GKTdm9VYOkr+vCmx7Atjs3aEtK6PisCe\n/QLv45SNyUcVVbAVe3mH4+CR9aJoK5UnIibONbQFmBQr19+wbir8jq28AS92daMD\n5M9xVEvkMXhin6iJJnr1sEX65WXzQMSe2EsWFssyCjhk8sv37n8U52clGzSNFhwU\nwnRMUcE3YiDwpf//SOIVc+cBxOH5BYZtLbjAG+Yy2D8akoH2J/aUZkIHguPMcPBl\nr+gr0+h+iA3XZZVJsu2n2c0MjiWbg/7INBvx67FqEAqOHOmJA4gvj7edht5jhb+c\nYJ/XlzWOnSCjCbDETKhlYLJuJxfnQvkH+WXUjQIDAQABAoIBADou0nNyMyMVIFB/\nsS5uhaw7yg3iSKNHnzQoATldWe/GgbEkBTFJdvP28aiaEQh8yQVnwJwiu0ai3qir\nAFp5H3yru1L51TWr3mH94o+9ecoXwVG1j+eL9oDJWJ1U3RasqFswW4QoxxMeF0fq\nIQD0rJytnjdZOrjVCnpJ2IHAbVemJLtr+OCd4i/irH2cmaN4Rhitj/3Lukzb/CJ/\nRp7lNrnLWjowF66/pPVuiVJENWuh1i7Sl2HWzvSUouiIJ9WYms0PgOwZMspXbvBP\npjPTPKpbRQZYffUgdu+vWIaRo+v6M6+ltp9BwVuCn2wrD9hjkhlwqdBiVEr/BeDl\nBPEoHd0CgYkAnHltG9V7DBqEx+0QL26SbT6/BxQKaAm6vTvmiZa2nMZYXIrz9QA0\nziSNsScXobVBd/XJTZP42kJq3gCgDp/VCpq2wT+BPGHQFzYc178eduIe6zivxHuR\n1qNcP2vG+UKUZrRBj/QmRnowLVN4n0z6PrvhNsLJ2ZOLi1UNLErU20V4UUwlHSuG\n1wJ5APXBLKPDj2Bp3pQ8X+8tT2Uf+XlmYbJYjCEloFQrAjuXCalAJsXhZnO4MeI/\nEMmBgE4Jo1ZlRTOsN3ZBPhPKVc6AXGag6E47A9dKS/X/Uy/qRje3Mx+LUu0DUEKH\nCg+QMev1Meav/1xL6n5iKvvwF4UDsbL1dGUnOwKBiQCGVPxlo92SI4YQuSVnAw80\nOGT5J6xTat7lLHKbdkbpyqH7ONN9ZyLuQpVeG8h+7EP7P4gFUN6YSeLDGlhOlcro\n4q+4sdM6SmLCOpOCaLI3r6KJn83N6aPnV7GPRPC59v2+Okv60Mi3QpjvoLRyVjyT\n9OnBAHMXlkJ7aJX5i3i3kilb6foG0+JbAngrY77w7w86c5bDz2EUxog1D48pewUW\nywF6vLzw/2L2iHVBN71gxKolFklga8gX+9Bedt8q2th8BhUIwP4n2lqKCinGSPSb\nE1pbQZflx/21AQUCw0q4cA3lIOejx1nkY44c3f7AfyRz9Edjpwt1ze8pIfzW3vV9\nAo8CgYg1WjH2Ix9fjm2u6uJwWdQnmucrRpMhJ08p6d1NqQPUmkI//kwLfgkib0Eg\nZFtGEKL79gwI1lpl1c0dD6552ED6/rUd7Um7xvoM+oUD2sFhfZSPc0qQaCY45RdW\nuEBa/oynVZbUNlyYnwofrz5p4kU91Vn4ThklH47cJDy39Hgz9QSOTkOSLn0Z\n-----END RSA PRIVATE KEY-----\n'


def rsa_crypt(data, pub_key):
    pub_key = rsa.PublicKey.load_pkcs1(pub_key)
    return rsa.encrypt(data, pub_key)


def rsa_decrypt(crypt, priv_key):
    priv_key = rsa.PrivateKey.load_pkcs1(priv_key)
    return rsa.decrypt(crypt, priv_key)


def aes_crypt(data, key):
    aes = pyaes.AESModeOfOperationCTR(key)
    crypt = aes.encrypt(data)
    return crypt


def aes_decrypt(crypt, key):
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted = aes.decrypt(crypt)
    return decrypted

# crypt = aes_crypt(data, key_256)
# print(crypt)
# crypt_key = rsa_crypt(key_256, pub)
# print(crypt_key)
# decrypt_key = rsa_decrypt(crypt_key, priv)
# print(decrypt_key)
# decrypt = aes_decrypt(crypt, decrypt_key)
# print(decrypt)


def encode_run(data, pub_key):
    session_key = os.urandom(32)
    crypt = aes_crypt(data, session_key)
    crypt_key = rsa_crypt(session_key, pub_key)
    with open("session_encrypted_key", "wb") as key_file:
        key_file.write(crypt_key)
    return crypt


def decode_run(crypt, priv_key):
    with open("session_encrypted_key", "rb") as key_file:
        crypt_key = key_file.read()
    decrypt_key = rsa_decrypt(crypt_key, priv_key)
    decrypt = aes_decrypt(crypt, decrypt_key)
    return decrypt

# cr = encode_run(data, pub)
# print(cr)
#
# data = decode_run(cr, priv)
# print(data)
