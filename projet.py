
import csv
from tkinter import *
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
from Imagerecup import * 
import random
from tkinter.messagebox import *



tab=["a","b","d","é","è","f","g","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]
liste=['','','','']
width = 440
height = 230
class Enfant:
  def __init__(self, name, score):
    self.name = name
    self.score = score




def cliquebtnfaux(couleur,buton,cadre,ligne,colonne,mot,lettre) : 
  if lettre in mot : 
    buton = Label(cadre,text="  ",bg="#85F450",height = 15, width = 62)
    buton.grid(row=ligne,column=colonne)
  else :
    buton = Label(cadre,text="  ",bg="#FF7F53",height = 15, width = 62)
    buton.grid(row=ligne,column=colonne)


def fctsuivant() :
  lettre = Label(fenetre, text="     ", font=("Courrier",30))
  lettre.grid(row=0,column=0)
  lettre_choisie=tab[random.randint(0, len(tab)-1)]
  lettre = Label(fenetre, text="lettre : "+lettre_choisie, font=("Courrier",30),bg='#53BFFF',fg="white",width='7')
  lettre.grid(row=0,column=0)
  choiximage()
  
  
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
  
  
  NomPhoto1=str.split(liste[0], '.')
  NomPhoto2=str.split(liste[1], '.')
  NomPhoto3=str.split(liste[2], '.')
  NomPhoto4=str.split(liste[3], '.')
  
  bouton = Button(frame,image=photoImg1, command= lambda : cliquebtnfaux("red",bouton,frame,2,0,NomPhoto1[0],lettre_choisie),height = 230, width = 440)
  bouton2 = Button(frame2,image=photoImg2, command=lambda : cliquebtnfaux("red",bouton2,frame2,2,1,NomPhoto2[0],lettre_choisie),height = 230, width = 440)
  bouton3 = Button(frame3,image=photoImg3, command=lambda : cliquebtnfaux("red",bouton3,frame3,3,0,NomPhoto3[0],lettre_choisie),height = 230, width = 440)
  bouton4 = Button(frame4,image=photoImg4, command=lambda : cliquebtnfaux("red",bouton4,frame4,3,1,NomPhoto4[0],lettre_choisie),height = 230, width = 440)

  boutonsuivant = Button(fenetre,text="suivant", command=fctsuivant,height = 2, width = 8,bg='#53BFFF', font=("Courrier",30),bd=0,fg="white")


  boutonsuivant.grid(row=0,column=1)
 
  

  bouton.grid(row=2,column=0)
  bouton2.grid(row=2,column=1)
  bouton3.grid(row=3,column=0)
  bouton4.grid(row=3,column=1)

  frame.grid(row=2,column=0)
  frame2.grid(row=2,column=1)
  frame3.grid(row=3,column=0)
  frame4.grid(row=3,column=1)
  fenetre.mainloop()

  return lettre






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




fenetre = Tk() 
fenetre.title("jeu de reconnaisance")
fenetre.maxsize(890,602)
fenetre.minsize(890,602)
fenetre.geometry("890x602")
fenetre.iconbitmap("voiture.ico")
fenetre.configure(bg='#53BFFF')

frame = Frame(fenetre,bg='black',height = 200, width = 440)
frame2 = Frame(fenetre,bg='#FCF34F',height = 200, width = 440)
frame3= Frame(fenetre,bg='#8CE34F',height = 200, width = 440)
frame4= Frame(fenetre,bg='#8CF344',height = 200, width = 440)





lettre = fctsuivant()
lettre.grid(row=0,column=0)




