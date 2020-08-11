import rsa

pub_key, priv_key = rsa.newkeys(1024)
pub_key = pub_key.save_pkcs1()
priv_key = priv_key.save_pkcs1()

print("your public key: ", end=" ")
print(pub_key)
print("your private key: ", end=" ")
print(priv_key)
