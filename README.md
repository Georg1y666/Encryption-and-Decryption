ENG
Encryption and Decryption Application
Overview
This repository contains a simple encryption and decryption application implemented in Python using the Tkinter GUI toolkit. The application allows users to encrypt and decrypt text messages using a combination of AES (Advanced Encryption Standard) and RSA (Rivest–Shamir–Adleman) algorithms.

Features
Text Encryption/Decryption: The application allows users to input plain text, which is then encrypted using a randomly generated AES key. The AES key is further encrypted with an RSA public key for secure transmission.

Key Management: The application automatically generates RSA key pairs for encryption and provides an option to save the private key securely. The user can load the private key when decrypting messages.

User Interface: The graphical user interface (GUI) is built using Tkinter, making it user-friendly and accessible for users to interact with the encryption and decryption functionality.

Usage
Encryption:

Enter the text in the input field.
Click the "Encrypt" button to generate an encrypted message and the corresponding encrypted AES key.
Save the private key for future decryption.
Decryption:

Enter the encrypted text in the input field.
Paste the encrypted AES key (in hex format) from the encryption step.
Click the "Decrypt" button to retrieve the original message.
Dependencies
Python 3.x
Tkinter (for GUI)
cryptography library (for Fernet encryption)
rsa library (for RSA encryption)
How to Run
Install the required dependencies by running pip install cryptography rsa.
Run the script by executing python your_script_name.py in the terminal.
Feel free to use, modify, and enhance this application for your encryption and decryption needs.

RU

Приложение для Шифрования и Дешифрования
Обзор
Этот репозиторий содержит простое приложение для шифрования и дешифрования, реализованное на Python с использованием графической библиотеки Tkinter. Приложение позволяет пользователям шифровать и дешифровать текстовые сообщения с использованием комбинации алгоритмов AES (Advanced Encryption Standard) и RSA (Rivest–Shamir–Adleman).

Возможности
Шифрование/Дешифрование текста: Приложение позволяет вводить обычный текст, который затем шифруется с использованием случайного ключа AES. Ключ AES также шифруется открытым ключом RSA для безопасной передачи.

Управление ключами: Приложение автоматически генерирует пары ключей RSA для шифрования и предоставляет опцию сохранить закрытый ключ для безопасного использования. Пользователь может загрузить закрытый ключ при дешифровании сообщений.

Графический интерфейс пользователя (GUI): Интерфейс создан с использованием Tkinter, что делает его удобным для взаимодействия пользователей с функциональностью шифрования и дешифрования.

Использование
Шифрование:

Введите текст в поле ввода.
Нажмите кнопку "Зашифровать", чтобы создать зашифрованное сообщение и соответствующий зашифрованный ключ AES.
Сохраните закрытый ключ для последующего дешифрования.
Дешифрование:

Введите зашифрованный текст в поле ввода.
Вставьте зашифрованный ключ AES (в шестнадцатеричном формате) из шага шифрования.
Нажмите кнопку "Дешифровать", чтобы получить исходное сообщение.
Модули
Python 3.x
Tkinter (для GUI)
Библиотека cryptography (для шифрования Fernet)
Библиотека rsa (для шифрования RSA)
Как запустить
Установите необходимые зависимости, выполнив pip install cryptography rsa.
Запустите скрипт, выполнив python ваш_скрипт.py в терминале.
Не стесняйтесь использовать, изменять и улучшать это приложение для своих потребностей в шифровании и дешифровании.

%Georgiy666%
