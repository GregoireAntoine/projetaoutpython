
import csv
from tkinter import *
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
from Imagerecup import * 
import random
from tkinter.messagebox import *
import unittest
import time

class Laphoto:
    #initalisation des informations nécéssaire
    def __init__(self,  nom,frame,ligne,colonne,lettre):
        self.nom = nom
        self.frame=frame
        self.ligne=ligne
        self.colonne=colonne
        self.lettre = lettre
    # Function de vérification de la présence ou non de la lettre dans le mot représenté par l'image
    def verif (self) : 
      if self.lettre in self.nom : 
        buton = Label(self.frame,text=self.nom ,bg="#85F450",height = 15, width = 62)
        buton.grid(row=self.ligne,column=self.colonne)
      else :
        buton = Label(self.frame,text=self.nom ,bg="#FF7F53",height = 15, width = 62)
        buton.grid(row=self.ligne,column=self.colonne)

def fctproject():
  # liste des sons 
  tab=["a","b","d","é","è","f","g","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]
  liste=['','','',''] #lsite vide
  width = 440 #largeur d'une image
  height = 230 # hauteur d'une image
  #fonction de renouvelement de fenêtre
  def fctsuivant() :
    #On efface la lettre présente sur la fenêtre
    lettre = Label(fenetre, text="     ", font=("Courrier",30))
    lettre.grid(row=0,column=0)
    # On choisi une lettre au hasard dans la liste et onn l'affiche à l'écran
    lettre_choisie=tab[random.randint(0, len(tab)-1)]
    lettre = Label(fenetre, text="lettre : "+lettre_choisie, font=("Courrier",30),bg='#53BFFF',fg="white",width='7')
    lettre.grid(row=0,column=0)
    # Execution de la fonction Choiximage permettant de récupérer 4 noms d'image différents
    choiximage()
    # Récupération des images grâce à leurs noms 
    img1 = Image.open(r'photo/'+liste[0])
    img1 = img1.resize((width,height))
    photoImg1 =  ImageTk.PhotoImage(img1)

    img2 = Image.open(r'photo/'+liste[1])
    img2 = img2.resize((width,height))
    photoImg2 =  ImageTk.PhotoImage(img2)

    img3 = Image.open(r'photo/'+liste[2])
    img3 = img3.resize((width,height))
    photoImg3=  ImageTk.PhotoImage(img3)

    img4 = Image.open(r'photo/'+liste[3])
    img4 = img4.resize((width,height))
    photoImg4 =  ImageTk.PhotoImage(img4)

    #Récupération du nom de l'image 
    NomPhoto1=str.split(liste[0], '.')
    NomPhoto2=str.split(liste[1], '.')
    NomPhoto3=str.split(liste[2], '.')
    NomPhoto4=str.split(liste[3], '.')
    
    #Création de 4 objets images
    imageclass1 = Laphoto(NomPhoto1[0],frame,2,0,lettre_choisie)
    imageclass2 = Laphoto(NomPhoto2[0],frame2,2,1,lettre_choisie)
    imageclass3 = Laphoto(NomPhoto3[0],frame3,3,0,lettre_choisie)
    imageclass4 = Laphoto(NomPhoto4[0],frame4,3,1,lettre_choisie)
    
    #Initialisation des 4 boutons 
    bouton = Button(frame,image=photoImg1, command= lambda : imageclass1.verif(),height = 230, width = 440)
    bouton2 = Button(frame2,image=photoImg2, command=lambda : imageclass2.verif(),height = 230, width = 440)
    bouton3 = Button(frame3,image=photoImg3, command=lambda : imageclass3.verif(),height = 230, width = 440)
    bouton4 = Button(frame4,image=photoImg4, command=lambda : imageclass4.verif(),height = 230, width = 440)
    
    def fctglobal():
      imageclass1.verif()
      imageclass2.verif()
      imageclass3.verif()
      imageclass4.verif()
     
    # Création du bouton permettant de passer à la question suivante et du bouton permettant de révélé toutes les réponses
    boutonsuivant = Button(fenetre,text="→", command=lambda :fctsuivant(),height = 2, width = 8,bg='#53BFFF', font=("Courrier",30),bd=0,fg="white")
    boutonverifglobal = Button(fenetre,text="X", command=lambda : fctglobal(),height = 2, width = 8,bg='#53BFFF', font=("Courrier",30),bd=0,fg="white")

    # Mise en place des boutons dans la fenêtre
    boutonsuivant.grid(row=0,column=1)
    boutonverifglobal.grid(row=4,column=1)
  
    bouton.grid(row=2,column=0)
    bouton2.grid(row=2,column=1)
    bouton3.grid(row=3,column=0)
    bouton4.grid(row=3,column=1)
    #Mise en place des frames dans la fenêtre
    frame.grid(row=2,column=0)
    frame2.grid(row=2,column=1)
    frame3.grid(row=3,column=0)
    frame4.grid(row=3,column=1)
    fenetre.mainloop()
    
    
    return lettre
  
  # Function récupérant 4 nom d'image au hasard et les mettant dans le tableau liste
  def choiximage() :
    verificateur=''
    compteur=0
    while compteur<4 :
      photochoisi=list[random.randint(0, len(list)-1)]
      if photochoisi not in verificateur :
        liste[compteur]=photochoisi
        compteur=compteur+1

      verificateur=photochoisi+verificateur
    
    return liste
  
  #initialisation de la fenêtre
  fenetre = Tk() 
  fenetre.title("jeu de reconnaisance")
  # Dimensions min max de la fenêtre
  fenetre.maxsize(890,702)
  fenetre.minsize(890,702)
  fenetre.geometry("890x702")
  fenetre.iconbitmap("voiture.ico")
  fenetre.configure(bg='#53BFFF')
  # Définition des frames présentent dans la fenêtre
  frame = Frame(fenetre,bg='black',height = 200, width = 440)
  frame2 = Frame(fenetre,bg='#FCF34F',height = 200, width = 440)
  frame3= Frame(fenetre,bg='#8CE34F',height = 200, width = 440)
  frame4= Frame(fenetre,bg='#8CF344',height = 200, width = 440)
  
  lettre = fctsuivant()


