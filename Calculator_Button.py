from tkinter import *

class CalculatorButtons:   
    def __init__(self, root):
        self.root = root 
       
    def onClick():
        pass
         
    def main(self,textbtn, x , y):
        btn = Button(self.root,text=textbtn)
        btn.place(x = x, y = y,width=80, height=40)