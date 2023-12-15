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

%Georgiy666%
