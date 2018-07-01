# -*- coding: utf-8 -*-

import tkinter

window = None

def load(gvars, qu):
    global window
    try:        
        window.focus_force()
        for widget in window.pack_slaves():
            widget.destroy()
    except:
        window = tkinter.Toplevel()
        
        
    tkinter.Label(window, text="Question: " + qu["question"]).pack()
    
    tkinter.Label(window, text="Astuce:" + qu["astuce"]).pack()
    
    tkinter.Label(window, text="Réponses:").pack()
    for rep in qu["reponses"]:
        
        if rep[1] == True:
            color = "green"
        else:
            color = "red"
        tkinter.Label(window, text="\t" + rep[0], fg=color).pack()