from tkinter import *
from Calculator_Entry import result_input
from Calculator_Button import CalculatorButtons

root = Tk()
btns = [
    {"textbtn":'1' , "x":15,"y":50},
    {"textbtn":'2' , "x":115,"y":50},
    {"textbtn":'3' , "x":215,"y":50},
    {"textbtn":'/' , "x":315,"y":50},
    
    {"textbtn":'4' , "x":15,"y":100},
    {"textbtn":'5' , "x":115,"y":100},
    {"textbtn":'6' , "x":215,"y":100},
    {"textbtn":'*' , "x":315,"y":100},
    
    {"textbtn":'7' , "x":15,"y":150},
    {"textbtn":'8' , "x":115,"y":150},
    {"textbtn":'9' , "x":215,"y":150},
    {"textbtn":'0' , "x":315,"y":150},
    
    {"textbtn":'+' , "x":15,"y":200},
    {"textbtn":'-' , "x":115,"y":200},
    {"textbtn":'=' , "x":215,"y":200},
    {"textbtn":'CL' , "x":315,"y":200}
]
def main_fram():
    root.title("Calculator")
    root.geometry('410x250')
    root.resizable(width=False,height=False)
    root.configure(bg='#f5f5f5')

def buttons():
    clubtn = CalculatorButtons(root)
    for btn in btns:
        clubtn.main(**btn)
    
def main():
    main_fram()
    result_input(root)
    buttons()
    root.mainloop() 
    
if __name__ == "__main__":
    main()