from tkinter import *
from Components.Calculator_Entry import result_input
from Components.Calculator_Button import CalculatorButtons

root = Tk()
btns = [ '1', '2' , '3' , '-' , '4' , '5' , '6' , '*' ,  '7' , '8' , '9' , '+' , '0' ,'=' ,'/','CL']

def main_fram(): 
    root.title("Calculator") 
    root.geometry('400x430')
    root.resizable(width=True,height=False)
    root.configure(bg="#34495E")

def buttons(entry):
    counter = 0
    clubtn = CalculatorButtons(root, entry)
    for i in range(1,11,3):
        for j in range(4):
            clubtn.main(btns[counter],i,j)
            counter += 1
    
def main():
    main_fram()
    entry = result_input(root)
    buttons(entry)
    root.mainloop() 
    
if __name__ == "__main__":
    main()