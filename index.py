# -*- coding: utf-8 -*-

import tkinter
import tkinter.filedialog
import tkinter.messagebox

import globalVars


from manageur.save import saveManageur
from manageur.questions.gui import createQuestion
from manageur.questions.gui import displayQuestion



from functools import partial

import aide


def loadMenu(gvars):
    gvars.liste.delete(0, tkinter.END)
    for question in gvars.questionsList:
        gvars.liste.insert(tkinter.END, question["question"])
    gvars.liste.config(width=0)


def listClick(e):
    if len(gvars.liste.curselection()) == 0:
        return
    displayQuestion.load(gvars, gvars.questionsList[gvars.liste.curselection()[0]])

def addQuestion():
    createQuestion.load(gvars)
    

def removeSelectedQuestion():
    try:
        del gvars.questionsList[gvars.liste.curselection()[0]]
        loadMenu(gvars)
    except:
        tkinter.messagebox.showerror("Erreur", "Vous n'avez rien sélectionné")


if __name__ == '__main__':
    gvars = globalVars.GVars()
    gvars.fenetre = tkinter.Tk()
    
    #globalVars.fenetre.attributes("-fullscreen", True)
    gvars.fenetre.geometry("1280x720")
    
    
    
    menuPrincipal = tkinter.Menu(gvars.fenetre)
    
    menuFichier = tkinter.Menu(menuPrincipal, tearoff=False)        
    menuPrincipal.add_cascade(label = "Fichier", menu = menuFichier)
    
    menuFichier.add_command(label = "Nouveau", command = partial(saveManageur.newFile, gvars))
    menuFichier.add_command(label = "Ouvrir", command = partial(saveManageur.openFile, gvars))
    menuFichier.add_command(label = "Sauvegarder", command = partial(saveManageur.saveFile, gvars))
    
    
    menuPrincipal.add_command(label = "Ajouter question", command=addQuestion)
    menuPrincipal.add_command(label = "Supprimer question sélectionnée", command=removeSelectedQuestion)
    
    menuPrincipal.add_command(label = "Aide", command=aide.displayHelp)
    
    gvars.fenetre.configure(menu = menuPrincipal)
    
    
    gvars.liste = tkinter.Listbox(gvars.fenetre)

    loadMenu(gvars)
    

    gvars.liste.bind('<Double-Button>', listClick)
    gvars.liste.pack(anchor=tkinter.CENTER, expand=True, fill=tkinter.BOTH)
    
    gvars.fenetre.mainloop()
