import os
from tkinter import messagebox

try:
    os.mkdir("dataset")
    os.mkdir("trainer")
    os.mkdir("files")
except Exception as e:
    messagebox.showerror("ERROR", "Directory already exists:\n" + str(e))
