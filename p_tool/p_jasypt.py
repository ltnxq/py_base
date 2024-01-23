from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

class BasicTextEncryptor:
    def __init__(self, password):
        self.password = password.encode()
        self.key = self.password[:16]  # AES-128使用16字节的密钥
    
    def encrypt(self, text):
        cipher = AES.new(self.key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(text.encode(), AES.block_size))
        iv = b64encode(cipher.iv).decode()
        ciphertext = b64encode(encrypted_data).decode()
        return iv + ciphertext
    
    def decrypt(self, ciphertext):
        iv = b64decode(ciphertext[:24])
        ciphertext = b64decode(ciphertext[24:])
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_data.decode()

# 示例用法
text = "Hello, World!"
password = "CloudApi"

encryptor = BasicTextEncryptor(password)
encrypted_text = encryptor.encrypt(text)
print("Encrypted Text: ", encrypted_text)

decrypted_text = encryptor.decrypt(encrypted_text)
print("Decrypted Text: ", decrypted_text)