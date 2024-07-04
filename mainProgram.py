"""
    ----------------------------------------------------------
        +Authors:
               *Duressa shukuri
               *Segni Girma
               *Firomsa Hika
               *Selamu Feleke


    ----------------------------------------------------------
"""

import tkinter as tk
from SearchInterface import SearchApp
if __name__ == "__main__":
    root = tk.Tk()
    app = SearchApp(root)
    app.centerWindow(900, 500)
    root.mainloop()
"""
 ------------------------------------------------------------------
        -All sections of the program is build based on the lecture give by instructor kibrom
                   -on IR System at Adama science and Technology University
        -Stemming section of the program uses the porters original implementation.
                   -for further reference:https://tartarus.org/martin/PorterStemmer/def.txt                                                             
 -------------------------------------------------------------------
"""
