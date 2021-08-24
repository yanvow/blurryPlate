from random import randint
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter import messagebox

import os
import Floutage

def delete2():
  fenetre3.destroy()
 
def delete3():
  fenetre4.destroy()
 
def delete4():
  fenetre5.destroy()
   
def login_sucess():
  global fenetre3

  file = open(plate1, "r")
  plate = file.readlines()
  
  fenetre3 = Toplevel(fenetre)
  fenetre3.title("Réussi")
  fenetre3.geometry("150x100")
  Label(fenetre3, text = "Plaque : " + plate[1]).pack()
  Button(fenetre3, text = "OK", command =delete2).pack()
 
def password_not_recognised():
  global fenetre4
  fenetre4 = Toplevel(fenetre)
  fenetre4.title("Réussi")
  fenetre4.geometry("150x100")
  Label(fenetre4, text = "Erreur MdP").pack()
  Button(fenetre4, text = "OK", command =delete3).pack()
 
def plate_not_found():
  global fenetre5
  fenetre5 = Toplevel(fenetre)
  fenetre5.title("Réussi")
  fenetre5.geometry("150x100")
  Label(fenetre5, text = "Fichier non trouvé").pack()
  Button(fenetre5, text = "OK", command =delete4).pack()

def login_verify():
  global plate1
  
  plate1 = plate_verify.get()
  password1 = password_verify.get()
  plate_entry1.delete(0, END)
  password_entry1.delete(0, END)
 
  list_of_files = os.listdir()
  if plate1 in list_of_files:
    file1 = open(plate1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()
 
  else:
        plate_not_found()
 
def register_user(file, plate, password):
  print("working")
   
  file_info = file
  plate_info = plate
  password_info = password
  
  file=open(file_info, "w")
  file.write(file_info+"\n")
  file.write(plate_info+"\n")
  file.write(password_info)
  file.close()
 
def login():
  global fenetre2
  fenetre2 = Toplevel(fenetre)
  fenetre2.title("S'identifier")
  fenetre2.geometry("300x250")
  Label(fenetre2, text = "Entrez vos détails ci-dessous").pack()
  Label(fenetre2, text = "").pack()
 
  global plate_verify
  global password_verify
   
  plate_verify = StringVar()
  password_verify = StringVar()
 
  global plate_entry1
  global password_entry1
   
  Label(fenetre2, text = "Nom du fichier * ").pack()
  plate_entry1 = Entry(fenetre2, textvariable = plate_verify)
  plate_entry1.pack()
  Label(fenetre2, text = "").pack()
  Label(fenetre2, text = "Mot de passe * ").pack()
  password_entry1 = Entry(fenetre2, textvariable = password_verify)
  password_entry1.pack()
  Label(fenetre2, text = "").pack()
  Button(fenetre2, text = "S'identifier", width = 10, height = 1, command = login_verify).pack()
   
   
def main_screen():
  global fenetre
  fenetre = Tk()
  fenetre.geometry("300x250")
  fenetre.title("Numéro de plaque")
  Label(text = "Numéro de plaque", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack() # Espace
  Button(text = "S'identifier", height = "2", width = "30", command = login).pack()

  fenetre.mainloop()

