# -*- coding: utf-8 -*-

import tkinter
import index

window = None

def load(gvars):
    global window
    try:        
        window.focus_force()
        for widget in window.pack_slaves():
            widget.destroy()
    except:
        window = tkinter.Toplevel()
        
        
    tkinter.Label(window, text="Question: ").pack()
    qu = tkinter.Entry(window, width=107)      
    qu.pack()
    
    tkinter.Label(window, text="Astuce:").pack()
    astuce = tkinter.Entry(window, width=107)
    astuce.pack()
    
    tkinter.Label(window, text="Bonnes réponses:").pack()
    goodAnswers = tkinter.Text(window, height=10)
    goodAnswers.pack()
    
    tkinter.Label(window, text="Mauvaises réponses:").pack()
    badAnswers = tkinter.Text(window)
    badAnswers.pack()
    
       
    createButton = tkinter.Button(window, text="Créer la question", command=lambda: onClickOpen(gvars, qu, goodAnswers, badAnswers, astuce))    
    createButton.pack()



def onClickOpen(gvars, qu, goodAnswer, badAnswer, astuce):
    try:
        question = qu.get()
        astuceTxt = astuce.get()
        goodRepTxt = goodAnswer.get("1.0", tkinter.END)#1.0 Ligne 1 caractère 0
        badRepTxt = badAnswer.get("1.0", tkinter.END)
    except Exception as e:
        print(e)
        tkinter.messagebox.showerror("Erreur", "Une erreur est survenue, \navez-vous tous bien remplis ?")
        return
    
    goodRepList = goodRepTxt.split("\n")
    badRepList = badRepTxt.split("\n")
    
    quDict = {'question': question}
    reponses = []
    for rep in goodRepList:
        if(rep != ""):
            reponses.append([rep, True])
            
    for rep in badRepList:
        if(rep != ""):
            reponses.append([rep, False])
     
    quDict['reponses'] = reponses
    quDict['astuce'] = astuceTxt
    gvars.questionsList.append(quDict)
    index.loadMenu(gvars)