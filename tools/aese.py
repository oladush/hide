"""This module contains all the encryption methods used in the project."""

import os
import rsa
import pyaes

pub = b""
priv = b""
session_key = ""

def accept_key(public_key, private_key):
    global pub, priv
    pub, priv = public_key, private_key


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


def encode_run(data, pub_key):
    global session_key
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
