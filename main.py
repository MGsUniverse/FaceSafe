import recognizer
from cryptography.fernet import Fernet
from tkinter import *

id = recognizer.recognize()

root = Tk()

# specify size of window.
root.geometry("250x170")

with open('files/' + str(id) + ".key") as key:
    fernet = Fernet(key.read())

with open("files/" + str(id) + ".bin", 'rb') as enc_file:
    encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# Create text widget and specify size.
T = Text(root, height=5, width=52)
T.delete(1.0, END)
T.insert(END, decrypted)

# Create label
l = Label(root, text="Private File")
l.config(font=("Courier", 14))


def save(face_id):
    # encrypting the file
    encrypted = fernet.encrypt(bytes(T.get("1.0", END), "utf-8"))

    # opening the file in write mode and
    # writing the encrypted data
    with open("files/" + str(face_id) + ".bin", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


# Create button for next text.
b1 = Button(root, text="Save", command=lambda: save(id))

# Create an Exit button.
b2 = Button(root, text="Exit", command=root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()
mainloop()
