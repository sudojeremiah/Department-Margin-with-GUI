# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:22:25 2019

@author: Jeremy
"""

import numpy as np
from tkinter import *
 
window = Tk()
 
window.title("DCM Margin Calculator")

window.geometry('350x200')

cost_input = Label(window, text="Please enter cost: ", font=("Arial Bold", 10))

cost_input.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():
 
    input = "Cost is: " + txt.get()
 
    cost_inpu.configure(text= input)

btn = Button(window, text="Enter", command=clicked)

btn.grid(column=2, row=0)
 
window.mainloop()

Dictionary = {"bake off":.4, "baked goods":.36, "prep foods":.50, 
              "specialty":.51, "coffee bar":.76, "sandwiches":.56, 
              "packaged":.42, "bulk":.49, "frozen":.33, "refrigerated":.31, 
              "beer":.26, "wine":.33, "produce":.38, "meat":.30, "supplements":.43, 
              "body care":.43, "mercantile":.45}

for key in Dictionary:
    print(key," - ", Dictionary[key])
    
Cost = float(input("Please enter cost: "))

Department = input("Please enter department name: ")

Price = Cost/(Dictionary[Department] -1)*-1

Price_round = np.round(Price,2)

print("Price at margin is:", Price_round)