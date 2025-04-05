# from tkinter import *

# class CalculatorButtons:   
#     def __init__(self, root, entry):
#         self.root = root 
#         self.entry = entry
#         self.value1 = 0
#         self.value2 = 0
#         self.operator = ''
       
#     def on_button_click(self,textbtn):
#         match textbtn:
#             case '+':
#                 self.value1 = float(self.entry.get())
#                 self.operator = '+'
#                 self.entry.delete(0, END)
#             case '-':
#                 self.value1 = float(self.entry.get())
#                 self.operator = '-'
#                 self.entry.delete(0, END)
#             case '*':
#                 self.value1 = float(self.entry.get())
#                 self.operator = '*'
#                 self.entry.delete(0, END)
#             case '/':
#                 self.value1 = float(self.entry.get())
#                 self.operator = '/'
#                 self.entry.delete(0, END)
#             case '=':
#                 result = 0
#                 self.value2 = float(self.entry.get())
#                 self.entry.delete(0, END)
#                 try:
#                     if self.operator == '+':
#                        result = self.value1 + self.value2
#                     elif self.operator == '-':
#                         result = self.value1 - self.value2
#                     elif self.operator == '*':
#                         result = self.value1 * self.value2
#                     elif self.operator == '/':
#                         result = self.value1 / self.value2                
#                     self.entry.insert(0, str(result))
#                 except ZeroDivisionError:
#                     self.entry.insert(0, "Error")
#                 except SyntaxError: 
#                     self.entry.insert(0, "Error")
#             case 'CL':
#                 self.entry.delete(0, END)
#                 CalculatorButtons.value1 = 0
#                 CalculatorButtons.value2 = 0
#                 CalculatorButtons.operator = ''
#             case _:
#                 self.entry.insert(END, textbtn)
         
#     def main(self,textbtn, x , y):
#         btn = Button(self.root, text=textbtn, font=("Arial", 18), width=5, height=2, 
#                                 bg="#34495E", fg="white", relief=RAISED, bd=5,command=lambda :self.on_button_click(textbtn))
#         btn.grid(row=x, column=y,  sticky="nsew")


from tkinter import *

class CalculatorButtons:
    def __init__(self, root, entry):
        self.root = root 
        self.entry = entry
        self.value1 = 0
        self.value2 = 0
        self.operator = ''

        self.button_frame = Frame(self.root) 
        self.button_frame.grid(row=1, column=0, columnspan=4, pady=20, padx=20)

    def on_button_click(self, textbtn):
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

    def create_canvas_button(self, textbtn, x, y, bg_color):
        button_canvas = Canvas(self.button_frame, width=110, height=55, bg=bg_color, bd=0, highlightthickness=0)
        button_canvas.grid(row=x, column=y, sticky="nsew", padx=3, pady=3)  # Reduced gap between buttons
        button_canvas.create_text(55, 27.5, text=textbtn, fill="white", font=('Arial', 21))
        button_canvas.create_rectangle(0, 0, 110, 55, outline="#36454F", width=5)  # Slightly larger button
        button_canvas.bind("<Button-1>", lambda event, textbtn=textbtn: self.on_button_click(textbtn))

    def main(self, textbtn, x, y):
        self.create_canvas_button(textbtn, x, y, bg_color="#0e0e1a")
        self.button_frame.grid_rowconfigure(x, weight=1)
        self.button_frame.grid_columnconfigure(y, weight=1)
