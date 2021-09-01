# Imports
from Crypto.Cipher import AES
import secrets
import string

# Opening the settings file
settings = []
with open("C:/Users/2005s/Documents/Visual Studio Code/Python/Tkinter/Custom-Text-Editor/Settings.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        settings.append(line)
print(settings)

# Generating a random 32-byte key as a byte array
key = ''.join(secrets.choice(string.digits + string.ascii_letters) for _ in range(32))
key = key.encode("utf-8")
print("Generated 32-byte array key:", key)

# Decode it into a string to save into a settings file
key = key.hex()
print("Key without b'': ", key)

settings.pop(1)
settings.insert(1, f"{key}")
settings.pop(0)
settings.insert(0, "False")
print(settings)
key = bytearray.fromhex(key)

# Saving the settings into the file
save_settings = "\n".join(settings)
with open("C:/Users/2005s/Documents/Visual Studio Code/Python/Tkinter/Custom-Text-Editor/Settings.txt", "w") as f:
    f.write(save_settings)

# Written text
written_text = "Hello world!"

# Converts to bytes array
encoded_written_text = written_text.encode("utf-8")
print("Key converted to byte array: ", key)

# Create new cipher, nonce, and tag
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(encoded_written_text)
nonce = cipher.nonce
nonce = nonce.hex()
tag = tag.hex()
key = key.hex()
ciphertext = ciphertext.hex()
print("Key: ", key)
print("Nonce: ", nonce)
print("Tag: ", tag)
print("Ciphertext: ", ciphertext)
print("Original message: ", written_text)

# ciphertext = str(ciphertext)
# encrypted_text_to_save = encrypted_text_to_save.split("'")
# encrypted_text_to_save = encrypted_text_to_save[1]