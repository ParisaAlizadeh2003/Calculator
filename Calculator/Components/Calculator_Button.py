from tkinter import *

class CalculatorButtons:   
    def __init__(self, root, entry):
        self.root = root 
        self.entry = entry
        self.value1 = 0
        self.value2 = 0
        self.operator = ''
       
    def on_button_click(self,textbtn):
        match textbtn:
            case '+':
                self.value1 = float(self.entry.get())
                self.operator = '+'
                self.entry.delete(0, END)
            case '-':
                self.value1 = float(self.entry.get())
                self.operator = '-'
                self.entry.delete(0, END)
            case '*':
                self.value1 = float(self.entry.get())
                self.operator = '*'
                self.entry.delete(0, END)
            case '/':
                self.value1 = float(self.entry.get())
                self.operator = '/'
                self.entry.delete(0, END)
            case '=':
                result = 0
                self.value2 = float(self.entry.get())
                self.entry.delete(0, END)
                try:
                    if self.operator == '+':
                       result = self.value1 + self.value2
                    elif self.operator == '-':
                        result = self.value1 - self.value2
                    elif self.operator == '*':
                        result = self.value1 * self.value2
                    elif self.operator == '/':
                        result = self.value1 / self.value2                
                    self.entry.insert(0, str(result))
                except ZeroDivisionError:
                    self.entry.insert(0, "Error")
                except SyntaxError: 
                    self.entry.insert(0, "Error")
            case 'CL':
                self.entry.delete(0, END)
                CalculatorButtons.value1 = 0
                CalculatorButtons.value2 = 0
                CalculatorButtons.operator = ''
            case _:
                self.entry.insert(END, textbtn)
         
    def main(self,textbtn, x , y):
        btn = Button(self.root, text=textbtn, font=("Arial", 18), width=5, height=2, 
                                bg="#34495E", fg="white", relief=RAISED, bd=5,command=lambda :self.on_button_click(textbtn))
        btn.grid(row=x, column=y,  sticky="nsew")