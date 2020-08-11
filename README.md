# PyCryptoContainer
## What is it? 

With this program you can encrypt and securely hide files from unwanted persons. Data encryption of your data is done using the AES algorithm, the key of which is later encrypted using RSA.

## How to use?
There is nothing difficult in using this program. The only thing you need is **python3** and the **pip** package installer. In order to build this program into an executable file you may need **PyInstaller**.

1. Make sure you have all of the above.
2. Сopy the this repository to your computer.
3. Install the following packages using **pip**: pyaes, rsa, pyglet.
4. In the **parameters.py** file, specify the desired settings. Create a password, specify encryption keys. (they can be generated in a file **gen_rsa.py**)
5. Responsibly approach the previous point, in case of loss of the password, the data cannot be restored.
6. Сreate a directory **folder** on your desktop and put the data you want to encrypt there (**at this stage it is better to create a backup copy**).
7. Make sure the program works correctly.
8. Package the program into an executable using **pyinstaller**.
9. Are you happy?

If you have any questions, you want to point out an error or help the project, write her oladushek.hokinga@gmail.com
