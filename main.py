import random

# lista caratteri casuali
caratteri = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]òèùàì:.;,'/  "

# chiedo all'utne la lunghezza della psw
num_caratteri = int(input("Inserire il numero dei caratteri per la tua password"))

# creo inizialmente una password vuota
password = ''


for i in range(num_caratteri):
    # prendo un carattere casuale
    carattere = random.choice(caratteri)
    # aggiungo il carattere casuale alla password
    password += carattere

# stampo la password finale
print(password)