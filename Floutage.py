from random import randint
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter import messagebox

import os

from Numéro_de_plaque import *

imageo=None
#fenetre graphique

def redimension(file):
    
    global imageo,lab6,pt_image
    
    imageOriginale=Image.open(file)
    largeur,hauteur=imageOriginale.size
    pt_image=file[:-4]+"_petite."+file[-3:]
    
    try :
        lab6.destroy()
    except :
        pass
    
    if largeur > 900 or hauteur > 750:
        imageOriginale.resize((largeur-int(largeur//2),hauteur-int(hauteur//2))).save(pt_image)
        imageo= ImageTk.PhotoImage(file = pt_image)
        lab6=Label(fenetre,text="Aperçu de l'image (redimensionnée)",font =("Helvetica",15),fg="red")
        lab6.grid(row=1,column=1,padx=5,pady=5)

    else:
        imageo= ImageTk.PhotoImage(file = str(file))
        lab6=Label(fenetre,text="Aperçu de l'image",font =("Helvetica",15),fg="red")
        lab6.grid(row=1,column=1,padx=5,pady=5)


def on_entry_click1(event):   
    global firstclick1

    if firstclick1:
        firstclick1 = False
        entry1.delete(0, "end")
    if not firstclick1:
        firstclick1 = True
        entry2.delete(0, "end")
        
def UploadAction(event=None):
    global filename, button1, lab4, lab5,button2,button, plate_nb, entry1, password, entry2


    button1.destroy()
    filename = filedialog.askopenfilename()
    

    if filename != "" :
        redimension(filename)

            
        button1.destroy()

        button2 = Button(fenetre,text="Annuler",font =("Helvetica",15),command= annuler)
        button2.grid(row=0,column=2,padx=10)

        lab5 = Label(fenetre, bg="grey",height=45,width=135)
        lab5.grid(row=0,column=1,padx=20,pady=20)
        
        lab4=Label(fenetre,image=imageo)
        lab4.grid(row=0,column=1,padx=5,pady=5)

        button = Button(fenetre,text="Floutter une zone",font =("Helvetica",15),command= create_window)
        button.place(x=1100,y=400)

        plate_nb= StringVar()
        entry1= Entry(fenetre, textvariable= plate_nb, width=25, justify = "center")
        entry1.insert(0, 'Entrez votre plaque...')
        entry1.bind('<FocusIn>', on_entry_click1)
        entry1.grid(row=0,column=3,padx=3,pady=10)




        password= StringVar()
        entry2= Entry(fenetre, textvariable= password, width=25, justify = "center")
        entry2.insert(0, 'Entrez votre MdP...')
        entry2.grid(row=0,column=4,padx=3,pady=10)



        button3 = Button(fenetre,text="Quitter",font =("Helvetica",15),command= quitter)
        button3.place(x=1000,y=400)
        
    else :
        menufloutage()
    
def quitter():
    try :
        os.remove(pt_image)
    except :
        pass
    fenetre.destroy()
    
    
     
def annuler():
    global X,Y,i
    
    i=0
    X=[]
    Y=[]
    lab4.destroy()
    lab5.destroy()
    lab6.destroy()
    button.destroy()
    button2.destroy()
    entry1.destroy()
    entry2.destroy()

    try :
        
        button4.destroy()
        window.destroy()
        os.remove(pt_image)
        
    except :
        pass
    menufloutage()
    



    

def lissage() :
    global imageo,imageOriginale,filename,X,Y,button4
    
    imageOriginale=Image.open(filename)
    largeur,hauteur=imageOriginale.size
    imageModifiee = Image.new("RGB",(largeur, hauteur))
    
    

    for y in range(hauteur) :
        for x in range(largeur) :
            p = imageOriginale.getpixel((x,y))
            if X[1] > x > X[0] and Y[1] > y > Y[0] :
                a = imageOriginale.getpixel((x-7,y-7))
                b = imageOriginale.getpixel((x-7,y))
                c = imageOriginale.getpixel((x-7,y+7))
                d = imageOriginale.getpixel((x,y-7))
                f = imageOriginale.getpixel((x,y+7))
                g = imageOriginale.getpixel((x+7,y-7))
                h = imageOriginale.getpixel((x+7,y))
                j = imageOriginale.getpixel((x+7,y+7))
                q0 = (a[0]+b[0]+c[0]+d[0]+p[0]+f[0]+g[0]+h[0]+j[0])//9
                q1 = (a[1]+b[1]+c[1]+d[1]+p[1]+f[1]+g[1]+h[1]+j[1])//9
                q2 = (a[2]+b[2]+c[2]+d[2]+p[2]+f[2]+g[2]+h[2]+j[2])//9 
                q = (q0,q1,q2)
            else :
                q = p[0],p[1],p[2]
            imageModifiee.putpixel((x,y),q)
    imageModifiee.save(filename[:-4]+"_floutte."+filename[-3:])
   
    try :
        os.remove(pt_image)
    except :
        pass
    x = filename[:-4]+"_floutte."+filename[-3:]
    redimension(x)
    
    button2.configure(text="Choisir une nouvelle image")
    button4 = Button(fenetre,text="Recommencer",font =("Helvetica",15),command= create_window)
    button4.grid(row=0,column=3,padx=10)

    pl = plate_nb.get()
    if    pl !="Entrez votre plaque...":
        tail, head = os.path.split(filename)
        nom_fichier = head[:-4]
        nb_plaque = plate_nb.get()
        mdp = password.get()
        register_user(nom_fichier, nb_plaque, mdp)




    button.destroy()
    entry1.destroy()
    entry2.destroy()
    lab4=Label(fenetre,image=imageo)
    lab4.grid(row=0,column=1,padx=5,pady=5)
    


    
def create_window():
    global window,X,Y,i


    if i==2:
        X=[]
        Y=[]
        i=0
        button4.destroy()

    window = Toplevel(fenetre)

    imageOriginale=Image.open(filename)
    largeur,hauteur=imageOriginale.size
    imageo2 = ImageTk.PhotoImage(file = str(filename))
    lab8 = Label(window,image=imageo2)
    lab8.grid(row=0,column=0,padx=5,pady=5)
    messagebox.showinfo("Le flouttage formera une zone rectangulaire", "Placez la diagonale du rectangle, cliquer: \n" 
                                            "1) Où commence la ligne diagonale\n"
                                           "2) Où finie la ligne diagonale ")

    window.bind("<Button 1>",getorigin)
    window.mainloop()



def getorigin(eventorigin):
    global x0,y0,i,X,Y
    
    if i<=1:
        x0 = eventorigin.x
        y0 = eventorigin.y
        x0-=5
        y0-=5
        X.append(x0)
        Y.append(y0)
        print(x0,y0,i)
        i+=1
    if i==2:
        if X[1]<X[0]:
            X=[X[1],X[0]]
        if Y[1]<Y[0]:
            Y = [Y[1],Y[0]]
        window.destroy()
        lissage()



def menufloutage():
    
    global button1
    
    button1= Button(fenetre,text="Rechercher une image",font =("Helvetica",15),height=30,width=70,command= UploadAction)
    button1.grid(row=0,column=1,padx=20,pady=40)
    
    button3 = Button(fenetre,text="Quitter",font =("Helvetica",15),command= quitter)
    button3.place(x=1000,y=400)




def mainfloutage():
    global fenetre

    fenetre = Tk()
    largeur_ecran = fenetre.winfo_screenwidth()
    hauteur_ecran = fenetre.winfo_screenheight()
    fenetre.geometry(str(largeur_ecran-100)+"x"+str(hauteur_ecran-100)+"+"+str(int(hauteur_ecran/2-(hauteur_ecran-100)/2))+"+"+str(int(largeur_ecran/2-(largeur_ecran-100)/2)))
    fenetre.configure(background='black')
    fenetre.title("Floutteur")

    menufloutage()
    fenetre.protocol("WM_DELETE_WINDOW",quitter)

    try:
        window.mainloop()
    except:
        pass
    fenetre.mainloop()

i=0
X=[]
Y=[]

firstclick1 = True
