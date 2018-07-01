# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 03:43:37 2018

@author: Bastien
"""
import tkinter

def displayHelp():
    window = tkinter.Toplevel()
        
    text = tkinter.Label(window, text="Créateur de liste de question 0.0.1\nCréé par Crikxi(Bastien)\nEncore en développement\n\nVous permet de créer votre propre liste de question pour la botte temporelle")
    text.pack()