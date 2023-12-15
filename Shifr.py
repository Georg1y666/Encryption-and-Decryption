from tkinter import Tk, Button, Label, Text, Entry, END
from cryptography.fernet import Fernet
import rsa

# Генерация пары ключей RSA
def generate_rsa_key_pair():
    publicKey, privateKey = rsa.newkeys(2048)
    return publicKey, privateKey

# Сохранение ключа в файл
def save_key_to_file(key, filename):
    with open(filename, 'wb') as f:
        f.write(key.save_pkcs1())

# Загрузка ключа из файла
def load_key_from_file(filename):
    with open(filename, 'rb') as f:
        key_data = f.read()
        return rsa.PrivateKey.load_pkcs1(key_data)

# Шифрование текста с использованием AES
def encrypt_text_aes(text, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

# Дешифрование текста с использованием AES
def decrypt_text_aes(encrypted_text, key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    return decrypted_text.decode()

# Шифрование ключа AES с использованием RSA
def encrypt_aes_key_rsa(aes_key, public_key):
    encrypted_aes_key = rsa.encrypt(aes_key, public_key)
    return encrypted_aes_key

# Дешифрование ключа AES с использованием RSA
def decrypt_aes_key_rsa(encrypted_aes_key, private_key):
    aes_key = rsa.decrypt(encrypted_aes_key, private_key)
    return aes_key

def encrypt_text():
    input_text = text_input.get("1.0", END).strip()
    aes_key = Fernet.generate_key()

    public_key, private_key = generate_rsa_key_pair()
    encrypted_aes_key = encrypt_aes_key_rsa(aes_key, public_key)
    encrypted_text = encrypt_text_aes(input_text, aes_key)

    # Сохранение ключа в файл
    save_key_to_file(private_key, 'private_key.pem')

    text_input_key.delete(0, END)
    text_input_key.insert(END, encrypted_aes_key.hex())

    text_output.delete("1.0", END)
    text_output.insert(END, encrypted_text)

def decrypt_text():
    input_text = text_input.get("1.0", END).strip()
    encrypted_aes_key_hex = text_input_key.get().strip()

    # Загрузка ключа из файла
    private_key = load_key_from_file('private_key.pem')
    
    encrypted_aes_key = bytes.fromhex(encrypted_aes_key_hex)
    aes_key = decrypt_aes_key_rsa(encrypted_aes_key, private_key)
    decrypted_text = decrypt_text_aes(input_text, aes_key)

    text_output.delete("1.0", END)
    text_output.insert(END, decrypted_text)

# Создание окна приложения
app = Tk()
app.title("Приложение для шифрования/дешифрования")

# Поле для ввода текста
text_input_label = Label(app, text="Текст для шифрования/дешифрования:")
text_input_label.pack()
text_input = Text(app, height=5, width=30)
text_input.pack()

# Поле для ввода зашифрованного ключа AES
key_input_label = Label(app, text="Зашифрованный ключ AES (в hex):")
key_input_label.pack()
text_input_key = Entry(app)
text_input_key.pack()

# Кнопка "Зашифровать"
encrypt_button = Button(app, text="Зашифровать", command=encrypt_text)
encrypt_button.pack()

# Кнопка "Дешифровать"
decrypt_button = Button(app, text="Дешифровать", command=decrypt_text)
decrypt_button.pack()

# Поле для вывода результатов
text_output_label = Label(app, text="Результат:")
text_output_label.pack()
text_output = Text(app, height=5, width=30)
text_output.pack()

# Запуск приложения
app.mainloop()