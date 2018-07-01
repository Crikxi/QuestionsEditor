# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:24:15 2018

@author: Bastien
"""

import tkinter
import json
import tkinter.filedialog
import tkinter.messagebox
import index

def newFile(gvars, resetTextures=True):
    rep = tkinter.messagebox.askokcancel(title="Etes vous sur ?", message="La sauvegarde actuelle sera supprimé.\nEtes-vous sur de vouloir créer\nun nouveau niveau")
    if(rep == True):
        gvars.questionsList = []
    index.loadMenu(gvars)
    

def openFile(gvars):
    fileName = tkinter.filedialog.askopenfilename(defaultextension=".json", filetypes=[("Fichier question", "*.json")])
    if(fileName == None or fileName == ''):
        return
    try:        
        file = open(fileName, mode='r')
        loadSave(gvars, file.read())
        file.close()
        index.loadMenu(gvars)
    except: 
        print("ERROR")
        tkinter.messagebox.showerror("Erreur", "Impossible de charger les questions")
    

def saveFile(gvars):
    fileName = tkinter.filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Fichier question", "*.json")])
    if(fileName == None or fileName == ''):
        return
    file = open(fileName, mode='w')
    file.write(createSave(gvars))
    file.close()
    

def createSave(gvars):#convert and create save
    return json.dumps({'saveVersion': 0, 'questionsList': gvars.questionsList})

def loadSave(gvars, content):#crontary of createSave
    save = json.loads(content)

    
    gvars.questionsList = save["questionsList"]
